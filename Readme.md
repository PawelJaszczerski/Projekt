# Modelowanie drgań wahadła matematycznego
Anna Ardanowska 181162, Paweł Jaszczerski 181085
## 1. Wstęp:
### Cel projektu:
badanie oscylacji wahadła matematycznego, zamodelowanie jego ruchu
### Opis modelowanego zjawiska fizycznego
Wahadło matematyczne składa się z punktu materialnego zawieszonej na długiej, nieważkiej,
nierozciągliwej nici. Masa punktowa jest wychylana z położenia równowagi i porusza się po
fragmencie okręgu o środku w punkcie zawieszenia nici. Dla małych kątów wychylenia (do
kilku stopni, sin(Θ) ≈ Θ), przyjmuje się, że drga ono harmonicznie. Zwykle pomija się opory
ruchu. Ruch drgający powodowany jest siłą grawitacji, a właściwie jej składową styczną do
toru ruchu.
### -Opis wykorzystywanych narzędzi:
- Język: Python3 (3.8)
- Biblioteki: matplotlib, NumPy, ewentualne biblioteki do wizualizacji (podlega
aktualizacji)
- Program PyCharm z kontrolą wersji poprzez GitHub
## 2. Ogólny opis projektu i możliwe alternatywy
Program modeluje ruch wahadła matematycznego, pobiera dane z pliku. Zwraca parametry i równanie ruchu, wykres wychylenia, energii potencjalnej i kinetycznej od czasu oraz wyświetla wizualizację wahadła.
### Alternatywy:
uwzględnienie większych wychyleń, drgań tłumionych
## 3. Specyficzne wymagania:
### Wymagania funkcjonalne:
Program pobiera dane z pliku zewnętrznego i wczytuje wartości z odpowiedniej części,
przetwarza je za pomocą zaprogramowanych funkcji. W przypadku, gdy parametry nie
spełniają wymagań zwraca konkretny błąd. Wyznacza i wyświetla równanie ruchu i
parametry w oparciu o równania opisujące ruch drgający, korzystając z modułu NumPy.
Wykorzystując moduł matplotlib tworzy wykresy. Wyświetla wizualizację ruchu wahadła za
pomocą modułu zewnętrznego. Umożliwia wybór danych do wyświetlenia. Obsługuje pliki o
konkretnym układzie, w przeciwnym przypadku zwraca odpowiedni błąd.
### Wymagania niefunkcjonalne:
Program działa szybko i płynnie dzięki pracy na tablicach NumPy i funkcjach
zoptymalizowanych pod kątem czasu pracy. Wyświetla dane liczbowe z dokładnością do
czterech miejsc po przecinku.
## 4. Harmonogram
- 27.11 – funkcje i wyliczenia
- 4.12 - wykresy
- 11.12 - wizualizacja
- 18.12 - obsługa plików
- 8.01 - obsługa błędów
