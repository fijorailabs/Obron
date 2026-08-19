#!/usr/bin/env python3
"""Szablon: numeracja bibliografii wg kolejności pierwszego cytowania w tekście.

Styl cytowania numerycznego (pozycje NIE ułożone alfabetycznie, tylko w kolejności
pierwszego przywołania w tekście: [1] pierwsze cytowane źródło, [2] drugie...)
wymaga, żeby numer rósł wraz z kolejnością występowania w dokumencie. Praca pisana
i poprawiana wieloma turami łatwo to łamie — pozycja [88] cytowana pierwszy raz w
rozdziale 3, podczas gdy pozycja [12] pojawia się dopiero w rozdziale 5.

Podmiana idzie przez znacznik pośredni (nie wprost stary_numer -> nowy_numer),
bo mapowanie nie jest monotoniczne — podmiana wprost nadpisywałaby numery, które
inny wpis mapy właśnie przeliczył na tę samą wartość.

To jest SZKIELET — podmień KOLEJNOSC na własną listę plików rozdziałów w kolejności,
w jakiej faktycznie występują w złożonym dokumencie, i ścieżkę do pliku bibliografii.

Użycie (z katalogu pracy):
    python3 renumeracja_bibliografii.py             # tylko raport, nic nie zapisuje
    python3 renumeracja_bibliografii.py --zastosuj   # przenumerowuje pliki na dysku
"""
import re
import sys
from pathlib import Path

BAZA = Path(__file__).resolve().parent

# --- DOSTOSUJ: kolejność plików rozdziałów, w jakiej występują w dokumencie ---
KOLEJNOSC = ['wstep', 'rozdzial-1', 'rozdzial-2', 'rozdzial-3', 'rozdzial-4',
             'rozdzial-5', 'zakonczenie', 'zalaczniki']
BIBLIOGRAFIA = BAZA / 'rozdzialy' / 'bibliografia.md'

RX_CYT = re.compile(r'(?<!\^)\[(\d{1,3})\]')


def czysty(t):
    """Wycina sekcje robocze i kod, żeby nie liczyć cytowań, których nie ma
    w wersji dla promotora/recenzenta."""
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.sub(r'`[^`]*`', '', t)
    return t


def main():
    zastosuj = '--zastosuj' in sys.argv
    porzadek = []
    for f in KOLEJNOSC:
        sciezka = BAZA / 'rozdzialy' / f'{f}.md'
        if not sciezka.exists():
            continue
        for m in RX_CYT.finditer(czysty(sciezka.read_text(encoding='utf-8'))):
            n = int(m.group(1))
            if n not in porzadek:
                porzadek.append(n)

    mapa = {stary: nowy for nowy, stary in enumerate(porzadek, 1)}
    zmienione = {k: v for k, v in mapa.items() if k != v}
    print(f"pozycji cytowanych: {len(porzadek)} | zmienia numer: {len(zmienione)}")
    if not zmienione:
        print("numeracja już zgodna z kolejnością cytowania")
        return 0
    for k, v in sorted(zmienione.items())[:12]:
        print(f"   [{k}] -> [{v}]")
    if len(zmienione) > 12:
        print(f"   ... i {len(zmienione) - 12} dalszych")

    if not zastosuj:
        print("\n(raport — nic nie zapisano; uruchom z --zastosuj)")
        return 0

    # 1. teksty rozdziałów — przez znacznik pośredni, mapowanie nie jest monotoniczne
    for f in KOLEJNOSC:
        p = BAZA / 'rozdzialy' / f'{f}.md'
        if not p.exists():
            continue
        t = p.read_text(encoding='utf-8')
        t = RX_CYT.sub(lambda m: f"\x02{mapa.get(int(m.group(1)), int(m.group(1)))}\x02", t)
        t = re.sub(r'\x02(\d+)\x02', r'[\1]', t)
        p.write_text(t, encoding='utf-8')

    # 2. bibliografia — przenumerowanie i przesortowanie wg nowych numerów
    if BIBLIOGRAFIA.exists():
        tb = BIBLIOGRAFIA.read_text(encoding='utf-8')
        pozycje, naglowek = {}, []
        for linia in tb.split('\n'):
            m = re.match(r'^\[(\d{1,3})\]\s*(.*)$', linia)
            if m:
                pozycje[int(m.group(1))] = m.group(2)
            elif not pozycje:
                naglowek.append(linia)
        nowe = sorted((mapa.get(s, s), tresc) for s, tresc in pozycje.items())
        BIBLIOGRAFIA.write_text(
            '\n'.join(naglowek).rstrip() + '\n\n' +
            '\n\n'.join(f"[{n}] {t}" for n, t in nowe) + '\n', encoding='utf-8')
        print(f"\nzastosowano; bibliografia: {len(nowe)} pozycji")
    return 0


if __name__ == '__main__':
    sys.exit(main())
