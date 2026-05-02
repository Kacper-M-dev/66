# Gra Karciana "66" (Schnapsen)

Implementacja klasycznej gry karcianej **"66"** napisana w języku Python. Projekt pozwala na rozgrywkę jednoosobową przeciwko algorytmowi AI (aktualnie "AI" losuje karte). Gra kładzie nacisk na strategię, liczenie punktów oraz umiejętne zarządzanie kartami atutowymi.

## 📝 O projekcie
Program odzwierciedla pełną mechanikę gry, w tym specyficzną hierarchię kart, system meldunków oraz zmianę zasad po wyczerpaniu talii. Został stworzony jako projekt edukacyjny skupiający się na logice gier oraz czystości kodu.

## 🃏 Zasady Gry
*   **Talia:** 24 karty (od 9 do Asa).
*   **Cel:** Zdobycie minimum **66 punktów**.
*   **Punktacja:** As (11), 10 (10), Król (4), Dama (3), Walet (2), 9 (0).
*   **Atut (Trump):** Jedna karta wyznacza kolor atutowy, który bije wszystkie inne kolory.
*   **Meldunki:** Para Król + Dama w tym samym kolorze daje 20 pkt (lub 40 pkt w kolorze atutowym).
*   **Faza Wymuszona:** Gdy talia się kończy, gracze mają obowiązek dokładania do koloru i przebijania karty przeciwnika.

## 🚀 Jak uruchomić

### Wymagania
*   Zainstalowany **Python 3.6** lub nowszy.

### Uruchomienie
1. Sklonuj repozytorium lub pobierz plik `main.py`.
2. Otwórz terminal w folderze projektu.
3. Uruchom grę komendą:
   ```bash
   python main.py
   ```
## TODO
[] Implementacja "inteligentnego" AI.

[] AI potrafiące wymieniać 9 na kartę ze spodu.

[] Tabela z podsumowaniem punktów po każdej turze.

