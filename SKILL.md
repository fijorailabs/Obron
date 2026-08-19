---
name: obron
description: >
  Kompletny proces pisania i obrony pracy naukowej z agentami AI — od pomysłu, przez
  problem badawczy, metodykę, badanie, rozdziały, redakcję i bramki jakości, aż po skład,
  arkusz zmian dla promotora i obronę. Trzynaście faz (0–12), osiem ról, pięć bramek. Wywołuj
  GDY: zaczynasz pracę licencjacką, inżynierską, magisterską, doktorat albo artykuł
  naukowy; szukasz tematu i problemu badawczego; piszesz protokół metodyki przed badaniem;
  piszesz albo poprawiasz rozdział; dostałeś uwagi promotora lub recenzenta do wdrożenia;
  robisz przegląd literatury i boisz się zmyślonych źródeł; szykujesz skład docx/PDF;
  budujesz arkusz Było→Jest dla promotora; przygotowujesz się do obrony; albo scalasz
  pracę wielu równoległych agentów i boisz się utraty treści przy mergu.
---

# Napisz i obroń pracę naukową

Metodyka wypracowana na realnej pracy dyplomowej pisanej z pomocą agentów AI, spisana
po to, żeby autor mógł zająć się **badaniem**, a nie opisywaniem badania.

Punkt wyjścia jest niewygodny: agent AI pisze i poprawia szybko, ale szybko też **psuje
po cichu**. Kasuje cudzą pracę przy scalaniu. Skleja słowa przy masowej podmianie.
Zostawia sygnały tekstu maszynowego. Cytuje źródła, których nie ma. Myli plik źródłowy
ze złożonym dokumentem. Żadna z tych usterek nie boli od razu — boli dopiero wtedy, gdy
znajdzie ją promotor albo recenzent.

Stąd cała metodyka: **bramka jakości PRZED, nie audyt PO.**

Zasada nadrzędna, która wraca w każdej fazie: **agent proponuje, niezależna kontrola
ocenia, zmiana wchodzi tylko z PASS.** Nigdy odwrotnie.

---

## Mapa procesu

```
 0  ZWIADOWCA     typ pracy, wymogi uczelni, kalendarz terminów
 1  ARCHITEKT     temat → problem → cele → hipotezy → spis treści
    ⛔ BRAMKA PLANU
 2  METODOLOG     protokół metodyki, prespecyfikacja
    ⛔ BRAMKA METODYKI          ← najtańsza kontrola w całym projekcie
 3  BIBLIOTEKARZ  kwerenda, rejestr zweryfikowanych źródeł
 4  BADACZ        wykonanie badania, dane, wyniki surowe
 5  COPYWRITER    rozdziały wg planu: metodyka → wyniki → dyskusja → teoria
 6  ILUSTRATOR    rysunki, tabele, wzory
    ⛔ BRAMKA GRAFIKI
 7  RECENZENT     recenzja wewnętrzna: stan dokumentu, nie zmiany w nim
 8  REDAKTOR      poprawki zdaniowe pod uwagi
    ⛔ BRAMKA ZDANIOWA          ← trzej niezależni sędziowie
 9  WSTĘPNIARZ    wstęp, zakończenie, streszczenie, tytuł — DOPIERO TERAZ
    ⛔ BRAMKA JAKOŚCI           ← zbiorcza, wpięta przed skład
10  SKŁADACZ      md → docx → PDF; typografia wyłącznie tutaj
11  ROZLICZENIOWY arkusz Było→Jest dla promotora
12  OBROŃCA       prezentacja, pytania komisji, próba generalna
```

Fazy 5–8 chodzą w pętli, rozdział po rozdziale. Reszta jest liniowa.

Definicje ról: `agenci/`. Wiedza dziedzinowa: `referencje/`. Skrypty: `szablony/`.

---

## Faza 0 — zwiadowca

Zanim padnie pierwsze zdanie planu, ustal trzy rzeczy i zapisz je:

1. **Typ pracy.** Licencjacka, inżynierska, magisterska, doktorat, artykuł. Empiryczna,
   przeglądowa, projektowo-wdrożeniowa, teoretyczna, studium przypadku, porównawcza.
   Każdy typ ma inny szkielet rozdziałów i inne sedno oceny → `referencje/typy-prac.md`.
   ⛔ Typ zadeklaruj we wstępie pracy — bywa, że recenzent ocenia inną kolumną formularza.

2. **Wymogi własnej uczelni**, odczytane z dokumentów, nie z pamięci ani z internetu.
   Znajdź i przeczytaj: regulamin studiów, procedurę dyplomowania, „zasady pisania prac
   dyplomowych" swojego wydziału oraz zarządzenie rektora o narzędziach AI, jeśli istnieje.
   Ustawa mówi o pracy dyplomowej zaskakująco mało — prawie wszystko, co student uważa za
   wymóg, jest aktem wewnętrznym uczelni i **różni się między uczelniami**.

3. **Kalendarz od końca.** Data obrony → termin złożenia → termin oddania promotorowi →
   czas na jego uwagi i dwie tury poprawek → termin zamknięcia badania. Licz wstecz,
   nie wprzód.

Czego nie da się rozstrzygnąć z dokumentów, zapisz jako **pytania do dziekanatu** i wyślij.
Zgadywanie wymogu formalnego kosztuje później przebudowę składu.

---

## Faza 1 — architekt: plan pracy

→ `agenci/architekt.md`

Trzy warianty tematu (ambitny, rekomendowany, bezpieczny), łańcuch cel → pytanie →
hipoteza → metoda → rozdział, katalog odrzuceń z powodami, spis treści z przypisaniem
hipotez do rozdziałów.

### ⛔ Bramka planu

- każda hipoteza ma kierunek, warunek ceteris paribus, definicję operacyjną i **jednostkę
  analizy**
- umiesz powiedzieć, jaki wynik obala każdą hipotezę
- tabela cel → pytanie → hipoteza → metoda → rozdział nie ma pustych pól
- wariant bezpieczny zapisany z warunkiem uruchomienia
- plan mieści się w czasie liczonym od realnej daty

Plan zatwierdza **człowiek i promotor**. To najtańszy moment na zmianę kierunku.

**Szkielet struktury domyślnie to IMRaD.** Gdy użytkownik prosi o strukturę/spis treści
artykułu naukowego od zera, stosuj IMRaD jako punkt wyjścia — szczegóły (model CARS,
proporcje, kiedy IMRaD nie wystarcza) w `referencje/struktura-i-kolejnosc.md`. Wyjątki
wg typu pracy → `referencje/typy-prac.md`.

---

## Faza 2 — metodolog: protokół przed badaniem

→ `agenci/metodolog.md`

**Zmiana metodyki po starcie badania unieważnia pomiary.** Protokół powstaje przed
badaniem, przechodzi audyt adwersarski i zostaje zamrożony zapisem zmian, którego skrót
trafia do tekstu pracy.

### ⛔ Bramka metodyki

Najtańsza kontrola w całym projekcie. Błąd znaleziony tutaj kosztuje przeredagowanie
akapitu; ten sam błąd po zebraniu danych kosztuje całe badanie.

- okno kalibracji materiału ustalone (czy badanie w ogóle jest w stanie wykryć różnicę)
- podłoga i sufit wykonalności wykluczone
- kontaminacja materiału wykluczona albo zaadresowana
- jednostka analizy nazwana wprost i zgodna z hipotezami
- plan analizy kompletny: testy, poprawki na wielokrotne porównania, progi, obsługa braków
- **policzona najmniejsza możliwa wartość p przy planowanym n** — wynik poniżej tej
  podłogi zawsze oznacza błąd implementacji, nie odkrycie
- dziesięć elementów odtwarzalności ma przypisane miejsce w pracy
- wynik negatywny zadeklarowany na piśmie jako pełnoprawny
- zagrożenia trafności spisane, przed pomiarem
- sekcja o danych osobowych i etyce napisana albo jawnie uznana za niedotyczącą

Dopóki ta lista nie jest zamknięta, badanie się nie zaczyna.

---

## Faza 3 — bibliotekarz: rejestr źródeł

→ `agenci/bibliotekarz.md`

Dwa pliki: mapa literatury (co czytamy gdzie i po co) oraz rejestr źródeł — **jedyne
źródło cytowań dla całej pracy**.

⛔ **Styl cytowania ustalasz teraz, nie później.** Zmiana stylu w połowie pracy oznacza
przerobienie każdego odwołania w każdym rozdziale. Jeśli regulamin uczelni mówi co innego
niż promotor, ustalenie z promotorem potwierdź mailem, zanim cokolwiek zmienisz.

⛔ **Weryfikujesz pokrycie twierdzenia, nie istnienie rekordu.** Najgroźniejsza klasa
halucynacji to źródło, które istnieje, ale mówi co innego — przechodzi każdą kontrolę
istnienia.

Copywriter cytuje wyłącznie z rejestru. Brakujące źródło zostawia jako jawny dług
`[ŹRÓDŁO?]`, nigdy jako przypis z pamięci.

---

## Faza 4 — badacz: wykonanie

Badanie realizuje zamrożony protokół. Wszystko, co odbiega od protokołu, jest odnotowywane
w momencie odstępstwa, nie odtwarzane z pamięci na końcu.

Produkt tej fazy poza danymi: **plik ustaleń faktograficznych** — osobne źródło prawdy,
oddzielone od rozdziałów, gdzie każdy wpis ma dowód w postaci pliku i numeru linii albo
rekordu w danych.

> Ustalenia wynikają z kodu i danych, nie z tego, co praca o sobie twierdzi.
> Zdanie w pracy sprzeczne z tym plikiem jest błędem faktycznym, nie stylistycznym.

W realnym projekcie ten plik ujawnił, że praca opisywała procedurę wziętą z generatora
danych demonstracyjnych, a nie z eksperymentu.

---

## Faza 5 — copywriter: rozdziały

→ `agenci/copywriter.md`, `referencje/styl-polski.md`, `referencje/struktura-i-kolejnosc.md`

**Kolejność pisania nie jest kolejnością w spisie treści:**

```
ryciny i tabele → metodyka → wyniki → dyskusja → teoria i przegląd → WSTĘP → zakończenie
→ streszczenie → tytuł
```

Trzy zakazy, od których zaczyna każdy piszący agent: nie cytuje spoza rejestru, nie zmyśla
liczb, nie wpisuje znaku `—`.

Struktura pracy jest jedna: **jedno źródło prawdy per rozdział, format Markdown, jeden
plik = jeden rozdział.** Markdown jest jedyną edytowalną warstwą. Diffuje się w gicie,
czyta bez narzędzi, nie wymaga otwierania dokumentu wynikowego, żeby poprawić literówkę.

Obowiązkowe artefakty towarzyszące: **słownik pojęć** (nie dodatek, tylko element pracy)
i **rejestr decyzji terminologicznych**, w tym decyzji zamkniętych. Bez rejestru druga
fala poprawek cofa decyzje pierwszej.

⛔ **Ujednolicenie terminologii idzie przed redakcją zdaniową.** Termin występujący
w pracy więcej niż raz nie jest sprawą zdania — spolszczenie w jednym miejscu tworzy dwie
wersje i stan gorszy niż przed poprawką. Na tym wywróciły się trzy niezależne zespoły.

---

## Faza 6 — ilustrator

→ `referencje/grafika.md`

**Rysunek ocenia się w docelowym rozmiarze na stronie, nigdy na monitorze.** Zanim
cokolwiek narysujesz, policz trzy liczby: szerokość obszaru tekstu, dostępną wysokość
i minimalną czcionkę.

⛔ **Diagramu wyników nie generuje się generatorem obrazów.** Ładny obrazek ze zmyślonymi
słupkami jest w pracy naukowej gorszy niż brak rysunku. Wyniki rysuje biblioteka
wykreślająca na realnych danych, schematy powstają z tekstowego źródła diagramu, wzory
składa się jako matematykę.

### ⛔ Bramka grafiki

Bramka czyta **realny rozmiar fizyczny pliku**, nie deklarowany w kodzie generującym:
szerokość, wysokość, proporcja, rozdzielczość, przezroczystość, i czy rzekomy wektor nie
jest rastrem w kontenerze wektorowym. Rysunek z werdyktem FAIL nie wchodzi do pracy —
nie skaluje się go „żeby wszedł", tylko przebudowuje układ.

Po bramce zostają dwa testy, których nie da się zautomatyzować: obejrzenie rysunku
w docelowym rozmiarze i przeczytanie każdej etykiety litera po literze.

---

## Faza 7 — recenzent wewnętrzny

→ `agenci/recenzent.md`

⛔ **Recenzent ocenia STAN DOKUMENTU, bramka zdaniowa ocenia ZMIANY.** To rozróżnienie
unieważnia większość automatycznych kontroli jakości, jeśli się je pomyli.

Rozdział, w którym poprawiono trzydzieści sześć zdań i wszystkie trzydzieści sześć
przeszło bramkę, może nadal zawierać sto dziesięć wad w zdaniach, których nikt nie tknął.
Obie oceny były prawdziwe. Żadna nie odpowiadała na pytanie, czy praca jest gotowa.

Przy całej pracy audyt rozbija się na wąskie, rozłączne zakresy z limitem objętości
raportu, a **naprawy wykonuje się przed odpaleniem syntezy** — inaczej synteza ocenia stan,
którego już nie ma.

⛔ Audyt nie jest monotoniczny: fala napraw sama wprowadza regresje, najczęściej
w rozdziałach edytowanych najczęściej. Wzrost liczby zarzutów między przebiegami to
informacja, nie porażka narzędzia.

---

## Faza 8 — redaktor i bramka zdaniowa

→ `agenci/redaktor.md`, `agenci/sedzia.md`, `referencje/kategorie.md`

To jest serce metodyki. Jeden agent-redaktor NIE wystarcza: model, który napisał poprawkę,
jest najgorszym sędzią własnej poprawki, bo nie widzi błędów kontekstowych — właśnie
z tego kontekstu wyszedł.

### Pipeline

```
1. WYKRYCIE     skrypt znajduje kandydatów regexem (podpowiedź, nie wyrok)
2. KWALIFIKACJA redaktor ocenia KAŻDE zdanie akapitu, także bez trafienia mechanicznego
3. REDAKCJA     przepisuje tylko zdania wadliwe, z kontekstem całego akapitu,
                kwalifikuje każdą zmianę do kategorii
4. BRAMKA       TRZEJ NIEZALEŻNI SĘDZIOWIE, wywołani RÓWNOLEGLE, każdy inna rubryka:
                  • ZDANIE   — czy samo zdanie jest teraz poprawne
                  • KONTEKST — czy pasuje do sąsiadów, nie tworzy sprzeczności
                  • UWAGI    — czy realizuje DOKŁADNIE tę uwagę, którą miało realizować
5. SCALENIE     werdykty zbierane per zdanie; brak werdyktu liczy się jak FAIL
6. ZASTOSOWANIE do pliku wchodzi WYŁĄCZNIE komplet PASS (albo PASS_Z_ZALEŻNOŚCIĄ)
7. CHANGELOG    dopisywany automatycznie, dopiero gdy w przebiegu nie ma żadnego FAIL
```

**Jednostką pracy jest akapit, jednostką zmiany jest zdanie.** Redaktor dostaje cały
akapit jako kontekst, ale wolno mu ruszyć wyłącznie wskazane zdania i musi rozliczyć się
z każdego. Zdanie pominięte milczeniem to błąd.

**Dlaczego trzy rubryki.** Sędzia oceniający tylko zdanie przepuści zdanie poprawne
w izolacji, a sprzeczne z akapitem. Sędzia oceniający tylko kontekst przepuści zdanie
ładnie wklejone, które nie realizuje uwagi, po którą powstało. Rubryka UWAGI istnieje po
to, żeby złapać naprawę jednej uwagi kosztem złamania innej — najczęstszy błąd wtórny
całej metodyki to rozbicie za długiego zdania przez wstawienie dwukropka dokańczającego
myśl.

**Werdykt wiąże się z treścią, nie z identyfikatorem.** Każdy PASS niesie skrót
kryptograficzny zaakceptowanego zdania. Bez tego w pętli poprawkowej stary PASS pasuje do
nowej wersji zdania, której żaden sędzia nie widział.

**Reguła dwóch pętli.** Zdanie, które nie przeszło bramki dwa razy z rzędu, nie idzie do
trzeciej automatycznej pętli — trafia na listę do decyzji człowieka.

**Bezpiecznik warstwy.** Zarzut dotyczący warstwy szerszej niż zdanie i akapit nie jest
podstawą do FAIL. Bez tego bezpiecznika pętla bywa nieskończona z konstrukcji: redaktor
spolszcza termin w jednym zdaniu, sędzia sprawdza spójność grepem po całej pracy, a przy
dwustu siedemdziesięciu wystąpieniach każda próba musi dostać FAIL.

**Zakres tury zamknięty na piśmie.** „Zakres ZAMKNIĘTY — wyłącznie pozycje z tej listy",
z twardymi regułami: zero myślników, zero zmiany liczb, zdanie poniżej 35 słów. Bez tego
redaktor „ulepsza przy okazji" i tura poprawek przestaje być rozliczalna.

### Reguła idempotentności podmian masowych

Podmiana uruchomiona na całej pracy musi dać ten sam wynik puszczona raz i dwa razy.

Klasyczny mechanizm awarii: naprawa zgody rodzaju zamienia „zrobił" na „zrobiła". Druga,
niezależna poprawka wykonuje później `tekst.replace("zrobił", "zrobiła")` na tekście,
który **już zawiera** „zrobiła" — a „zrobił" jest podciągiem „zrobiła", więc powstaje
„zrobiłaa". Błąd przechodzi każdy test typu „skrypt się wykonał bez wyjątku" i wychodzi
dopiero przy czytaniu treści. W realnym projekcie dotarł do streszczenia rozdziału.

1. `str.replace` na urywku słowa jest zakazany. Zawsze `re.sub` z granicą słowa `\b`.
2. Po każdej podmianie uruchom skrypt drugi raz i porównaj wynik — różnica oznacza brak
   idempotentności.
3. Przegrepuj ślady sklejenia, np. `\w+(aa|ąą|ęę|ćć)\b`.
4. **Wynik ocenia się po treści, czytając diff — nigdy po tym, że skrypt zwrócił kod 0.**

Obowiązkowy test niezależny od narzędzia: porównaj **listę wszystkich tokenów** przed i po,
sprawdź, że każda różnica pasuje do dozwolonego wzorca, i że nie powstały nowe artefakty.

---

## Faza 9 — wstęp, zakończenie, streszczenie

→ `referencje/struktura-i-kolejnosc.md`

Dopiero teraz. Wstęp opisuje pracę, która już istnieje; napisany pierwszy zawsze obiecuje
więcej, niż praca dowozi.

Wstęp buduje się na trzech ruchach: terytorium → luka → zajęcie luki. Sygnałem
gramatycznym luki jest spójnik przeciwstawny albo przeczenie; wstęp bez takiego sygnału
nie uzasadnia, po co ta praca powstała. **Zakres celu musi równać się zakresowi luki.**

⛔ Wstęp i zakończenie pisze się i poprawia **razem**, jednym przebiegiem. Cel zapowiedziany
bez rozliczenia i wniosek bez zapowiedzianego celu to ta sama usterka widziana z dwóch
stron.

⛔ Sprawdź osobno, czy wnioski nadal wynikają z wyników. Po turach poprawek, w których
osłabiono twierdzenia w rozdziale wyników, zakończenie zwykle zostaje nieruszone.

### ⛔ Bramka jakości — wszystko jedną komendą, przed składem

Wniosek z audytu incydentów tej metodyki: **każdy** incydent miał w danym momencie już
istniejącą kontrolę, która by go wykrył — tylko kontrole były rozproszone po osobnych
skryptach odpalanych ręcznie, kiedy ktoś sobie o nich przypomniał.

Bramka agreguje je w jeden przebieg i **wpina się przed skład**: dokument z błędami
fizycznie nie ma prawa powstać, bo skrypt eksportu przerywa się przy FAIL.

| Kategoria | Co łapie |
|---|---|
| konflikty git | znaczniki `<<<<<<<` po nieudanym scaleniu |
| sklejenia po podmianach | ślady typu „zrobiłaa" |
| otwarte długi | pozostałe znaczniki `[ŹRÓDŁO?]` |
| anglicyzmy | terminy z zamkniętej listy wracające lokalnie |
| zgoda gramatyczna | rodzaj i przypadek wokół podmienionych fraz |
| spójność liczb | ta sama wielkość w dwóch rozdziałach |
| cytowania w obu kierunkach | numer bez pozycji ORAZ pozycja nigdy nieprzywołana |
| ciągłość numeracji rysunków | luka w numeracji i znacznik bez pliku na dysku |
| liczba wzorów nie spada | licznik z progiem minimalnym, łapie regresję przy scalaniu |
| wymiary ilustracji | delegacja do bramki grafiki |
| objętość | liczba stron złożonego dokumentu wobec limitu uczelni |

Szkielet: `szablony/bramka.py`. Dwa tryby: pełny i szybki (bez najwolniejszej kontroli
wymiarów), do użycia w pętli redakcyjnej.

⛔ **Bramka tylko ostrzega, nigdy nie przepisuje tekstu autora.** Automatyczna naprawa
w walidatorze łamała zdania po skrótach i psuła zaakceptowany tekst przy każdej drobnej
zmianie.

⛔ **Wszystkie pomiary i audyty wykonuj na tekście PO transformacji eksportu**, nie na
surowym źródle. To jest to, co faktycznie zobaczy promotor, a niektóre kategorie są
celowo obecne w źródle i usuwane dopiero w składzie.

---

## Faza 10 — skład: separacja treści od typografii

**Zasada twarda: źródło nigdy nie zawiera decyzji typograficznych.** Twarde spacje po
jednoliterowych spójnikach, zdjęcie pozostałych myślników, styl akapitu, spis treści,
strona tytułowa — wszystko to powstaje wyłącznie w warstwie eksportu.

Powód jest praktyczny, nie estetyczny: poprawianie typografii wprost w źródle przez
agentów kosztowało dziesiątki zbędnych wywołań modelu i spowodowało kilka regresji przy
scalaniu równoległych gałęzi. Reguła kontekstowa w eksporcie robi to samo zero-tokenowo,
deterministycznie i powtarzalnie przy każdym składaniu.

```
źródła .md (jedyne edytowalne)
   → transformacja (utnij notatki robocze, komentarze, wstaw obrazy)
   → warstwa typograficzna (twarde spacje, zdjęcie myślników)
   → ⛔ BRAMKA JAKOŚCI — PRZERWIJ przy FAIL
   → skład na szablonie referencyjnym (justowanie, wcięcia, style, tabele)
   → PDF przez konwerter z makrem aktualizującym pola
```

Trzy realne miejsca awarii, na które trzeba uważać:

- **pusty spis treści w PDF** — zwykła konwersja nie odświeża pól; potrzebne makro
  aktualizujące indeksy,
- **pusty spis w surowym pliku docx to nie błąd** — pole jest oznaczone jako wymagające
  odświeżenia i edytor wypełnia je przy otwarciu,
- **kolizje numeracji przypisów między rozdziałami** przy scalaniu plików — prefiksowanie
  per rozdział.

**Szablon referencyjny generuj skryptem, nie klikaj.** Wtedy jest odtwarzalny jedną
komendą i nie musi żyć w repozytorium.

⛔ Pliki wynikowe są **zawsze generowane, nigdy edytowane ręcznie.** Ręczna edytka w docx
to fałszywe źródło prawdy — następny eksport ją nadpisze i praca zniknie bez ostrzeżenia.

---

## Faza 11 — arkusz zmian dla promotora

Promotor nie czyta diffu gita. Potrzebuje tabeli: co się zmieniło, gdzie i dlaczego,
w formie, którą przegląda w pięć minut.

**Arkusz jest generatorem, nie plikiem.** Powstaje ze stanu repozytorium przy każdym
uruchomieniu, a pliki robocze zostają nietknięte.

1. **Diff liczony od wersji, którą recenzent faktycznie czytał** — nie od ostatniego
   commitu i nie łańcuchem przez wersje pośrednie. Recenzent widział konkretny dokument
   w konkretnym dniu; arkusz porównuje się do TEGO stanu, odtworzonego datą commita.
2. **Każda zmiana jako para Było→Jest z realnym cytatem.** Wiersz bez cytatu jest
   bezwartościowy — recenzent i tak musi otworzyć dokument.
3. **Numer strony z realnego złożonego PDF**, nie z szacowania po znakach. Rozkład stron
   w arkuszu jest zarazem testem jego poprawności: wszystkie zmiany na stronach 4–7
   oznaczają, że generator złapał tylko początek pracy.
4. **Kolumna na komentarz recenzenta**, pusta.
5. **Zmiany masowe w osobnej zakładce**, nie wymieszane ze zmianami merytorycznymi —
   inaczej ten sam wzorzec powtórzony kilkaset razy zasypuje to, co ważne.
6. **Zakładka ilustracji z linkami** do plików źródłowych każdego rysunku.

Trzy zarzuty, przez które pierwsza wersja takiego arkusza została odrzucona: wiersze bez
cytatu, łańcuchowanie przez wersje pośrednie, zaśmiecenie wzorcem masowym.

---

## Faza 12 — obrona

→ `agenci/obronca.md`

Osiem do dziesięciu minut, cztery bloki, jeden slajd na jedną myśl, wyniki na wykresach.
Trzy pytania padają prawie zawsze: stałe pytanie promotora z jego przedmiotu, pytanie
recenzenta z jego obszaru, pytanie o metodykę albo wnioski.

⛔ **Przygotowanie do obrony zaczynasz przed złożeniem pracy.** Próba generalna
z adwersarzem prawie zawsze wskazuje miejsca warte poprawienia w tekście — a po złożeniu
już się ich nie poprawi.

Pytanie, które pojawia się coraz częściej: „proszę wyjaśnić ten fragment własnymi
słowami". Nie da się na nie przygotować odpowiedzi. Da się przygotować tylko jedno:
**zdanie, którego autor nie umie wytłumaczyć, nie powinno w pracy zostać.**

---

## Praca równoległa i kontrola integralności

Gdy więcej niż jeden agent pracuje na tej samej pracy (osobne worktree per rozdział albo
per zadanie), scalanie gałęzi jest największym pojedynczym źródłem cichej utraty pracy.
Git nie zgłasza konfliktu tam, gdzie drugi agent w ogóle nie dotknął pliku — więc jeśli
agent zaczyna od nieaktualnego stanu, jego diff **cofa** cudzą pracę i nikt tego nie
widzi, dopóki ktoś nie policzy.

1. **Przed rozpoczęciem pracy** policz liczniki, które mogą tylko rosnąć (rysunki,
   nagłówki, unikalne cytowania, tabele, wzory) oraz te, które mogą tylko maleć
   (anglicyzmy z zamkniętej listy, pozostałe myślniki, otwarte długi źródeł). Zapisz
   migawkę.
2. **Zanim cokolwiek dotkniesz w worktree**, zmerguj aktualny stan głównej gałęzi.
3. **Po skończonej pracy** policz ponownie. Licznik rosnący spadł → coś zniknęło. Licznik
   malejący wzrósł → wróciła rzecz już naprawiona. Żaden z tych wyników nie jest
   drobiazgiem do poprawienia później — to błąd krytyczny wstrzymujący zgłoszenie
   gotowości.
4. **Po ostatecznym scaleniu** przegrepuj całe drzewo po znacznikach konfliktu.

Mierz liczniki **na tekście po transformacji eksportu**. Szkielet:
`szablony/kontrola_integralnosci.py`.

⛔ **Changelog musi dopisywać, nie nadpisywać, i musi uruchamiać się sam.** Instrukcja
„teraz uruchom changelog" wypisywana przez skrypt spowodowała, że 375 zmian weszło do
pracy bez śladu. Osobno: nadpisywanie zamiast dopisywania zjadło 606 wpisów, odzyskanych
potem z historii gita.

---

## Lekcje z incydentów

### (a) Regresje przy scalaniu gałęzi

Pięć zespołów agentów pracujących równolegle o mało nie skasowało sobie nawzajem pracy:
przeliczona oś danych zniknęła w jednym rozdziale, dwa wpięte rysunki w innym, dwanaście
odwołań cytowań w trzecim. Nikt tego nie zauważył, bo git nie zgłasza konfliktu tam, gdzie
tylko jeden agent dotknął pliku. **Sam test „zmergowało się bez konfliktu" nie dowodzi
niczego** — brak konfliktu i utrata treści to dwa różne zdarzenia.

### (b) `replace` bez granicy słowa

Opisane w Fazie 8. Błąd przeszedł cały pipeline aż do złożonego dokumentu i wyłapał go
dopiero zewnętrzny audyt.

### (c) Zewnętrzny audyt AI myli źródło ze składem

Model odpalony jako audytor ocenił dokument PO transformacji eksportu i zgłosił fałszywy
zarzut wobec fragmentu, który w źródle wyglądał inaczej. Pomylił efekt warstwy składu
z błędem treści.

Z dwudziestu zarzutów tego audytu realne były cztery. **Ale to właśnie ten audyt wychwycił
największe przeoczenie całego projektu** — brak zamówionego przez promotora słownika pojęć.
Wniosek nie brzmi „nie ufaj audytom", tylko: **każdy zarzut audytu weryfikuj w plikach,
zanim go poprawisz.** „Niezależny" nie znaczy „nieomylny", tylko „inny punkt startu".

### (d) Zatruty prompt orkiestratora

Fałszywy fakt w prompcie orkiestratora zatruł dziewięciu agentów naraz i wszedł jako
ozdobnik do pięciu gotowych tekstów. **Prompt wymaga audytu źródłowego dokładnie tak samo
jak wygenerowany tekst.** Stąd obowiązkowa sekcja „fakty użyte + źródła" w każdym oddaniu
pracy przez agenta.

### (e) Rozbieżność pomiaru z audytem rozstrzyga się w plikach

Pomiar po zamkniętej liście wzorców dawał zero anglicyzmów, pomiar szeroki dawał sto
dziewiętnaście, z czego osiemdziesiąt dwa to jedno słowo. Oba były technicznie poprawne
i oba mierzyły co innego. Rozbieżność między własnym pomiarem a audytem jest sygnałem, że
**własny pomiar może być za wąski** — nie dowodem, że audyt się myli.

### (f) „Skrypt się wykonał" ≠ „wynik jest poprawny"

Powracający wzorzec w całej metodyce: kod wyjścia zero traktowany jako dowód sukcesu,
podczas gdy jedynym dowodem sukcesu jest przeczytanie treści wynikowej. Bramki
automatyczne łapią kategorie błędów dające się sformalizować regułą. Nie łapią wszystkiego
— literówka w etykiecie osi, przekręcony sens zdania i źle dobrany typ wykresu przechodzą
przez każdą automatyczną kontrolę.

**Żadna praca nie jest gotowa bez ludzkiego przeczytania wyniku.** Bramki są warunkiem
koniecznym, nie wystarczającym.

### (g) Tempo pracy z agentami wygląda maszynowo — zadeklaruj to wprost

Praca poprawiana przez wiele agentów naraz zmienia się w tempie i wzorcu, którego człowiek
pracujący samodzielnie by nie osiągnął. To samo w sobie nie jest problemem, jeśli autor
faktycznie kieruje procesem i weryfikuje wynik — ale ukrywanie tego jest ryzykowne, bo
wzorzec jest rozpoznawalny.

**Jawna deklaracja użycia AI**, zgodna z tym, do czego zobowiązuje uczelnia albo
wydawnictwo. Nie jako przeprosiny, tylko jako fakt metodologiczny na równi z opisem innych
narzędzi użytych w badaniu. Miejsce deklaracji zależy od zakresu użycia: pomoc językowa
zwykle do podziękowań, udział w analizie danych, kodzie albo grafikach — do metodyki.

---

## Pliki w tym skillu

| Ścieżka | Zawartość |
|---|---|
| `agenci/architekt.md` | faza 1: temat, problem, hipotezy, spis treści |
| `agenci/metodolog.md` | faza 2: protokół, prespecyfikacja, statystyka, ograniczenia |
| `agenci/bibliotekarz.md` | faza 3: kwerenda, weryfikacja źródeł, antyplagiat |
| `agenci/copywriter.md` | faza 5: pisanie rozdziału |
| `agenci/redaktor.md` | faza 8: poprawki zdaniowe pod uwagi |
| `agenci/sedzia.md` | bramka zdaniowa, trzy rubryki |
| `agenci/recenzent.md` | faza 7: recenzja wewnętrzna stanu dokumentu |
| `agenci/obronca.md` | faza 12: prezentacja i pytania komisji |
| `referencje/kategorie.md` | katalog kategorii uwag: kod, definicja, warstwa, naprawa |
| `referencje/styl-polski.md` | jak pisać zdania, pary ZŁE→DOBRE, anglicyzmy, typografia |
| `referencje/struktura-i-kolejnosc.md` | IMRaD, model CARS, dyskusja, proporcje, kolejność |
| `referencje/typy-prac.md` | typologia prac w polskich realiach, szkielety, wymogi |
| `referencje/grafika.md` | limity, formaty, kolor, uczciwe kodowanie danych, bramka |
| `szablony/bramka.py` | zbiorcza bramka jakości |
| `szablony/kontrola_integralnosci.py` | migawka i porównanie liczników |
| `szablony/wykryj.py` | deterministyczny detektor wad zdania, wejście pipeline'u |
| `szablony/myslniki.py` | zdejmowanie znaku pauzy w warstwie eksportu |
| `szablony/renumeracja_bibliografii.py` | numeracja wg pierwszego wystąpienia |

Szablony są **szkieletami do dostosowania**, nie gotowcami: ścieżki, listy rozdziałów,
wzorce błędów i progi są przykładowe.
