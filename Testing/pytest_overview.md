
[](https://www.google.com/search?q=%23the-pytest-framework)

## Das `pytest`-Framework

`pytest` ist ein Python-Framework zum Schreiben und Ausführen von Tests. Wir können es mit `pip install pytest` installieren und mit oder ohne Angabe eines Dateinamens ausführen. Wenn ein Dateiname angegeben ist, wird nur diese Datei getestet. Andernfalls findet und führt `pytest` automatisch alle Dateien namens `test_*.py` oder `*_test.py` im aktuellen Verzeichnis und in Unterverzeichnissen aus. Dieser Vorgang wird als **Test-Sammlung** bezeichnet.

Damit `pytest` Funktionen als Tests erkennt, müssen ihre Namen mit `test` beginnen. Funktionen mit anderen Namen werden nicht als Tests betrachtet. Hier ist ein Beispiel:

```python
from main import sum_instances


def test_can_sum_2_strings() -> None:
    assert (
        sum_instances("Can", "Add") == "CanAdd"
    ), "Sum of 'Can' and 'Add' should be equal to 'CanAdd'"

def test_can_sum_2_numbers() -> None:
    assert (
            sum_instances(2, 3) == 5
    ), "Sum of 2 and 3 should be equal to 5"
```

Lassen Sie uns `pytest` ausführen:

```python
(venv) .../py-testing> pytest
============================= test session starts ==============================
platform win32 -- Python 3.10.4, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: .../py-testing
collected 2 items

test_sum_instances.py .F                                                 [100%] 

E       AssertionError: Sum of 2 and 3 should be equal to 5
E       assert -1 == 5
E        +  where -1 = sum_instances(2, 3)

test_sum_instances.py:13: AssertionError
=========================== short test summary info ============================
FAILED test_sum_instances.py::TestSum::test_can_sum_2_numbers - AssertionError: Sum of 2 and 3 should be equal to 5
```

Ich hoffe, diese Ausgabe entspricht nun vollständig Ihren Erwartungen. Wenn Sie weitere Konvertierungen benötigen, stehe ich gerne zur Verfügung.