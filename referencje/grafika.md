# Grafika naukowa w pracy dyplomowej

> Rysunek, tabela i wzór są treścią pracy, nie jej ozdobą. Ten plik obsługuje cały
> ich cykl: policzenie limitów przed narysowaniem, wybór formatu, uczciwe kodowanie
> danych, bramkę wymiarową przed wstawieniem i edycję istniejącej grafiki.

Ilustracja, która wygląda dobrze na ekranie, może po wpasowaniu w stronę A4 mieć
czcionkę 3 pt albo w ogóle się nie zmieścić. **Rysunek ocenia się w docelowym
rozmiarze na stronie, nigdy na monitorze.**

## Krok zero: policz, zanim narysujesz

Zanim wygenerujesz cokolwiek graficznego, ustal trzy liczby:

1. **Szerokość obszaru tekstu** w centymetrach (A4 z marginesami 2,5 cm → 16 cm;
   układ dwułamowy → szerokość jednego łamu)
2. **Dostępną wysokość** (strona minus marginesy minus miejsce na podpis i
   wiersz źródła, zwykle ok. 20 cm)
3. **Minimalną czcionkę w rysunku** — ma wyglądać jak tekst pracy, nie mniejsza

Dopiero z tych trzech liczb wynika rozmiar pliku. Odwrotna kolejność (najpierw
rysunek, potem próba dopasowania) kończy się nieczytelnym obrazkiem.

## Limity — praca dyplomowa A4, jednołamowa

| Parametr | Wartość |
|---|---|
| maksymalna szerokość | 15,24 cm (6 cali — obszar tekstu przy marginesach 2,5 cm) |
| maksymalna wysokość | 20 cm |
| minimalna czcionka w rysunku | 10 pt |
| rozdzielczość rastra | 300 DPI |
| PNG przy 15,24 cm szerokości | 1800 px |
| proporcja docelowa | 4:3 do 1:1,3 (szersze niż 2:1 wymaga przebudowy układu, nie skalowania) |

Artykuł do czasopisma ma limity ostrzejsze i różne między wydawcami (czcionka
bywa 6–7 pt, łam pojedynczy 8,4–9 cm) — sprawdzaj instrukcje konkretnego pisma,
w razie braku danych przyjmij najostrzejszy wariant ze znanych ci wydawców.

## Format pliku

Wektor (PDF, EPS, SVG) dla wszystkiego, co jest kreską: schematy, wykresy,
diagramy. Skaluje się bez utraty jakości, brak problemu z DPI. Raster (PNG,
TIFF) tylko dla zdjęć i zrzutów ekranu. Nigdy nie „podnoś jakości" rastra do
wektora — to nie działa, tylko powiększa plik. Gdy łańcuch eksportu wymaga
rastra, generuj PNG w 300 DPI **z pliku wektorowego**, nie ze zrzutu ekranu.

## Kolor — nie może być jedynym nośnikiem informacji

Około 8% mężczyzn ma zaburzenia rozpoznawania barw, a praca bywa drukowana
czarno-biało. Rozróżnienie musi działać także przez kształt znacznika, rodzaj
linii (ciągła/przerywana/kropkowana) albo etykietę.

Paleta bezpieczna dla daltonistów (Wong, *Nature Methods* 2011):

```
#000000 czarny   #E69F00 pomarańczowy   #56B4E9 błękitny   #009E73 zielony morski
#F0E442 żółty    #0072B2 niebieski      #D55E00 ceglasty   #CC79A7 różowy
```

Uwaga: nie wszystkie osiem kolorów mają dość kontrastu na białym tle do użycia
jako **linia albo tekst** (żółty i jasny pomarańcz/błękit poniżej progu WCAG
3:1) — do linii, znaczników i tekstu bezpieczny jest pięcioelementowy podzbiór
`["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#000000"]`; pełna ósemka nadaje
się do wypełnień dużych obszarów, o ile mają ciemną obwódkę. Zawsze warto
zmierzyć kontrast (wzór WCAG: `(L1+0.05)/(L2+0.05)`, L = luminancja względna)
zamiast zakładać, że „kolor z bezpiecznej palety" znaczy „bezpieczny w każdej roli".

Mapy ciepła i skale ciągłe: `viridis` albo `cividis` — percepcyjnie jednorodne,
konwertują się poprawnie do skali szarości. Nigdy `jet`/`rainbow` (tworzą
fałszywe krawędzie w danych) ani domyślnej palety wielu bibliotek do wykresów
bez sprawdzenia (czerwony/zielony bywają nierozróżnialne przy najczęstszej
postaci daltonizmu).

## Pułapka automatycznego przycinania

Opcja automatycznego przycinania rysunku do zawartości (często nazywana „tight"
w bibliotekach do wykresów) **zmienia fizyczny rozmiar pliku** — długa etykieta
legendy rozpycha rysunek poza zadeklarowany rozmiar. Zamiast przycinania po
fakcie, układaj rysunek od razu wewnątrz zadanej ramki (constrained/fixed
layout), nie przycinaj go później.

## Diagramy (Mermaid i podobne)

- Układ pionowy domyślnie; poziomy przy więcej niż czterech elementach w rzędzie
  rozpycha diagram na szerokość i wymusza mikroskopijną czcionkę.
- Diagram wyższy niż limit wysokości dzieli się na dwa rysunki z osobnymi
  numerami albo upraszcza przez usunięcie poziomu szczegółu — nie skaluje się
  „żeby wszedł".
- Krótkie etykiety w węzłach; rozwinięcie idzie do podpisu pod rysunkiem.
- **Źródłem prawdy jest plik tekstowy diagramu, nie wyeksportowany obrazek.**
  Tekst diffuje się w gicie, poprawia się literówkę bez regenerowania od zera i
  renderuje ponownie w dowolnym rozmiarze. Trzymaj plik źródłowy obok rysunku i
  commituj oba.
- Nie każdy schemat to schemat blokowy: chronologia, wymiana komunikatów, model
  danych, cykl życia obiektu i przepływ wielkości mają własne typy diagramów
  dedykowane do tego kształtu danych, nie uniwersalny prostokąt-ze-strzałką.

## Wzory matematyczne

Numeruj, odwołuj się do numeru przed wystąpieniem w tekście, objaśnij każdy
symbol (wzór bez legendy oznaczeń jest gorszy niż jego brak). Sprawdź, czy
łańcuch eksportu faktycznie renderuje matematykę — jeśli w dokumencie
wynikowym widać surowy zapis wzoru zamiast złożonego symbolu, wzór nie został
wyrenderowany i nie wolno tego tak zostawić.

## Bramka przed wstawieniem do pracy

Rysunek z werdyktem FAIL nie wchodzi do pracy — nie skaluje się go „żeby
wszedł", tylko przebudowuje układ. Bramka czyta **realny rozmiar fizyczny
pliku**, nie deklarowany w kodzie generującym, i sprawdza szerokość, wysokość,
proporcję, DPI, obecność kanału przezroczystości i to, czy rzekomy wektor nie
jest w rzeczywistości rastrem wklejonym do kontenera wektorowego.

Nawet po przejściu bramki wymiarowej zostają dwa testy, których nie da się
zautomatyzować:

1. Wydrukuj albo wyświetl rysunek w docelowym rozmiarze i przeczytaj najmniejszą
   etykietę. Musisz mrużyć oczy → jest za mała.
2. Przeczytaj każdą etykietę litera po literze. Literówka w podpisie osi
   przechodzi przez każdą automatyczną kontrolę wymiarów.

## Uczciwe kodowanie danych

Rysunek może spełniać wszystkie limity fizyczne i nadal kłamać:

- Słupki i pola liczone od zera — ucięta oś przy słupkach zawyża różnicę wizualnie.
- Nazwij, co pokazuje wąs błędu (odchylenie standardowe, błąd standardowy,
  przedział ufności, percentyl) i podaj `n`. Wąsy bez definicji nie znaczą nic.
- Odróżnij brak danych od zera — nie łącz linią punktów przez lukę w pomiarach.
- Skaluj pole, nie promień — podwojenie promienia daje poczwórne pole i
  poczwórne wrażenie wizualne. Trójwymiarowe słupki „dla efektu" — nigdy.
- Panele porównawcze mają identyczne zakresy osi, inaczej porównanie jest
  trikiem wizualnym.

## Edycja istniejącej grafiki — nigdy nie twórz od nowa

Każda ilustracja ma zapisane źródło (plik diagramu albo funkcję generującą
wykres). Zmiana grafiki to edycja tego źródła i ponowny render **tego jednego
pliku**, nie generowanie od zera i nie przebudowa wszystkich rysunków naraz.

Procedura: znajdź źródło (grep po nazwie pliku wynikowego w skryptach/
diagramach) → zmień w źródle wyłącznie to, co trzeba → wyrenderuj tylko ten
plik → sprawdź wymiary bramką → obejrzyj wynik (render bez obejrzenia nie jest
skończoną edycją).

Terminologia na grafice musi zgadzać się z terminologią tekstu. Gdy tekst
zmienia termin, grafiki **nie aktualizują się same** — trzeba przeszukać
wszystkie źródła diagramów i wykresów pod kątem starego terminu i poprawić
każde trafienie. Zapomniany termin na wyrenderowanym obrazku wykrywa dopiero
wzrokowy audyt, nie żaden automat tekstowy.

## Interpretacja gotowego rysunku — jak czytać PNG/PDF wynikowy

Ocena istniejącej grafiki wymaga jej **obejrzenia**, nie tylko odczytania
metadanych pliku. Kolejność sprawdzania: (1) czy tekst na grafice zgadza się
z terminologią tekstu, (2) czy etykiety nie są ucięte albo nachodzące na
siebie (częsty defekt: tytuły ramek w diagramach przy zbyt małym marginesie),
(3) czy liczby na grafice zgadzają się z liczbami w tekście obok — rozjazd to
albo błąd, albo brakujące zdanie tłumaczące różnicę metodyki pomiaru, (4) czy
znaki diakrytyczne wyrenderowały się poprawnie. Werdykt o grafice bez jej
realnego obejrzenia jest niewiarygodny.
