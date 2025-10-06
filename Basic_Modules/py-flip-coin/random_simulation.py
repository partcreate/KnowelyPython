import random
import matplotlib.pyplot as plt

# Parameter der Simulation
NUM_FLIPS = 10          # N (Würfe pro Runde)
NUM_REPETITIONS = 10000 # R (Anzahl der Runden)

# Liste für die Ergebnisse der 10.000 Runden
results = []

# Führe 10.000 Runden durch
for _ in range(NUM_REPETITIONS):
    heads_in_round = 0

    # Simuliere 10 Münzwürfe
    for _ in range(NUM_FLIPS):
        # random.randint(0, 1) liefert 0 (Zahl) oder 1 (Kopf) mit p=0.5
        heads_in_round += random.randint(0, 1)

    # Füge die Gesamtanzahl der Köpfe zur Ergebnisliste hinzu
    results.append(heads_in_round)

# Visualisierung des Histogramms (Häufigkeitsverteilung)
plt.figure(figsize=(8, 5))
# Wir nutzen Bins 0 bis 11, um die Ergebnisse 0 bis 10 darzustellen
bins = range(NUM_FLIPS + 2)
plt.hist(results, bins=bins, align='left', rwidth=0.8, color='green', edgecolor='black')

plt.title(f'Empirische Binomialverteilung (Simulation)')
plt.xlabel('Anzahl der Köpfe (k)')
plt.ylabel('Häufigkeit der Beobachtung')
plt.xticks(range(NUM_FLIPS + 1))

plt.savefig('coin_flip_simulation_random.png')
print("Simulation erfolgreich durchgeführt und Graph als 'coin_flip_simulation_random.png' gespeichert.")

print(f"Simulierter Mittelwert: {sum(results) / NUM_REPETITIONS:.2f}")