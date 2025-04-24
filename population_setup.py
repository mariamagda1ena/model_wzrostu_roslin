import numpy as np


def setup_clustered_population(clusters, N_0, L):
    """
    Tworzy zklasteryzowane ustawienie populacji poprzez wylowsowaanie pozycji centroidów klastrów i równomierne
    rozmieszczenie osobników wokół nich.
    :param clusters: liczba klastrów
    :param N_0: liczba osobników
    :param L: rozmiar przestrzeni
    :return: pozycje osobników
    """
    positions = []
    for _ in range(clusters):
        center_x, center_y = np.random.uniform(0.2 * L, 0.8 * L, 2)
        for _ in range(N_0 // clusters):
            dx, dy = np.random.normal(0, L * 0.05, 2)
            x, y = center_x + dx, center_y + dy
            if 0 <= x <= L and 0 <= y <= L:
                positions.append([x, y])
    positions = positions[:N_0]
    return positions

def setup_random_population(N_0, L):
    """
    Tworzy losowe ustawienie populacji.
    :param N_0: population size
    :param L: area size
    :return: positions of individuals
    """
    positions = []
    for _ in range(N_0):
        x, y = np.random.uniform(0, L, 2)
        positions.append([x, y])
    return positions