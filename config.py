# Parametry modelu

L = 100  # rozmiar przestrzeni
N_0 = 150 # rozmiar populacji
T = 100  # liczba kroków czasowych
r_interact = 5 # promień wpływu sąsiedztwa na wzrost
r_0 = 0.5  # początkowe tempo wzrostu
alpha = 0.5  # siła hamowania wzrostu (im więcej sąsiadów, tym wolniejszy wzrost)
mutation_strength = 0.05 # szum
clusters = 3 # liczba klastrów w rozmieszczeeniu zklastrowanym
initial_size = 0.7 # początkowy rozmiar
random_population = True # jeśli true - rozmieszczenie losowe, jeśli false - zklastrowane