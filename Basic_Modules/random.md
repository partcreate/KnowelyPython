## `random`

Das in Python integrierte Modul `random` ermöglicht es uns, Zufallszahlen auszugeben; wir importieren es wie folgt:

```python
import random
```

Einige Funktionen aus dem Modul:

  * `random.randint()` — gibt eine Zufallszahl aus dem angegebenen Bereich zurück.
  * `random.choice()` — gibt ein zufälliges Element aus der angegebenen Sequenz zurück.
  * `random.choices()` — gibt eine Liste zufälliger Auswahlen aus der angegebenen Sequenz zurück.
  * `random.shuffle()` — gibt die angegebene Sequenz in zufälliger Reihenfolge zurück.

Betrachten wir einige Beispiele:

```python
import random

fruits = ["apple", "banana", "orange", "pear", "strawberry", "raspberry"]

print(random.randint(100, 120))	 	# 103
print(random.choice(fruits))		# pear
print(random.choices(fruits))		# ['apple']

random.shuffle(fruits)		
print(fruits)				 	 	# ['strawberry', 'raspberry', 'apple', 'pear', 'banana', 'orange']
```

Eine weitere nützliche Funktion im Modul `random` ist `seed()`. Sie initialisiert den Zufallszahlengenerator und stellt sicher, dass die Zufallszahlen beim Neustart des Codes konsistent bleiben:

```python
import random


random.seed(5)
for _ in range(3):
	print(random.randint(0, 100))
```

Beim ersten Ausführen dieses Codes wird die Ausgabe sein:

```
3
56
27
```

...und wenn wir ihn erneut ausführen, wird sich die Ausgabe nicht ändern\!

```
```