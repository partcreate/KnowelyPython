
## `decimal`

Das `decimal`-Modul unterstützt gerundete dezimale Gleitkomma-Arithmetik schnell und genau. Es bietet mehr Präzision und einen kleineren Bereich als der `float`-Typ. Wir können das `decimal`-Modul mit dem folgenden Code importieren:

```python
import decimal
```

Manche Floats können nicht exakt binär dargestellt werden, aber `Decimal`-Zahlen verhalten sich wie echte Dezimalzahlen. Um eine Dezimalzahl zu speichern, verwenden wir die `Decimal`-Klasse. Hier ist ein Beispiel für die Verwendung von `float`-Zahlen:

```python
print(0.1+0.2)			  # 0.3000000000000004
print(0.1+0.2 == 0.3)		# False
```

...und ein Beispiel für die Verwendung von `Decimal`-Zahlen:

```python
from decimal import Decimal

print(Decimal("0.1")+Decimal("0.2"))				  # Decimal("0.3")
print((Decimal("0.1")+Decimal("0.2")) == Decimal("0.3"))	# True
```

Wie gezeigt, haben wir den String an die `Decimal`-Klasse übergeben, weil endliche Dezimalbrüche in binärer Form unendlich sein können, was zu Rundungen und Genauigkeitsverlust führen kann. Die Übergabe eines Strings verhindert diesen Fehler:

```python
print(Decimal(0.1))		    # 0.1000000000000000055511151231257827021181583404541
print(Decimal("0.1"))		# 0.1
```