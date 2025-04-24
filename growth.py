import numpy as np
from scipy.spatial import KDTree

def population_growth(T, positions, r_interact, alpha, mutation_strength, r_0, traits, trajectories):
    """
    Równanie zahamowanego wzrostu. Wzrost jest hamowany przez liczbę sąsiadów, gdzie sąsiedztwo jest definiowane przez
    promień r_interact.
    :param T: liczba kroków czasowych.
    :param positions: pozycje osobników.
    :param r_interact: promień interakcji.
    :param alpha: siła hamowania wzrostu
    :param mutation_strength: szum.
    :param r_0: początkowe tempo wzrostu.
    :param traits: wielkości osobników
    :param trajectories: ([positions], [traits]).
    :return: trajectories, traits.
    """

    for t in range(T):
        tree = KDTree(positions)

        # Spowolniony wzrost rośliny w zależności od sąsiedztwa
        for i, pos in enumerate(positions):
            neighbors = tree.query_ball_point(pos, r_interact)
            n_neighbors = len(neighbors) - 1  # -1 bo nie liczymy siebie samego

            # Zmniejszenie tempa wzrostu w zależności od gęstości
            r_eff = r_0 * np.exp(-alpha * n_neighbors)

            # Wzrost rośliny
            traits[i] *= 1 + r_eff * mutation_strength  # roślina rośnie
            traits[i] = np.clip(traits[i], 0.1, 5.0)  # ograniczenie maksymalnej wielkości rośliny

        trajectories.append((np.array(positions.copy()), np.array(traits.copy())))
    return trajectories, traits