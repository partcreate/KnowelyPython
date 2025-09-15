Okay, ich konvertiere den Code jetzt für dich.

-----

## Das `unittest`-Framework

`unittest` ist ein integriertes Python-Test-Framework mit folgenden zentralen Anforderungen:

  - Es ist klassenbasiert: Tests müssen in Klassen platziert werden, die von `unittest.TestCase` erben.
  - Statt des eingebauten `assert`-Statements verwenden wir die `unittest.TestCase`-Assertionsmethoden.

Wir können das vorherige Beispiel in wenigen Schritten in einen `unittest`-Testfall umwandeln:

1.  Importiere `unittest` aus der Standardbibliothek.
2.  Erstelle eine Klasse `TestSum`, die von `TestCase` erbt.
3.  Wandle die Testfunktionen in Methoden um, indem du `self` als erstes Argument hinzufügst.
4.  Verwende `self.assertEqual()` für die Überprüfungen.
5.  Ändere den Befehlszeileneinstiegspunkt, um `unittest.main()` aufzurufen.

Lass uns dieselbe Funktion aus der Datei `main.py` testen:

```python
def sum_instances(a: int | str, b: int | str) -> int | str:
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    return a + b
```

…und die Datei `test_sum_instances.py` erstellen:

```python
import unittest

from main import sum_instances


class TestSum(unittest.TestCase):

    def test_can_sum_2_strings(self) -> None:
        self.assertEqual(
            sum_instances("Can", "Add"),
            "CanAdd",
            "Sum of 'Can' and 'Add' should be equal to 'CanAdd'"
        )

    def test_can_sum_2_numbers(self) -> None:
        self.assertEqual(
            sum_instances(2, 3),
            5,
            "Sum of 2 and 3 should be equal to 5"
        )


if __name__ == "__main__":
    unittest.main()
```

Wenn wir dies im Terminal ausführen, erhalten wir eine Erfolgsmeldung (gekennzeichnet durch einen Punkt) oder eine Fehlermeldung (gekennzeichnet durch ein F):

```python
(venv) .../py-testing> python test_sum_instances.py
F.
======================================================================
FAIL: test_can_sum_2_numbers (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "...\test_sum_instances.py", line 16, in test_can_sum_2_numbers
    self.assertEqual(
AssertionError: -1 != 5 : Sum of 2 and 3 should be equal to 5

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

Wir haben soeben zwei Tests mit dem `unittest`-Test-Runner ausgeführt.