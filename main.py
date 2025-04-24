import os
from numpy.distutils.command.config import config
from scipy.spatial import KDTree
from scipy.stats import spearmanr
from libpysal.weights import KNN
from esda.moran import Moran
from esda.moran import Moran_Local

from growth import population_growth
from population_setup import *
from visualisation import *
import config


def main():
    """
    Przeprowadza symulację wzrostu roślin.
    """
    trajectories = []
    if config.random_population:
        positions = setup_random_population(config.N_0, config.L)
    else:
        positions = setup_clustered_population(config.clusters, config.N_0, config.L)
    traits = [config.initial_size] * len(positions)
    trajectories.append((np.array(positions.copy()), np.array(traits.copy())))

    # Symulacja wzrostu
    trajectories, traits = population_growth(config.T, positions, config.r_interact, config.alpha, config.mutation_strength, config.r_0, traits, trajectories)

    # Obliczanie korelacji sąsiedzkiej
    positions = np.array(positions)
    traits = np.array(traits)
    tree = KDTree(positions)
    neighbor_means = []

    for i, pos in enumerate(positions):
        dists, idxs = tree.query(pos, k=5)  # siebie + 4 sąsiadów
        neighbors = idxs[1:]  # pomijamy siebie
        if len(neighbors) > 0:
            mean_trait = np.mean(traits[neighbors])
            neighbor_means.append(mean_trait)
        else:
            neighbor_means.append(np.nan)

    neighbor_means = np.array(neighbor_means)
    valid = ~np.isnan(neighbor_means)

    r_spearman, p_spearman = spearmanr(traits[valid], neighbor_means[valid])
    w_knn = KNN(positions, k=4)
    moran = Moran(traits, w_knn)
    print(f"Korelacja Spearmana: ρ = {r_spearman:.3f}, p-value = {p_spearman:.3e}")
    print(f"Moran's I: {moran.I:.3f}, p-value = {moran.p_sim:3f}")

    frames_dir = 'frames'
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)

    for t in range(config.T + 1):
        pos, trait = trajectories[t]
        frame_filename = os.path.join(frames_dir, f"frame_{t:03d}.png")
        plot_population(t, pos, trait, save_path=frame_filename)

    lisa = Moran_Local(traits, w_knn, permutations=9999)
    generate_LISA_plot(lisa, traits, positions)
    create_gif_from_frames('frames', 'wzrost_roslin.gif')

def create_gif_from_frames(frames_dir, gif_filename, duration=0.5):
    """
    Łączy wszystkie obrazki z katalogu `frames_dir` w jeden plik GIF.
    Wymaga biblioteki imageio (pip install imageio).
    :param frames_dir: folder z plikami .png
    :param gif_filename: nazwa pliku wyjściowego GIF
    :param duration: czas wyświetlania jednej klatki w sekundach
    """
    import imageio
    import os

    # Sortujemy pliki po nazwach, żeby zachować kolejność generacji
    filenames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])

    with imageio.get_writer(gif_filename, mode='I', duration=duration) as writer:
        for file_name in filenames:
            path = os.path.join(frames_dir, file_name)
            image = imageio.v2.imread(path)
            writer.append_data(image)

    print(f"GIF został stworzony i zapisany jako '{gif_filename}'.")

if __name__ == "__main__":
    main()

