import math
import matplotlib.pyplot as plt

# 1. Parameter definieren
N = 10  # Anzahl der Münzwürfe
p = 0.5  # Wahrscheinlichkeit für Kopf

# Liste der möglichen Ergebnisse (k=0 bis k=10)
k_werte = list(range(N + 1))
wahrscheinlichkeiten = []

# 2. Schleife: Berechnung für alle k
for k in k_werte:
    # A. Binomialkoeffizient (Reihenfolgen)
    koeffizient = math.comb(N, k)

    # B. Wahrscheinlichkeit der Erfolge (p hoch k)
    erfolge = p ** k

    # C. Wahrscheinlichkeit der Misserfolge ((1-p) hoch (N-k))
    misserfolge = (1 - p) ** (N - k)

    # D. Gesamtwahrscheinlichkeit P(X=k)
    p_k = koeffizient * erfolge * misserfolge
    wahrscheinlichkeiten.append(p_k)

# 3. Das Ergebnis für k=0
p_zero = wahrscheinlichkeiten[0]
print(f"Die theoretische Wahrscheinlichkeit für genau 0 Köpfe (k=0) ist: {p_zero:.8f}")

# 4. Visualisierung der theoretischen Verteilung
plt.figure(figsize=(8, 5))
plt.bar(k_werte, wahrscheinlichkeiten, color='darkred', edgecolor='black')
plt.title(f'Theoretische Binomialverteilung N={N}, p={p}')
plt.xlabel('Anzahl der Köpfe (k)')
plt.ylabel('Wahrscheinlichkeit P(X=k)')
plt.xticks(k_werte)
plt.grid(axis='y', alpha=0.5)

plt.savefig('binomial_theory_graph.png')
print("Der theoretische Graph wurde als 'binomial_theory_graph.png' gespeichert.")