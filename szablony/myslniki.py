#!/usr/bin/env python3
"""Szablon: zdejmowanie znaku pauzy (—) w warstwie EKSPORTU, deterministycznie.

Wielu promotorów/recenzentów czyta znak myślnika (—, em dash) w prozie naukowej
jako sygnał tekstu generowanego przez model i traktuje to jako powód do
podejrzeń o samodzielność pracy — niezależnie od tego, kto naprawdę go wpisał.

Dlaczego to jest sprawa SKŁADU, nie treści: reguła działa z kontekstu (co stoi
przed myślnikiem i co po nim), więc da się ją zapisać jako zestaw reguł
regexowych i uruchamiać przy każdym eksporcie, zero tokenów, w pełni
powtarzalnie. Poprawianie tego ręcznie przez agenta w źródle jest kosztowne
(dziesiątki wywołań modelu na dużej pracy) i podatne na regresje przy scalaniu
równoległej pracy wielu agentów.

Czego NIE rusza (myślnik jest tam poprawny i musi zostać):
- tytuły cytowanych źródeł w bibliografii/przypisach (cudza własność)
- elipsa zastępująca pominięty czasownik ("wariant A: 90%, wariant B — żaden")
- zakresy liczbowe i nazwiska dwuczłonowe zapisane półpauzą, nie myślnikiem
- wnętrze bloków kodu, wzorów, ścieżek plików, wierszy tabel

To jest SZKIELET — reguły są ogólne i sprawdzone w praktyce, ale każda praca ma
własne nietypowe konstrukcje zdaniowe. Po podmianie zawsze przeczytaj diff.

Użycie:
    from myslniki import zdejmij
    tekst_po_skladzie = zdejmij(tekst_zrodlowy)

Samodzielnie (raport, nic nie zapisuje):
    python3 myslniki.py --raport plik.md
"""
import re
import sys
from pathlib import Path

SPOJNIKI = r'(?:a|ale|lecz|natomiast|czyli|to znaczy|a więc|zatem|dlatego|przy czym|choć)'

# fragmenty chronione: wycinamy je na czas obróbki i wklejamy z powrotem bez zmian
CHRONIONE = [
    re.compile(r'`[^`]*`'),                      # kod w tekście
    re.compile(r'^\[\d+\].*$', re.M),            # pozycje bibliografii
    re.compile(r'^\[\^[^\]]+\]:.*$', re.M),      # definicje przypisów
    re.compile(r'\*[^*\n]{3,}\*'),               # tytuły kursywą
    re.compile(r'\{\{RYSUNEK:[^}]*\}\}'),        # znaczniki rysunków
    re.compile(r'[\w/.-]+\.(?:png|svg|py|md|csv|json|yaml)'),
    re.compile(r'^\s*\|.*\|\s*$', re.M),         # wiersze tabel
    re.compile(r'^Objaśnienie oznaczeń:.*?(?=\n\n)', re.M | re.S),
    re.compile(r'\$\$[^$]*\$\$'),                # wzory wyświetlane
    re.compile(r'(?<!\$)\$[^$\n]+\$(?!\$)'),      # wzory w tekście
]

# elipsa: przed myślnikiem podmiot, po nim krótka fraza bez orzeczenia, koniec zdania
RX_ELIPSA = re.compile(r'—\s+(?:żadnego|żadnej|nic|zero)\b|—\s+nie(?=[.,;)])')


def _zamroz(t):
    schowek = []
    for rx in CHRONIONE:
        def sub(m):
            schowek.append(m.group(0))
            return "\x02" + "\x03" * len(schowek) + "\x02"
        t = rx.sub(sub, t)
    return t, schowek


def _odmroz(t, schowek):
    for i in range(len(schowek), 0, -1):
        t = t.replace("\x02" + "\x03" * i + "\x02", schowek[i - 1])
    return t


def zdejmij(tekst, raport=False):
    """Zwraca tekst bez myślników w prozie. Z raport=True zwraca (tekst, statystyki)."""
    t, schowek = _zamroz(tekst)
    stat = {}

    def licz(nazwa, n=1):
        stat[nazwa] = stat.get(nazwa, 0) + n

    # 1. zakres liczbowy: "10 — 20" -> półpauza bez spacji
    t, n = re.subn(r'(?<=\d)\s*—\s*(?=\d)', '–', t)
    licz("zakres liczbowy -> półpauza", n)

    # 2. wtrącenie domknięte: "X — wtrącenie — Y" -> przecinki
    def wtracenie(m):
        licz("wtrącenie domknięte -> przecinki")
        return f", {m.group(1)}, "
    t = re.sub(r'(?<=\S) — ([^—.!?]{1,90}?) — (?=\S)', wtracenie, t)

    # 3. przed spójnikiem: "X — a więc Y" -> przecinek
    t, n = re.subn(rf' — (?={SPOJNIKI}\b)', ', ', t)
    licz("przed spójnikiem -> przecinek", n)

    # 4. elipsa: myślnik zastępuje pominięte orzeczenie -> ZOSTAJE
    licz("elipsa (zostawiona)", len(RX_ELIPSA.findall(t)))
    t = RX_ELIPSA.sub(lambda m: m.group(0).replace('—', '\x01'), t)

    # 5. dopowiedzenie na końcu zdania: "X — dopowiedzenie." -> przecinek
    def koncowe(m):
        licz("dopowiedzenie na końcu zdania -> przecinek")
        return f", {m.group(1)}{m.group(2)}"
    t = re.sub(r' — ([^—]{1,80}?)([.!?](?:\s|$))', koncowe, t)

    # 6. nagłówki: "## 1.1. Tytuł — podtytuł" -> dwukropek (konwencja tytułowa)
    def naglowek(m):
        licz("nagłówek -> dwukropek")
        return f"{m.group(1)}: {m.group(2)}"
    t = re.sub(r'^(#{1,4} [^\n—]+) — ([^\n]+)$', naglowek, t, flags=re.M)

    # 7. pozostałe wtrącenia pojedyncze: "X — Y" w środku zdania -> przecinek
    def pojedyncze(m):
        licz("wtrącenie pojedyncze -> przecinek")
        return ', '
    t = re.sub(r'(?<=[a-ząćęłńóśźż0-9,)\]”"A-ZĄĆĘŁŃÓŚŹŻ]) — (?=[a-ząćęłńóśźż0-9])', pojedyncze, t)

    # 8. myślnik w nawiasie: "(plik.py — 493 linie)" -> przecinek
    def w_nawiasie(m):
        licz("myślnik w nawiasie -> przecinek")
        return f"({m.group(1)}, {m.group(2)})"
    for _ in range(4):
        nowy = re.sub(r'\(([^()—]{1,200}) — ([^()]{1,200})\)', w_nawiasie, t)
        if nowy == t:
            break
        t = nowy

    # 9. przeczenie po myślniku: "X — nie robi Y" -> nowe zdanie
    def przeczenie(m):
        licz("przeczenie po myślniku -> nowe zdanie")
        return f". Nie {m.group(1)}"
    t = re.sub(r' — nie ([a-ząćęłńóśźż]+)', przeczenie, t)

    # 10. wtrącenie przed wielką literą/skrótem: "wersję — NULL w polu…" -> nowe zdanie
    def przed_wielka(m):
        licz("wtrącenie przed wielką literą -> nowe zdanie")
        return f". {m.group(1)}"
    t = re.sub(r'(?<=[a-ząćęłńóśźż]) — ([A-ZĄĆĘŁŃÓŚŹŻ][A-ZĄĆĘŁŃÓŚŹŻ]+\b)', przed_wielka, t)

    # 11. po zamrożonym fragmencie (np. nazwie pliku): "auth.py — 223 linie" -> przecinek
    def po_znaczniku(m):
        licz("dopowiedzenie po chronionym fragmencie -> przecinek")
        return ', '
    t = re.sub(r'(?<=\x02) — (?=[\d\[a-ząćęłńóśźż])', po_znaczniku, t)

    t = t.replace('\x01', '—')          # przywracamy elipsy
    t = _odmroz(t, schowek)

    stat["POZOSTAŁO w prozie"] = t.count('—')
    return (t, stat) if raport else t


def main():
    if "--raport" not in sys.argv:
        print(__doc__)
        return
    args = [a for a in sys.argv[1:] if a != "--raport"]
    if not args:
        sys.exit("Podaj ścieżkę pliku: python3 myslniki.py --raport plik.md")
    for sciezka in args:
        p = Path(sciezka)
        tekst = p.read_text(encoding="utf-8")
        przed = tekst.count('—')
        _, stat = zdejmij(tekst, raport=True)
        po = stat["POZOSTAŁO w prozie"]
        print(f"{p.name}: {przed} -> {po}")
        for k, v in stat.items():
            if k != "POZOSTAŁO w prozie" and v:
                print(f"  {k}: {v}")


if __name__ == '__main__':
    main()
