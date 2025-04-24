# Model Wzrostu Roślin

Projekt symulujący wzrost roślin przy użyciu danych wejściowych. Program sprawdza zależność między wielkością osobnika a jego sąsiadami. 

## Struktura projektu

model_wzrostu_roslin/ │ ├── frames/ # Generowane klatki animacji ├── main.py # Główna logika programu ├── config.py # Parametry wzrostu roślin ├── utils.py # Funkcje pomocnicze ├── requirements.txt # Wymagane biblioteki └── README.md # Ten plik

## Działanie

1. Program generuje kolejne etapy wzrostu rośliny.
2. Każdy etap jest zapisywany jako osobna klatka.
3. Finalnie tworzony jest animowany GIF pokazujący cały proces.

## Uruchamianie

1. Środowisko wirtualne

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate    # Windows
2. Intstalacja bibliotek
`pip install -r requirements.txt`
3. Uruchamianie programu
`python main.py`
