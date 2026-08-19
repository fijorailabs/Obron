# Katalog kategorii uwag — wspólny język redaktora, sędziów i skryptów

Uwaga promotora brzmi „za dużo anglicyzmów". Uwaga recenzenta brzmi „język zbyt
popularnonaukowy". Dopóki nie mają kodu i definicji, każdy agent interpretuje je po
swojemu i poprawki się rozjeżdżają: jeden usuwa anglicyzm w zdaniu, drugi zostawia go
w sąsiednim, trzeci wprowadza z powrotem przy okazji innej poprawki.

**Kategoria to kod, definicja, warstwa i instrukcja „jak poprawiasz".** Wszystkie cztery
elementy są obowiązkowe. Kategoria bez instrukcji naprawy jest tylko narzekaniem.

## Jak się tego używa

- Kod nigdy nie występuje sam. W komunikacji z człowiekiem zawsze z nazwą: „myślnik
  w tekście (A1)", nie samo „A1".
- Zdanie może mieć kilka kategorii naraz i zwykle ma.
- **Warstwa** decyduje, kto i kiedy poprawia. To najważniejsza kolumna w tym katalogu —
  ignorowanie jej produkuje nieskończone pętle poprawkowe (patrz `bezpiecznik warstwy`
  w `agenci/sedzia.md`).
- Ten plik jest jedynym źródłem prawdy o kategoriach dla redaktora, sędziów i skryptów.
  Definicja żyje w pliku, nie w głowie agenta.

## Warstwy

| Warstwa | Znaczenie |
|---|---|
| `zdanie` | poprawiasz w obrębie jednego zdania |
| `akapit` | wymaga spojrzenia na cały akapit |
| `rozdział` | wymaga przejrzenia całego rozdziału |
| `cała praca` | ⛔ NIE rób przy okazji akapitu — osobne zadanie na wszystkie rozdziały naraz |
| `skład` | szablon dokumentu wynikowego, nie tekst źródłowy; zgłoś, nie poprawiaj |
| `nowa treść` | brakujące rysunki, tabele, wzory; zgłoś propozycję, nie poprawiaj |
| `weryfikacja w danych` | rozstrzyga kod, dane albo źródło, nigdy wygoda redaktora |

⛔ **Reguła warstwy.** Zarzut dotyczący warstwy szerszej niż ta, na której pracuje
redaktor, nie jest podstawą do odrzucenia jego zmiany. Jest osobnym zadaniem.

---

## A — język i redakcja zdania

Grupa A obsługuje najczęstszy zarzut recenzentów wobec prac pisanych z pomocą modeli:
tekst jest poprawny, ale brzmi popularnonaukowo albo maszynowo.

**A1 — myślnik w tekście** (warstwa: zdanie)

Co to jest: znak `—` (em dash) w prozie. Czytany przez recenzentów jako sygnał tekstu
generowanego maszynowo. Konsekwencją bywa odrzucenie pracy jako wątpliwie samodzielnej,
niezależnie od tego, kto naprawdę ten znak wpisał.

Jak poprawiasz: zamiennik zależy od funkcji zdaniowej, nie ma jednego uniwersalnego.
Przecinki z obu stron (wtrącenie), nawias (dopowiedzenie poboczne), kropka i nowe zdanie
(myśl samodzielna), „czyli"/„to znaczy" (wyjaśnienie), dwukropek (wyliczenie KOŃCZĄCE
zdanie). ⛔ Nigdy dywiz `-` w środku zdania.

Gdzie myślnik ZOSTAJE: tytuły cytowanych źródeł w bibliografii (cudza własność, zmiana
byłaby przekłamaniem), objaśnienia oznaczeń pod wzorami („$k$ — liczba par"), elipsy
zastępujące pominięty czasownik („wariant A poprawny w 90%, wariant B — żaden").

**A2 — dwukropek w połowie zdania** (warstwa: zdanie)

Co to jest: zdanie dokańczane po dwukropku zamiast podziału na dwa zdania.

Jak poprawiasz: rozbijasz na dwa zdania. Dwukropek wprowadzający wyliczenie na końcu
zdania jest POPRAWNY — to fałszywe trafienie, odrzuć je.
⛔ To najczęstszy błąd wtórny całej metodyki: usunięcie myślnika (A1) przez wstawienie
dwukropka dokańczającego myśl usuwa jeden zarzut i tworzy drugi.

**A3 — anglicyzm** (warstwa: zdanie LUB cała praca)

Co to jest: zapożyczenie bez potrzeby.

⛔ Termin występujący w pracy wielokrotnie NIE jest sprawą zdania. Spolszczenie w jednym
miejscu tworzy dwie wersje terminu, czyli stan gorszy niż przed poprawką. Sprawdź grepem
liczbę wystąpień w całym tekście i przy więcej niż jednym zgłoś jako zadanie na całą pracę.

Jak poprawiasz: polski odpowiednik z rejestru terminologicznego. Termin bez odpowiednika
zostaje, ale przy pierwszym wystąpieniu dostaje polskie objaśnienie i oryginał w nawiasie
kursywą.

**A4 — zdanie za długie** (warstwa: zdanie)

Co to jest: powyżej 35 słów ALBO więcej niż dwie myśli w jednym zdaniu.

Jak poprawiasz: dzielisz na krótkie zdania, każde z jedną myślą, każde wynikające
logicznie z poprzedniego. Próg operacyjny: powyżej 35 słów kwalifikuj zawsze; między 25
a 35 kwalifikuj, gdy zdanie niesie więcej niż dwie myśli; poniżej 25 słów nie kwalifikuj
samą długością.

**A5 — kolokwializm lub odwołanie do prozy życia** (warstwa: zdanie)

Co to jest: potoczne słownictwo, obrazowanie z życia codziennego zamiast definicji.

Jak poprawiasz: definiujesz potrzebę, problem badawczy i kryteria oceny zamiast opowiadać.

**A6 — ściana liczb w tekście** (warstwa: zdanie)

Co to jest: ciąg wartości statystycznych w prozie.

Jak poprawiasz: opis słowny zostaje w tekście, wartości idą do tabeli, w tekście zostaje
odwołanie do niej. Czytelnik ma z prozy wynieść wniosek, a z tabeli liczby.

**A7 — forma osobowa zamiast bezosobowej** (warstwa: zdanie)

Co to jest: „uważam", „zbadałem", „widzimy", „nasza praca".

Jak poprawiasz: „przeprowadzono", „wykazano", „przyjęto", „zastosowano".

**A8 — pytanie retoryczne** (warstwa: zdanie)

Co to jest: pytanie w tekście zamiast twierdzenia. Praca ma definiować, nie pytać.

Jak poprawiasz: zamieniasz na twierdzenie albo na zdefiniowanie problemu badawczego.

**A9 — parametry w nawiasach** (warstwa: zdanie)

Co to jest: wyliczanie wartości i warunków w nawiasie zamiast w tabeli.

Jak poprawiasz: zawartość nawiasu do tabeli, w tekście odwołanie.

**A10 — zdanie nie wynika z poprzedniego** (warstwa: akapit)

Co to jest: skok myślowy, brak łącznika logicznego.

Jak poprawiasz: dopisujesz łącznik albo zdanie pomostowe.

**A11 — niejasna lub piętrowa składnia** (warstwa: zdanie)

Co to jest: szyk przestawny, wielokrotne zagnieżdżenie, zdanie gubiące kontekst.

Jak poprawiasz: prostujesz szyk, rozbijasz zagnieżdżenia, jedna myśl na zdanie.

**A12 — sformułowanie wartościujące** (warstwa: zdanie)

Co to jest: „zaskakująco", „niestety", „warto", „ciekawy" zamiast opisu faktu.

Jak poprawiasz: usuwasz ocenę, zostawiasz fakt. Zamiast „zaskakująco niska" piszesz ile.

**A13 — termin obcy bez objaśnienia przy pierwszym użyciu** (warstwa: rozdział)

Co to jest: skrót albo termin użyty zanim czytelnik dostał jego znaczenie.

Jak poprawiasz: przy pierwszym użyciu rozwinięcie i polskie znaczenie, dalej sam termin.

**A14 — metafora lub personifikacja** (warstwa: zdanie)

Co to jest: obraz zamiast opisu („specyfikacja bywała balastem, nie mapą").

Jak poprawiasz: podmiotem zdania ma być procedura albo wynik, nie rzecz uosobiona.

**A15 — narracja o samej pracy** (warstwa: zdanie)

Co to jest: zdanie mówi, co praca robi, zamiast mówić rzecz. Komentarz autorski.

Jak poprawiasz: zapowiedź struktury zostaje, komentarz autorski usuwasz.

**A16 — myślnik ukryty pod inny znak** (warstwa: zdanie)

Co to jest: półpauza `–` albo dywiz `-` w spacjach, w funkcji myślnika. Pozorna poprawka.

Jak poprawiasz: traktujesz jak A1. ⛔ Nigdy nie podmieniasz jednego znaku pauzy na drugi.

**A17 — antyteza retoryczna** (warstwa: zdanie)

Co to jest: figura „nie X, lecz Y" zamiast twierdzenia wprost.

Jak poprawiasz: rozbijasz na twierdzenie wprost. Figurę zostawiasz tylko przy realnym
kontraście, który sam w sobie jest treścią.

**A18 — akapit bez formy bezosobowej** (warstwa: akapit)

Co to jest: metryka AKAPITU, nie zdania — akapit dłuższy niż trzy zdania, w którym
podmiotem nie jest procedura ani wynik.

Jak poprawiasz: pracujesz na całym akapicie naraz, sprawdzasz, kto jest podmiotem.

**A19 — nagromadzenie wtrąceń** (warstwa: zdanie)

Co to jest: kilka wtrąceń w nawiasach i przecinkach naraz gubi tok zdania.

Jak poprawiasz: rozbijasz na osobne zdania. Jedno wtrącenie na zdanie to maksimum.

---

## B — aparat naukowy i cytowania

**B1 — niewłaściwy styl cytowania** (warstwa: cała praca)

Co to jest: przypisy dolne tam, gdzie wymagana jest numeracja `[X]`, albo mieszanie stylów.

Jak poprawiasz: jeden styl na całą pracę, wybrany na starcie i zapisany w rejestrze
decyzji. Przy stylu numerycznym: numer wg PIERWSZEGO wystąpienia w tekście, to samo
źródło zawsze pod tym samym numerem. Zadanie na całą pracę naraz, nigdy przy okazji
akapitu.

**B2 — brak odwołania przy nazwie własnej** (warstwa: zdanie)

Co to jest: firma, organizacja, metoda, narzędzie albo badanie przywołane bez odwołania
do źródła przy pierwszym wystąpieniu.

Jak poprawiasz: dodajesz odwołanie przy PIERWSZYM wystąpieniu. Zasada: wszystko, czego
nie jesteś właścicielem, ma źródło.

**B3 — rysunek, tabela lub wzór bez zapowiedzi** (warstwa: akapit)

Co to jest: element nieprzywołany w tekście przed swoim wystąpieniem.

Jak poprawiasz: dopisujesz zapowiedź przed elementem („Wyniki przedstawia tabela 4.3.").

**B4 — numeracja załączników** (warstwa: cała praca)

Co to jest: odwołania do załączników bez numerów.

Jak poprawiasz: „stanowi załącznik pracy" → „stanowi załącznik nr N". ⛔ Numeru nie
wymyślasz — brak listy załączników zgłaszasz jako zadanie na całą pracę.

**B5 — niespójna bibliografia** (warstwa: cała praca)

Co to jest: to samo źródło pod różnymi numerami albo niepełny opis bibliograficzny.

Jak poprawiasz: każde źródło z pełnym opisem, to samo źródło zawsze pod tym samym numerem.

**B6 — przypis zbiorczy** (warstwa: rozdział)

Co to jest: kilka różnych źródeł pod jednym numerem. Przy cytowaniu numerycznym jeden
numer to dokładnie jedno źródło.

Jak poprawiasz: rozbijasz na tyle numerów, ile jest źródeł. Zadanie na całą pracę naraz.

**B7 — przypis z sufiksem literowym** (warstwa: rozdział)

Co to jest: `[7a]`, `[44b]` dopisane po fakcie. Dowód, że kolejność numeracji się rozjechała.

Jak poprawiasz: przenumerowanie w kolejności wystąpienia, jednym skryptem na całą pracę.

**B8 — źródło przy nazwie w zdaniu sąsiednim** (warstwa: akapit)

Co to jest: nazwa własna pierwszy raz bez odwołania, źródło stoi zdanie lub dwa dalej.

Jak poprawiasz: przenosisz odwołanie do zdania z PIERWSZYM wystąpieniem nazwy. Zbiór
przypisów w pliku musi zostać ten sam, zmienia się tylko miejsce.

**B9 — źródło nieistniejące albo niesprawdzone** (warstwa: weryfikacja w danych)

Co to jest: pozycja bibliograficzna, której istnienia nikt nie potwierdził. Klasyczna
awaria pracy pisanej z modelem językowym: opis wygląda poprawnie, autorzy istnieją,
czasopismo istnieje, a konkretny artykuł nie.

Jak poprawiasz: ⛔ Każda pozycja przed złożeniem ma potwierdzone istnienie — DOI
rozwiązujący się do rekordu, strona wydawcy albo plik PDF na dysku. Pozycja bez
potwierdzenia wypada z bibliografii razem ze zdaniem, które się na nią powoływało.
Nie „poprawia się" jej opisu, bo poprawianie opisu nieistniejącej pracy tworzy
wiarygodniejsze zmyślenie.

**B10 — cytowanie za kimś podane jako własne** (warstwa: zdanie)

Co to jest: teza wzięta z pracy przeglądowej, a przypisana pracy oryginalnej, której
autor nie czytał.

Jak poprawiasz: albo docierasz do oryginału i cytujesz go po przeczytaniu, albo zapisujesz
jawnie jako cytowanie wtórne („za: [X]").

**B11 — dzielenie zdania rozrywa pokrycie źródłem** (warstwa: zdanie)

Co to jest: zdanie z przypisem podzielone na dwa. Przypis zostaje przy jednym fragmencie,
drugi staje się twierdzeniem bez źródła.

Jak poprawiasz: przed podziałem ustal, do których fragmentów odnosi się źródło. Do
wszystkich — powtórz odwołanie przy każdym. Do jednego — podziel tak, żeby reszta nie
wyglądała na cytowaną. To samo dotyczy nazwiska autora: teza komuś przypisana zostaje
w zdaniu z jego nazwiskiem albo dostaje jawną atrybucję.

---

## C — merytoryka i siła twierdzeń

Grupa C jest groźniejsza niż cała grupa A razem wzięta. Myślnik naraża na zarzut
niesamodzielności. Fałszywe albo zawyżone twierdzenie naraża na zarzut nierzetelności.

**C1 — zawyżony czasownik dowodowy** (warstwa: zdanie)

Co to jest: „wykazano", „udowodniono", „dowodzi", „przesądza" obiecują rozstrzygnięcie
mocniejsze niż niosą dane.

Jak poprawiasz: czasownik dobierasz do siły dowodu — „zaobserwowano", „zmierzono",
„nie znaleziono statystycznie istotnych dowodów". Czasownik dowodowy zostaje wyłącznie
przy opisie cudzego badania, które faktycznie coś wykazało.

**C2 — wniosek o braku efektu z braku istotności** (warstwa: zdanie)

Co to jest: „wykazano brak różnicy" na podstawie wyniku nieistotnego statystycznie.
Brak dowodu na efekt nie jest dowodem na brak efektu.

Jak poprawiasz: „nie znaleziono statystycznie istotnych dowodów na różnicę", z jawnym
zaznaczeniem ograniczonej mocy badania i, jeśli to możliwe, z podaniem granicy
wykrywalności — jaką najmniejszą różnicę badanie było w stanie wykryć.

**C3 — zbyt szerokie twierdzenie o pierwszeństwie** (warstwa: zdanie)

Co to jest: „pierwsza praca", „pierwsze kontrolowane badanie". Twierdzenie szersze, niż
potrzeba do uzasadnienia oryginalności, a łatwe do podważenia jednym kontrprzykładem.
Przy obecnym tempie publikacji recenzent, który znajdzie podobną pracę, ma podstawę do
odrzucenia całości.

Jak poprawiasz: zawężasz do realnej luki („nie zidentyfikowano kontrolowanego porównania
X i Y przy tym samym modelu i tych samych zadaniach"). Oryginalność zostaje, ryzyko znika.

**C4 — twierdzenie o wyczerpaniu literatury** (warstwa: zdanie)

Co to jest: „w literaturze brakuje", „nie istnieją badania", „jedyne badanie".
Twierdzenie o tym, czego nie ma, jest nie do obrony — wymagałoby przeczytania wszystkiego.

Jak poprawiasz: przenosisz twierdzenie z literatury na własną kwerendę i zawężasz zakres:
„w przeprowadzonej kwerendzie (bazy, słowa kluczowe, zakres lat) nie zidentyfikowano…".

**C5 — zawyżone twierdzenie o odtwarzalności** (warstwa: zdanie)

Co to jest: „co do bitu", „w pełni odtwarzalny", „gwarantuje", „zawsze" — bez osobnego
testu, który by to potwierdził.

Jak poprawiasz: „wysoka replikowalność proceduralna dzięki zamrożonym wersjom
oprogramowania, parametrom i ziarnom losowości" — albo wskazujesz artefakt
potwierdzający mocniejszą wersję.

**C6 — deklaracja weryfikacji, której nie przeprowadzono** (warstwa: zdanie)

Co to jest: praca deklaruje własność wymagającą osobnego eksperymentu, którego nie ma.

Jak poprawiasz: albo wskazujesz artefakt, albo osłabiasz twierdzenie do tego, co
faktycznie zapewniono, i dopisujesz zdanie mówiące wprost, czego nie sprawdzono.
⛔ Milczące usunięcie mocnego twierdzenia jest gorsze niż jawnie postawiona granica —
recenzent, który pamięta poprzednią wersję, przeczyta to jako zacieranie śladu.

**C7 — mylny opis przedmiotu porównania** (warstwa: zdanie)

Co to jest: praca twierdzi, że mierzy wpływ jednego czynnika, a w rzeczywistości
porównywane warianty różnią się kilkoma czynnikami naraz.

Jak poprawiasz: piszesz konsekwentnie, że badany jest efekt całego zoperacjonalizowanego
wariantu, nie pojedynczego czynnika. Rozdzielenie czynników wymagałoby dodatkowego
ramienia kontrolnego i tak to nazywasz w ograniczeniach.

**C8 — metryka złożona opisana jako prosta** (warstwa: rozdział)

Co to jest: metryka łączy dwa zjawiska, a nazwa sugeruje jedno (np. liczba iteracji do
sukcesu, w której niepowodzenie dostaje wartość karną — miara łączy szybkość dojścia do
sukcesu z częstością niepowodzeń).

Jak poprawiasz: ⛔ nie zmieniasz definicji ani wartości. Nadajesz metryce nazwę ujawniającą
złożoność i dopisujesz zdanie wymieniające oba składniki. Ta sama nazwa w metodyce,
wynikach i dyskusji, inaczej powstaje nowa niespójność.

**C9 — wynik na podłodze albo suficie wykonalności** (warstwa: rozdział)

Co to jest: wszystkie warianty osiągnęły 0% albo 100%. Z takiego wyniku nie wynika, że
warianty są równie skuteczne — wynika, że zadanie nie mierzyło różnicy między nimi.

Jak poprawiasz: opisujesz wynik jako informację o trudności zadania, nie o równoważności
metod, i przenosisz go do ograniczeń.

**C10 — twierdzenie niezgodne z kodem, danymi lub źródłem** (warstwa: weryfikacja w danych)

Co to jest: zdanie opisuje procedurę, parametr albo liczbę inaczej, niż potwierdza
materiał źródłowy. Nie chodzi o zbyt mocne sformułowanie, tylko o twierdzenie nieprawdziwe.

Jak poprawiasz: ⛔ NIGDY nie wybierasz wygodniejszej wersji. Ustalasz stan w źródle,
cytujesz plik i numer linii w uzasadnieniu, dopiero potem przepisujesz zdanie. Gdy źródła
nie da się rozstrzygnąć, zdanie idzie do decyzji autora, nie do zmiany.

**C11 — rozjazd pojęcia między rozdziałami** (warstwa: cała praca)

Co to jest: ten sam obiekt opisany inaczej w dwóch miejscach. Niewidoczne przy czytaniu
jednego rozdziału, a właśnie tak pracuje pipeline zdaniowy.

Jak poprawiasz: ustalasz wersję zgodną z danymi, wpisujesz do rejestru pojęć, dopiero
potem prostujesz wszystkie miejsca jednym przebiegiem na całej pracy.

**C12 — niespójność liczbowa między rozdziałami** (warstwa: cała praca)

Co to jest: ta sama wielkość podana w dwóch miejscach z różnymi wartościami, albo
arytmetyka, która się nie zgadza (deklarowana liczba przebiegów niezgodna z iloczynem
czynników planu badania).

Jak poprawiasz: przeliczasz z definicji planu badania, prostujesz wszystkie wystąpienia
naraz. Różnica uzasadniona inną metodyką pomiaru zostaje, ale musi być jawnie nazwana.

**C13 — odstępstwo od prespecyfikacji** (warstwa: rozdział)

Co to jest: analiza wykonana inaczej, niż zapowiadał protokół metodyki. Recenzent zestawi
metodykę z wynikami i zapyta, czy sposób analizy dobrano po zobaczeniu wyników.

Jak poprawiasz: wersja prespecyfikowana zostaje jako główna, wersja alternatywna obok jako
analiza wrażliwości, z jawnym powodem odstępstwa. To jest jedyny bezpieczny układ.

**C14 — wniosek niewynikający z wyników** (warstwa: rozdział)

Co to jest: zakończenie twierdzi więcej albo co innego niż rozdział z wynikami. Częste po
turach poprawek, w których osłabiono wyniki, a nie ruszono wniosków.

Jak poprawiasz: dla każdego zdania wniosku wskazujesz konkretny wynik, który go niesie.
Brak takiego wyniku oznacza usunięcie zdania, nie jego złagodzenie.

**C15 — korelacja opisana jako przyczyna** (warstwa: zdanie)

Co to jest: „powoduje", „prowadzi do", „przekłada się na" przy danych obserwacyjnych.

Jak poprawiasz: „współwystępuje z", „wiąże się z", plus zdanie o możliwych czynnikach
zakłócających.

---

## D — struktura tekstu

**D1 — wiszący nagłówek lub za krótki podrozdział** (warstwa: rozdział)

Co to jest: nagłówek postawiony w środku tekstu bez potrzeby; podrozdział krótszy niż
kilka stron, bez własnej ilustracji i tabeli. Sygnał, że struktura powstała z listy
zadań, nie z logiki wywodu.

Jak poprawiasz: łączysz sąsiednie podrozdziały albo przebudowujesz rozdział.
⛔ Nie usuwasz samego nagłówka zostawiając treść bez przynależności.

**D2 — termin użyty bez wprowadzenia** (warstwa: akapit)

Co to jest: pojęcie pojawia się, zanim czytelnik dostał jego znaczenie.

Jak poprawiasz: wprowadzasz termin zdanie wcześniej. Zasada „od zera do bohatera":
na wstępie zakładasz, że czytelnik nie wie nic.

**D3 — brak słownika pojęć** (warstwa: cała praca)

Co to jest: praca z dużą liczbą terminów specjalistycznych bez słownika.

Jak poprawiasz: słownik jako obowiązkowy element pracy, nie dodatek. Każdy termin
specjalistyczny użyty w tekście głównym ma definicję w słowniku.

**D4 — rozjazd wstępu z zakończeniem** (warstwa: cała praca)

Co to jest: wstęp zapowiada inne cele, pytania albo zakres niż te, z których rozlicza się
zakończenie.

Jak poprawiasz: wstęp i zakończenie czyta się i poprawia razem, jednym przebiegiem, na
samym końcu pracy. Cel zapowiedziany bez rozliczenia i wniosek bez zapowiedzianego celu
to ta sama usterka widziana z dwóch stron.

**D5 — rozdział bez wprowadzenia albo podsumowania** (warstwa: rozdział)

Co to jest: rozdział zaczyna się od szczegółu i kończy w połowie myśli.

Jak poprawiasz: każdy rozdział otwiera akapit mówiący, co czytelnik w nim znajdzie
i po co, a zamyka akapit z wnioskiem cząstkowym i przejściem do następnego.

**D6 — treść główna schowana w załączniku** (warstwa: cała praca)

Co to jest: rozstrzygające dane, kluczowa tabela albo istotny fragment metodyki
przeniesione do załącznika, żeby zmieścić się w limicie objętości.

Jak poprawiasz: w załączniku zostaje materiał uzupełniający i dowodowy. To, co jest
potrzebne do zrozumienia wywodu i sprawdzenia wniosku, wraca do tekstu głównego.

---

## E — skład dokumentu

Grupa E nie jest sprawą tekstu źródłowego. **Zgłaszasz, nie poprawiasz** — poprawka
należy do szablonu i warstwy eksportu, nigdy do pliku źródłowego.

| Kod | Co to jest |
|---|---|
| **E1** | brak strony tytułowej albo niezgodność ze wzorem uczelni |
| **E2** | brak spisu treści albo spis niewypełniony w pliku wynikowym |
| **E3** | tekst niewyjustowany |
| **E4** | odstępy i wcięcia akapitów niezgodne z wymogiem |
| **E5** | sierotki, wdowy i bękarty |
| **E6** | krawędzie i formatowanie tabel |
| **E7** | numeracja stron: położenie, format, strona startowa |
| **E8** | brak wykazu rysunków, tabel albo skrótów |
| **E9** | objętość poza dopuszczalnym zakresem |

---

## F — brakująca treść

Grupa F to nie usterka istniejącego tekstu, tylko brak. **Zgłaszasz propozycję**, nie
poprawiasz w miejscu.

| Kod | Co to jest |
|---|---|
| **F1** | za mało rysunków (schematów, nie wykresów) |
| **F2** | za mało diagramów prezentujących budowę i przepływ |
| **F3** | za mało diagramów prezentujących wyniki, i za mało ich typów |
| **F4** | za mało wzorów; zależność opisana słowami zamiast zapisana formalnie |
| **F5** | brak tabeli w podrozdziale, który jej wymaga |

---

## Jak rozszerzać ten katalog

Kategoria trafia tu wtedy, gdy wystąpiła **dwa razy** — pierwszy raz to wypadek, drugi
to wzorzec. Przy dopisywaniu podaj wszystkie cztery elementy: kod, definicję, warstwę
i instrukcję naprawy. Kategoria bez warstwy zablokuje pipeline, kategoria bez instrukcji
naprawy wróci jako spór między agentami.

Kategorie własne dopisuj na końcu grupy z kolejnym numerem. ⛔ Nie przenumerowuj
istniejących — kody są używane w zapisanych werdyktach, arkuszu zmian i changelogu,
a przenumerowanie unieważnia historię.
