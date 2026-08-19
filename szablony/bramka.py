#!/usr/bin/env python3
"""Szablon: zbiorcza bramka jakości pracy naukowej — jedno polecenie, wszystkie kontrole.

Idea: każdy incydent jakości (regresja przy scalaniu, sklejenie po podmianie masowej,
rysunek w złej proporcji, sprzeczna liczba między rozdziałami) ma OSOBNĄ, prostą kontrolę,
która by go wykryła. Problem nie jest brak kontroli — jest rozproszenie po wielu skryptach
odpalanych ręcznie, kiedy ktoś sobie o nich przypomni. Ta bramka agreguje je w jeden przebieg
i wpina się PRZED skład dokumentu: skrypt eksportu przerywa się, gdy bramka zwróci błąd.

To jest SZKIELET do dostosowania, nie gotowiec — podmień:
- listę plików źródłowych (ROZDZIALY),
- wzorce błędów w k_odmiana() / k_anglicyzmy() na własne, znane błędy tej konkretnej pracy,
- próg WZOROW_MINIMUM po pierwszym policzeniu wzorów w swoim dokumencie.

Użycie:
    python3 bramka.py            # pełny przebieg, kod wyjścia 1 przy błędach
    python3 bramka.py --szybka   # bez kontroli wymiarów rysunków (zwykle najwolniejszej)
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

# --- DOSTOSUJ: katalog z rozdziałami i lista plików w kolejności pracy ---
BAZA = Path(__file__).resolve().parent
ROZDZIALY = sorted((BAZA / "rozdzialy").glob("*.md"))
BIBLIOGRAFIA = BAZA / "rozdzialy" / "bibliografia.md"

bledy: list[str] = []


def blad(nazwa, opis):
    bledy.append(f"{nazwa}: {opis}")


def czysta_proza(tekst):
    """Usuwa z tekstu elementy, w których normalne reguły prozy nie obowiązują
    (kod, komentarze robocze, adresy, cytaty w nawiasach kwadratowych, kursywa)."""
    tekst = re.sub(r"<!--.*?-->", "", tekst, flags=re.S)
    tekst = re.sub(r"`[^`]*`", "", tekst)
    tekst = re.sub(r"^\[\d+\].*$", "", tekst, flags=re.M)
    tekst = re.sub(r"https?://\S+", "", tekst)
    tekst = re.sub(r"\*[^*\n]{3,}\*", "", tekst)
    return tekst


# ── 1. znaczniki konfliktu git pozostawione po nieudanym mergu ─────────────────
def k_konflikty():
    for p in ROZDZIALY:
        tekst = p.read_text(encoding="utf-8")
        for wzor in ("<<<<<<<", ">>>>>>>"):
            if wzor in tekst:
                blad("konflikty git", f"{p.name} zawiera {wzor}")


# ── 2. ślady sklejenia po podmianach masowych (np. "zrobiłaa") ─────────────────
def k_sklejenia():
    # podwojona samogłoska/spółgłoska na końcu wyrazu — typowy ślad kolizji dwóch
    # niezależnych podmian tekstowych wykonanych bez granicy słowa (\b)
    wzor = re.compile(r"\b\w+(?:aa|ee|ii|oo|uu|łaa|ąą|ęę|ćć)\b")
    for p in ROZDZIALY:
        for m in wzor.finditer(czysta_proza(p.read_text(encoding="utf-8"))):
            blad("sklejenie po podmianie", f"{p.name}: „{m.group(0)}”")


# ── 3. anglicyzmy, które miały zostać spolszczone (PODMIEŃ listę na własną) ────
def k_anglicyzmy():
    # przykładowa lista — podmień na terminy własnej pracy, które promotor/
    # recenzent kazał spolszczyć, z uwzględnieniem świadomych wyjątków
    ANGLICYZMY_DO_SPOLSZCZENIA = []  # np. ["frontier", "on-premise"]
    if not ANGLICYZMY_DO_SPOLSZCZENIA:
        return
    rx = re.compile(r"\b(" + "|".join(ANGLICYZMY_DO_SPOLSZCZENIA) + r")\b", re.I)
    for p in ROZDZIALY:
        for m in rx.finditer(czysta_proza(p.read_text(encoding="utf-8"))):
            blad("anglicyzm", f"{p.name}: „{m.group(0)}”")


# ── 4. znane wzorce błędnej zgody gramatycznej wokół podmienionych fraz ────────
def k_odmiana():
    # przykładowe wzorce — podmień na błędy faktycznie wykryte w swojej pracy;
    # to NIE jest ogólny sprawdzacz gramatyki, tylko lista znanych wcześniej usterek
    WZORCE = [
        # (r"regex łapiący znany błąd", "opis błędu"),
    ]
    for p in ROZDZIALY:
        t = czysta_proza(p.read_text(encoding="utf-8"))
        for rx, opis in WZORCE:
            for m in re.finditer(rx, t):
                blad("zgoda gramatyczna", f"{p.name}: „{m.group(0)}” ({opis})")


# ── 5. cytowania numeryczne w obu kierunkach ────────────────────────────────────
def k_cytowania():
    if not BIBLIOGRAFIA.exists():
        return
    bib_t = BIBLIOGRAFIA.read_text(encoding="utf-8")
    bib = {int(m.group(1)) for m in re.finditer(r"^\[(\d{1,3})\]", bib_t, re.M)}
    cyt = set()
    for p in ROZDZIALY:
        cyt |= {int(m.group(1)) for m in
                re.finditer(r"(?<!\^)\[(\d{1,3})\]", czysta_proza(p.read_text(encoding="utf-8")))}
    for n in sorted(cyt - bib):
        blad("cytowania", f"[{n}] przywołane w tekście, brak pozycji w bibliografii")
    for n in sorted(bib - cyt):
        blad("cytowania", f"[{n}] w bibliografii, nigdy nie przywołane w tekście")


# ── 6. numeracja rysunków ciągła + każdy znacznik ma odpowiadający plik ────────
def k_rysunki():
    # zakłada znacznik postaci {{RYSUNEK: `sciezka`}} — podmień na własną konwencję
    for p in ROZDZIALY:
        t = p.read_text(encoding="utf-8")
        for m in re.finditer(r"\{\{RYSUNEK:\s*`([^`]+)`\s*\}\}", t):
            if not (BAZA / m.group(1)).exists():
                blad("rysunki", f"{p.name}: brak pliku {m.group(1)}")
    numery = {}
    for p in ROZDZIALY:
        for m in re.finditer(r"^Rysunek (\d+)\.(\d+)\.", p.read_text(encoding="utf-8"), re.M):
            numery.setdefault(int(m.group(1)), set()).add(int(m.group(2)))
    for rozdz, nn in sorted(numery.items()):
        oczekiwane = set(range(1, max(nn) + 1))
        for brak in sorted(oczekiwane - nn):
            blad("rysunki", f"luka w numeracji: brak rysunku {rozdz}.{brak}")


# ── 7. liczba wzorów matematycznych nie może spaść przy scalaniu ───────────────
# Ustaw po pierwszym policzeniu wzorów w swojej pracy; podnoś przy każdym dodanym.
WZOROW_MINIMUM = 0


def k_wzory():
    if WZOROW_MINIMUM <= 0:
        return
    n = sum(len(re.findall(r"\$\$[^$]+\$\$", p.read_text(encoding="utf-8"), re.S))
            for p in ROZDZIALY)
    if n < WZOROW_MINIMUM:
        blad("wzory", f"w plikach jest {n} wzorów, minimum to {WZOROW_MINIMUM} — "
                      f"któryś zniknął (sprawdź ostatnie scalenia gałęzi)")


# ── 8. delegacja do skryptów pomocniczych (dostosuj listę do własnych narzędzi) ─
def k_skrypty(szybka):
    zadania = [
        # ("kontrola integralności", [sys.executable, "kontrola_integralnosci.py", "--porownaj"]),
        # ("wymiary rysunków", [sys.executable, "sprawdz_wymiary_rysunkow.py"]),
    ]
    for nazwa, cmd in zadania:
        if szybka and "wymiary" in nazwa:
            continue
        w = subprocess.run(cmd, cwd=BAZA, capture_output=True, text=True)
        if w.returncode != 0:
            wynik = (w.stdout + w.stderr).strip().splitlines()
            blad(nazwa, wynik[-1][:160] if wynik else "nieznany błąd")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--szybka", action="store_true")
    a = ap.parse_args()

    k_konflikty()
    k_sklejenia()
    k_anglicyzmy()
    k_odmiana()
    k_cytowania()
    k_rysunki()
    k_wzory()
    k_skrypty(a.szybka)

    if bledy:
        print(f"BRAMKA: {len(bledy)} błędów\n")
        for b in bledy:
            print("  ", b)
        return 1
    print("BRAMKA: wszystkie kontrole przeszły "
          f"({'tryb szybki, bez wymiarów rysunków' if a.szybka else 'pełny przebieg'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
