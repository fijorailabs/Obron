#!/usr/bin/env python3
"""Szablon: kontrola integralności — czy praca poprzednich agentów nie zniknęła.

Zasada: przed pracą zapisujesz stan (--zapisz), po pracy porównujesz (--porownaj).
Liczniki "rosnące" (rysunki, cytowania, tabele, nagłówki) nie mają prawa spaść.
Liczniki "malejące" (stary format przypisów, anglicyzmy z listy do spolszczenia,
znaki pauzy w prozie) nie mają prawa wzrosnąć. Naruszenie któregokolwiek to sygnał,
że scalenie gałęzi/praca równoległego agenta po cichu skasowała albo cofnęła
czyjąś wcześniejszą robotę — git nie zgłasza konfliktu tam, gdzie tylko jedna
strona dotknęła pliku, więc bez tej kontroli regresja przechodzi niezauważona.

Mierz na tekście PO transformacji eksportu (to, co faktycznie zobaczy promotor/
recenzent), nie na surowym źródle — niektóre kategorie (np. znaki pauzy) są
celowo obecne w źródle i usuwane dopiero w warstwie składu.

To jest SZKIELET — podmień listę ROZDZIALY i funkcję czysty() na własną
transformację eksportu (albo usuń wywołanie, jeśli mierzysz surowe źródło).

Użycie (z katalogu pracy):
    python3 kontrola_integralnosci.py                # stan wszystkich rozdziałów
    python3 kontrola_integralnosci.py rozdzial-3      # jeden rozdział
    python3 kontrola_integralnosci.py --zapisz        # migawka przed pracą
    python3 kontrola_integralnosci.py --porownaj      # różnica wobec migawki
"""
import argparse
import json
import re
import sys
from pathlib import Path

BAZA = Path(__file__).resolve().parent
MIGAWKA = BAZA / "integralnosc-migawka.json"

# --- DOSTOSUJ: lista plików rozdziałów bez rozszerzenia .md ---
ROZDZIALY = ["wstep", "rozdzial-1", "rozdzial-2", "rozdzial-3",
             "rozdzial-4", "rozdzial-5", "zakonczenie"]

# --- DOSTOSUJ: anglicyzmy z listy do spolszczenia w tej konkretnej pracy ---
RX_ANGLICYZM = re.compile(r'PODMIEN|NA|WLASNE|TERMINY')


def czysty(surowy: str) -> str:
    """Podmień na własną transformację eksportu, jeśli taką masz (usuwanie
    komentarzy roboczych, notatek, znaczników). Domyślnie zwraca tekst bez zmian."""
    return surowy


def zmierz(rozdzial: str):
    p = BAZA / "rozdzialy" / f"{rozdzial}.md"
    if not p.is_file():
        return None
    surowy = p.read_text(encoding="utf-8")
    fin = czysty(surowy)
    return {
        # rosnące albo stałe — spadek oznacza, że ktoś skasował cudzą pracę
        "rysunki": surowy.count("{{RYSUNEK:"),
        "cytowania": len(re.findall(r"\[\d+\]", fin)),
        "liczby": len(set(re.findall(r"\d+[,.]\d+", fin))),
        "tabele": len(re.findall(r"^\|", fin, re.M)),
        "naglowki": len(re.findall(r"^#{1,4} ", fin, re.M)),
        # malejące albo zerowe — wzrost oznacza regresję
        "przypisy_stare": len(re.findall(r"\[\^", fin)),
        "anglicyzmy": len(RX_ANGLICYZM.findall(fin)),
        "myslniki": fin.count("—"),
    }


ROSNACE = ("rysunki", "cytowania", "liczby", "tabele", "naglowki")
MALEJACE = ("przypisy_stare", "anglicyzmy", "myslniki")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rozdzial", nargs="?")
    ap.add_argument("--zapisz", action="store_true", help="migawka przed pracą")
    ap.add_argument("--porownaj", action="store_true", help="różnica wobec migawki")
    a = ap.parse_args()

    cele = [a.rozdzial] if a.rozdzial else ROZDZIALY
    stan = {r: zmierz(r) for r in cele if zmierz(r)}

    if a.zapisz:
        MIGAWKA.write_text(json.dumps(stan, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Migawka zapisana: {MIGAWKA}")
        print("Po pracy uruchom: python3 kontrola_integralnosci.py --porownaj")
        return

    if a.porownaj:
        if not MIGAWKA.is_file():
            sys.exit("BŁĄD: brak migawki. Najpierw --zapisz przed rozpoczęciem pracy.")
        przed = json.loads(MIGAWKA.read_text(encoding="utf-8"))
        bledy = []
        for r, teraz in stan.items():
            p = przed.get(r)
            if not p:
                continue
            for k in ROSNACE:
                if teraz[k] < p[k]:
                    bledy.append(f"{r}: {k} spadło {p[k]} → {teraz[k]} (skasowana cudza praca?)")
            for k in MALEJACE:
                if teraz[k] > p[k]:
                    bledy.append(f"{r}: {k} wzrosło {p[k]} → {teraz[k]} (regresja)")
        if bledy:
            print("INTEGRALNOŚĆ NARUSZONA\n")
            for b in bledy:
                print(f"   {b}")
            sys.exit(1)
        print("Integralność zachowana — nic nie zginęło, nic nie wróciło.")
        return

    for r, w in stan.items():
        alarm = " <-- SPRAWDŹ" if (w["przypisy_stare"] or w["anglicyzmy"]) else ""
        print(f"{r:20s} {w}{alarm}")


if __name__ == "__main__":
    main()
