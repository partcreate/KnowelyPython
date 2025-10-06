
## `sys`

Python verfügt über das eingebaute Modul **`sys`**, das eine Schnittstelle zur teilweisen Interaktion mit dem Python-Interpreter bietet. Wir importieren das Modul `sys` auf folgende Weise:

```python
import sys
```

Zu den `sys`-Funktionen gehört **`sys.getrefcount()`**, das die Anzahl der Referenzen auf eine Variable zurückgibt. **`sys.argv`** hingegen liefert eine Liste der an ein Python-Skript übergebenen Kommandozeilenargumente, wobei der erste Wert immer der Name des Skripts ist. Hier ist der Eingabecode:

```python
import sys

print(sys.argv)
```

Hier ist das Ergebnis:

```
["/Users/User/Desktop/pythonProject/main.py"]
```

Alle Argumente, die wir an das Skript übergeben, werden als Typ **`str`** gespeichert.

```
```