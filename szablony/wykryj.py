#!/usr/bin/env python3
"""
wykryj.py — deterministyczny detektor wad zdania w polskiej prozie naukowej.

Wejście pipeline'u redakcyjnego (Faza 8 w SKILL.md): tnie rozdział na akapity i zdania,
przypisuje kody kategorii z `referencje/kategorie.md` i produkuje zadania dla agenta
redaktora.

⛔ Trafienie tego skryptu jest PODPOWIEDZIĄ, nie wyrokiem. Skrypt widzi tylko to, co da
się złapać wyrażeniem regularnym: znaki pauzy, dwukropki, długość, anglicyzmy z zamkniętej
listy, nawiasy z parametrami. NIE widzi kolokwializmów, metafor, zdań niewynikających
z poprzedniego, zawyżonych twierdzeń ani terminów użytych bez wprowadzenia.

Dlatego skrypt oddaje redaktorowi WSZYSTKIE zdania akapitu, a nie tylko te z trafieniem.
Zdania bez trafienia dostają flagę `wymaga_kwalifikacji_agenta`. Filtrowanie zdań regexem
przed podaniem ich agentowi ukryło raz połowę rozdziału: 112 z 210 zdań nigdy nie trafiło
pod ocenę, bo nie miały trafienia mechanicznego.

Użycie:
    python3 wykryj.py rozdzialy/R1.md                    # raport czytelny dla człowieka
    python3 wykryj.py rozdzialy/R1.md --json zadania.json  # zadania dla agenta
    python3 wykryj.py rozdzialy/*.md --tylko-liczby      # sam licznik, do bramki

Kod wyjścia: 0 = brak trafień krytycznych, 1 = są trafienia kategorii krytycznych.
"""

import argparse
import json
import os
import re
import sys

# ── Konfiguracja — dostosuj pod własną pracę ────────────────────────────────

MAX_SLOW = 35          # próg twardy długości zdania (kategoria A4)
PROG_MIEKKI = 25       # między PROG_MIEKKI a MAX_SLOW kwalifikuj przy >2 myślach
MAX_LICZB_W_ZDANIU = 3  # powyżej — ściana liczb do tabeli (A6)

KRYTYCZNE = {"A1", "A16"}  # trafienia blokujące (znak pauzy i jego przebrania)

# Anglicyzmy: zamknięta lista dla dziedziny. Rozszerz o własne.
ANGLICYZMY = [
    "harness", "frontier", "workflow", "benchmark", "commit", "feedback",
    "backend", "frontend", "framework", "pipeline", "fallback", "baseline",
    "coverage", "edge case", "pull request", "code review", "prompt",
    "fine-tuning", "seed", "open-weights", "deadline", "insight", "feature",
    "release", "deployment", "case study", "know-how", "performance",
]

# Zwroty wartościujące i kolokwializmy (A12, A5) — lista startowa
WARTOSCIUJACE = [
    "warto", "niestety", "na szczęście", "zaskakująco", "ciekawie", "ciekawy",
    "oczywiście", "rzecz jasna", "po prostu", "wręcz", "znakomicie", "kluczowy",
    "fundamentalny", "przełomowy", "rewolucyjny", "imponujący", "uczciwość nakazuje",
]

# Formy osobowe (A7)
OSOBOWE = [
    r"\buważam\b", r"\bsądzę\b", r"\bzbadałem\b", r"\bzbadałam\b", r"\bmoim zdaniem\b",
    r"\bwidzimy\b", r"\bzauważmy\b", r"\brozważmy\b", r"\bnasza praca\b",
    r"\bw naszej pracy\b", r"\bprzedstawię\b", r"\bomówię\b", r"\bpokażę\b",
]

# Zawyżone czasowniki dowodowe i twierdzenia (grupa C) — najgroźniejsza kategoria
ZAWYZONE = {
    "C1": [r"\bwykazano\b", r"\budowodniono\b", r"\bdowodzi\b", r"\bprzesądza\b"],
    "C2": [r"brak\s+różnic", r"nie\s+ma\s+różnic", r"wykazano\s+brak"],
    "C3": [r"\bpierwsz\w+\s+(praca|badanie|eksperyment)", r"po\s+raz\s+pierwszy"],
    "C4": [r"w\s+literaturze\s+brak", r"nie\s+istniej\w+\s+badan", r"\bjedyn\w+\s+badanie\b"],
    "C5": [r"co\s+do\s+bitu", r"w\s+pełni\s+odtwarzaln", r"\bgwarantuje\b", r"pełn\w+\s+replikowaln"],
}

# Fragmenty chronione — nie analizujemy ich wcale
CHRONIONE = [
    (re.compile(r"^```.*?^```", re.S | re.M), "blok kodu"),
    (re.compile(r"^\s*\|.*\|\s*$", re.M), "wiersz tabeli"),
    (re.compile(r"^\s*\[\^?\d+\]:.*$", re.M), "pozycja bibliografii"),
    (re.compile(r"^\s*!\[.*$", re.M), "obraz"),
    (re.compile(r"\$\$.*?\$\$", re.S), "wzór blokowy"),
    (re.compile(r"<!--.*?-->", re.S), "komentarz"),
]

# Znak maskujący fragmenty chronione. Musi być czymś, co nie występuje w prozie.
MASKA = "\uf8ff"

# ── Cięcie tekstu ───────────────────────────────────────────────────────────

SKROTY = {"np", "tj", "tzn", "itp", "itd", "por", "ang", "łac", "ok", "m.in", "r", "s",
          "nr", "ust", "art", "poz", "rys", "tab", "wz", "dr", "prof", "mgr", "inż"}

_ZDANIE = re.compile(r"(?<=[.!?])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ„(\[])")


def zamaskuj_chronione(tekst):
    """Zastępuje fragmenty chronione placeholderami, żeby nie trafiały do analizy."""
    for wzor, _opis in CHRONIONE:
        tekst = wzor.sub(lambda m: MASKA * min(len(m.group(0)), 40), tekst)
    return tekst


def tnij_na_zdania(akapit):
    """
    Dzieli akapit na zdania z obsługą polskich skrótów.
    Nie jest doskonałe i nie musi być — redaktor dostaje też cały akapit.
    """
    kandydaci = _ZDANIE.split(akapit)
    zdania, bufor = [], ""
    for k in kandydaci:
        bufor = (bufor + " " + k).strip() if bufor else k
        ostatnie = bufor.rstrip(".!?").split()[-1].rstrip(".").lower() if bufor.split() else ""
        if ostatnie in SKROTY:
            continue
        zdania.append(bufor)
        bufor = ""
    if bufor:
        zdania.append(bufor)
    return [z for z in zdania if z.strip()]


def tnij_na_akapity(tekst):
    """Akapit = blok prozy oddzielony pustą linią. Nagłówki i listy pomijamy."""
    akapity = []
    for blok in re.split(r"\n\s*\n", tekst):
        b = blok.strip()
        if not b or b.startswith("#") or b.startswith(">"):
            continue
        if re.match(r"^\s*[-*+]\s", b) or re.match(r"^\s*\d+\.\s", b):
            continue
        if MASKA in b and len(b.replace(MASKA, "").strip()) < 20:
            continue
        akapity.append(b)
    return akapity


# ── Detektory ───────────────────────────────────────────────────────────────

def liczba_slow(zdanie):
    return len(re.findall(r"\b[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+\b", zdanie))


def liczba_liczb(zdanie):
    return len(re.findall(r"\b\d+(?:[.,]\d+)?\b", zdanie))


def wykryj_w_zdaniu(zdanie):
    """Zwraca listę (kod, dowód) dla jednego zdania."""
    traf = []
    czysty = zdanie.replace(MASKA, "")

    # A1 — myślnik w prozie
    if "—" in czysty:
        traf.append(("A1", "znak — w zdaniu"))

    # A16 — myślnik ukryty pod inny znak (półpauza albo dywiz w spacjach)
    if re.search(r"\s[–-]\s", czysty):
        traf.append(("A16", "półpauza albo dywiz w funkcji myślnika"))

    # A2 — dwukropek dokańczający myśl.
    # Fałszywe trafienia odrzucamy: godzina, proporcja, wersja, dwukropek na końcu zdania.
    for m in re.finditer(r":", czysty):
        i = m.start()
        przed, po = czysty[max(0, i - 1):i], czysty[i + 1:i + 3]
        if przed.isdigit() and po[:1].isdigit():
            continue                      # 19:30, qwen:30b, proporcja
        if not czysty[i + 1:].strip():
            continue                      # dwukropek kończący zdanie (lista poniżej)
        if re.match(r"\s+[a-ząćęłńóśźż]", czysty[i + 1:]):
            traf.append(("A2", "dwukropek w połowie zdania"))
            break

    # A3 — anglicyzmy z listy
    for a in ANGLICYZMY:
        if re.search(rf"\b{re.escape(a)}\w*\b", czysty, re.I):
            traf.append(("A3", f"anglicyzm: {a}"))

    # A4 — zdanie za długie
    n = liczba_slow(czysty)
    if n > MAX_SLOW:
        traf.append(("A4", f"{n} słów"))
    elif n > PROG_MIEKKI:
        traf.append(("A4?", f"{n} słów — sprawdź, czy nie ma więcej niż dwóch myśli"))

    # A6 — ściana liczb
    if liczba_liczb(czysty) > MAX_LICZB_W_ZDANIU:
        traf.append(("A6", f"{liczba_liczb(czysty)} wartości liczbowych — do tabeli"))

    # A7 — forma osobowa
    for wzor in OSOBOWE:
        if re.search(wzor, czysty, re.I):
            traf.append(("A7", f"forma osobowa: {wzor}"))

    # A8 — pytanie retoryczne
    if "?" in czysty:
        traf.append(("A8", "znak zapytania w prozie"))

    # A9 — parametry w nawiasach
    for m in re.finditer(r"\(([^)]{10,})\)", czysty):
        if len(re.findall(r"\d", m.group(1))) >= 3:
            traf.append(("A9", "parametry liczbowe w nawiasie — do tabeli"))
            break

    # A12 — sformułowania wartościujące
    for w in WARTOSCIUJACE:
        if re.search(rf"\b{re.escape(w)}\b", czysty, re.I):
            traf.append(("A12", f"wartościowanie: {w}"))

    # A19 — nagromadzenie wtrąceń
    if czysty.count("(") >= 2 or czysty.count(",") >= 6:
        traf.append(("A19", "nagromadzenie wtrąceń"))

    # Grupa C — zawyżone twierdzenia. Najgroźniejsza kategoria, choć regex łapie
    # tylko sformułowania; zgodność z danymi musi sprawdzić człowiek albo metodolog.
    for kod, wzory in ZAWYZONE.items():
        for wzor in wzory:
            if re.search(wzor, czysty, re.I):
                traf.append((kod, f"zawyżone twierdzenie: {wzor}"))
                break

    # B2 — nazwa własna bez odwołania (heurystyka: Wielka Litera w środku zdania,
    # bez [X] w tym samym zdaniu). Dużo fałszywych trafień, dlatego znak zapytania.
    if not re.search(r"\[\d+\]", czysty):
        srodek = " ".join(czysty.split()[1:])
        if re.search(r"\b[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]{2,}(?:\s+[A-Z][a-z]+)?\b", srodek):
            traf.append(("B2?", "nazwa własna bez odwołania — sprawdź, czy to pierwsze wystąpienie"))

    return traf


# ── Przebieg ────────────────────────────────────────────────────────────────

def przetworz(sciezka):
    surowy = open(sciezka, encoding="utf-8").read()
    tekst = zamaskuj_chronione(surowy)
    wynik = {"plik": sciezka, "akapity": []}

    for nr_a, akapit in enumerate(tnij_na_akapity(tekst), 1):
        zdania = tnij_na_zdania(akapit)
        poz = []
        for nr_z, z in enumerate(zdania, 1):
            traf = wykryj_w_zdaniu(z)
            poz.append({
                "id": f"{nr_a}.{nr_z}",
                "tekst": z.replace(MASKA, ""),
                "kategorie_wykryte_mechanicznie": sorted({k for k, _ in traf}),
                "dowody": [d for _, d in traf],
                # ⛔ To pole jest sednem skryptu: zdanie bez trafienia NIE jest
                # zdaniem poprawnym, tylko zdaniem, którego skrypt nie umie ocenić.
                "wymaga_kwalifikacji_agenta": not traf,
            })
        wynik["akapity"].append({"nr": nr_a, "kontekst": akapit.replace(MASKA, ""),
                                 "zdania": poz})
    return wynik


def raport(wynik):
    ile_zdan = sum(len(a["zdania"]) for a in wynik["akapity"])
    liczniki, krytyczne = {}, 0
    for a in wynik["akapity"]:
        for z in a["zdania"]:
            for k in z["kategorie_wykryte_mechanicznie"]:
                liczniki[k] = liczniki.get(k, 0) + 1
                if k in KRYTYCZNE:
                    krytyczne += 1

    print(f"\n{wynik['plik']}")
    print(f"  akapitów: {len(wynik['akapity'])}, zdań: {ile_zdan}")
    bez = sum(1 for a in wynik["akapity"] for z in a["zdania"] if z["wymaga_kwalifikacji_agenta"])
    print(f"  bez trafienia mechanicznego: {bez} "
          f"({100 * bez // max(ile_zdan, 1)}%) — te też idą do redaktora")
    if not liczniki:
        print("  brak trafień")
        return krytyczne
    print("  trafienia:")
    for k in sorted(liczniki, key=lambda x: -liczniki[x]):
        znacznik = " ⛔" if k in KRYTYCZNE else ""
        print(f"    {k:5} {liczniki[k]:4}{znacznik}")
    return krytyczne


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pliki", nargs="+")
    ap.add_argument("--json", help="zapisz zadania dla agenta do pliku")
    ap.add_argument("--tylko-liczby", action="store_true")
    args = ap.parse_args()

    wyniki, krytyczne = [], 0
    for p in args.pliki:
        if not os.path.isfile(p):
            print(f"pomijam (brak pliku): {p}", file=sys.stderr)
            continue
        w = przetworz(p)
        wyniki.append(w)
        krytyczne += raport(w)

    if args.json and not args.tylko_liczby:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(wyniki, fh, ensure_ascii=False, indent=2)
        print(f"\nzadania zapisane: {args.json}")

    print(f"\ntrafienia kategorii krytycznych: {krytyczne}")
    return 1 if krytyczne else 0


if __name__ == "__main__":
    sys.exit(main())
