# Model Wzrostu Roślin

Projekt symulujący wzrost roślin przy użyciu danych wejściowych. Program sprawdza zależność między wielkością osobnika a jego sąsiadami. 

## Działanie

1. Program generuje kolejne etapy wzrostu rośliny.
2. Każdy etap jest zapisywany jako osobna klatka.
3. Finalnie tworzony jest animowany GIF pokazujący cały proces oraz mapa LISA pokazująca lokalną autokorelację przestrzenną.

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

