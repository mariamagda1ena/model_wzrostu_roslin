import matplotlib.pyplot as plt
import numpy as np

def plot_population(t, pos, trait, save_path=None):
    """
    Rysuje populację w 2D razem ze skalą kolorów, która odzwierciedla wielkość osobników. Promień punktów na wykresie
    odpowiada wielkości osobników.
    :param t: krok czasowy
    :param pos: pozycje osobników
    :param trait: wielkość osobników
    :param save_path: ścieżka do zapisu grafu
    """
    plt.figure(figsize=(8, 8))

    # Tworzenie skali kolorów
    sc = plt.scatter(pos[:, 0], pos[:, 1], s=trait * 80, c=trait, cmap='viridis', alpha=0.8, edgecolors='k', vmin=0.1,
                     vmax=5.0)

    # Dodanie paska kolorów
    plt.colorbar(sc, label="Wielkość rośliny")
    plt.title(f"Wzrost roślin (Krok {t})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")

    # Zapisz wykres do katalogu 'frames'
    if save_path is not None:
        plt.savefig(save_path)
    plt.close()


def generate_LISA_plot(lisa, traits, positions):
    """
    Rysuje mapę LISA
    :param lisa: lokalny współczynnik autokorelacji przestzrennej Morana.
    :param traits: wielkość osobników.
    :param positions: pozycje osobników.
    """
    # Kolory mapy LISA
    region_colors = np.full(len(traits), 'lightgrey', dtype=object)
    sig = lisa.p_sim < 0.1
    quadrant = lisa.q

    region_colors[(quadrant == 1) & sig] = 'red'  # High-High
    region_colors[(quadrant == 2) & sig] = 'blue'  # Low-Low
    region_colors[(quadrant == 3) & sig] = 'lightgreen'  # Low-High
    region_colors[(quadrant == 4) & sig] = 'orange'  # High-Low

    # Wizualizacja
    plt.figure(figsize=(9, 6))
    plt.scatter(positions[:, 0], positions[:, 1], c=region_colors, edgecolor='k', s=60)
    plt.title("Mapa LISA (4 najbliższych sąsiadów)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()