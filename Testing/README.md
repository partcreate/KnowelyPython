
[](https://www.google.com/search?q=%23testing-in-python)

# Testen in Python

Heute werfen wir einen Blick auf die Arten von Tests, die in Python verfügbar sind.

-----

[](https://www.google.com/search?q=%23automated-vs-manual-testing)

## Automatisierte vs. manuelle Tests

Bei manuellen Tests führen wir unseren Code mit verschiedenen Parametern aus und beobachten die Ergebnisse. Je nachdem, wie gründlich wir sein müssen, müssen wir möglicherweise alle App-Funktionen, mögliche Eingaben und das erwartete Ergebnis auflisten. Nach jeder Code-Änderung sollten wir jeden aufgeführten Punkt überprüfen. **Automatisierte Tests vereinfachen diesen Prozess**, indem sie den Testplan über Skripte ausführen, was Python standardmäßig ermöglicht.

-----

[](https://www.google.com/search?q=%23the-assert-statement)

## Die `assert`-Anweisung

Die `assert`-Anweisung ist das einfachste Testwerkzeug in Python. Wenn unser Code fehlerfrei ist, ist die Bedingung `True`, andernfalls ist sie `False`. Wir können nach der Bedingung eine Ausnahmenachricht hinzufügen, die durch ein Komma getrennt ist:

```python
def sum_instances(a: int | str, b: int | str) -> int | str:
    if isinstance(a, int) and isinstance(b, int):
        return a - b  # here we made an error to look how our tests work
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    return a + b


def test_can_sum_2_strings() -> None:
    assert (
            sum_instances("Can", "Add") == "CanAdd"
    ), "Sum of 'Can' and 'Add' should be equal to 'CanAdd'"


def test_can_sum_2_numbers() -> None:
    assert (
            sum_instances(2, 3) == 5
    ), "Sum of 2 and 3 should be equal to 5"


if __name__ == "__main__":
    test_can_sum_2_strings()
    print("'test_can_sum_2_strings' success")
    test_can_sum_2_numbers()
    print("'test_can_sum_2_numbers' success")
```

Das Ergebnis ist:

```python
'test_can_sum_2_strings' success
Traceback (most recent call last):
  File "...\main.py", line 24, in <module>
    test_can_sum_2_numbers()
  File "...\main.py", line 16, in test_can_sum_2_numbers
    assert (
AssertionError: Sum of 2 and 3 should be equal to 5
```

Hier haben wir versucht, eine eigene Testschnittstelle zu erstellen, aber es gibt bereits viele ausgezeichnete Tools für automatisierte Tests. Apropos...