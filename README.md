# Temat: Detekcja anomalii na syntetycznych obrazach histopatologicznych z wykorzystaniem autoenkoderów


## Cel pracy: 
Celem pracy jest zaprojektowanie i implementacja systemu do generowania syntetycznych obrazów przypominających mikroskopowe obrazy próbek tkanek wykorzystywanych w diagnostyce nowotworów. Opracowane narzędzie umożliwi tworzenie struktur imitujących elipsoidalne jądra komórkowe, z pełną kontrolą nad ich cechami statystycznymi, takimi jak rozmiar, tekstura czy rozkład przestrzenny. Wygenerowane obrazy posłużą do przeprowadzenia eksperymentów z wykorzystaniem autoenkoderów w detekcji anomalii, opierającej się na założeniu, że model uczony wyłącznie na zdrowych wzorcach będzie gorzej rekonstruował nieznane wzorce chorobowe. Różnica w jakości rekonstrukcji posłuży do identyfikacji anomalii. Celem badań jest ocena skuteczności takiego podejścia w wykrywaniu odchyleń od wzorcowych (zdrowych) struktur komórkowych, co może znaleźć potencjalne zastosowanie w diagnostyce medycznej, zwłaszcza w kontekście wykrywania zmian patologicznych.

 ## Zakres pracy:

1. Analiza literatury – przegląd metod detekcji anomalii w obrazach medycznych, ze szczególnym uwzględnieniem autoenkoderów

2. Projekt i implementacja systemu do generowania obrazów syntetycznych

3. Trening i testowanie autoenkodera na obrazach syntetycznych

 4. Ocena skuteczności wykrywania anomalii na podstawie różnic w jakości rekonstrukcji, w zależności od rodzaju i intensywności wprowadzonych odchyleń

5. Dokumentacja utworzonego rozwiązania oraz podsumowanie wyników eksperymentów

## Potencjalne zastosowania

Wyniki projektu mogą mieć zastosowanie w diagnostyce medycznej, wspierając wykrywanie zmian patologicznych w obrazach mikroskopowych.


## Pliki
Głównym plikiem projektu, zawierającym implementację systemu, jest notatnik Jupyter Notebook znajdujący się pod ścieżką /notebook/03_1_testy_i_wyniki.ipynb.
Projekt w przysłości zostanie rozbudowany o dodatkowe funkcje, oraz sprawdzone zostanie działanie enkodera dla funkcji straty SSIM.

