# The `@pytest.mark.parametrize` Decorator

Parameterisierung beim Testen beinhaltet das **Ausführen desselben Tests mit verschiedenen Wertsätzen**, wobei jede Kombination als neuer Testfall betrachtet wird. In `pytest` erreichen wir dies mit dem `@pytest.mark.parametrize`-Decorator. So testet man die Funktion `sum_instances` aus der Datei `main.py` mit Parameterisierung:

```python
import pytest

from main import sum_instances


@pytest.mark.parametrize(
    "a,b,result",
    [
        ("Can", "Add", "CanAdd"),
        (2, 3, 5)
    ]
)
def test_can_sum(a: int | str, b: int | str, result: int | str) -> None:
    assert (
        sum_instances(a, b) == result
    ), f"Sum of {a} and {b} should be equal to {result}"
```

In diesem Fall können die Parameter `("Can", "Add", "CanAdd")` oder `(2, 3, 5)` sein. Jeder Test kann unabhängig fehlschlagen:

```
============================= test session starts ==============================
collecting ... collected 2 items

..\test_sum_instances.py::test_can_sum[Can-Add-CanAdd]        PASSED [ 50%]
..\test_sum_instances.py::test_can_sum[2-3-5]                  FAILED [100%]
test_sum_instances.py:5 (test_can_sum[2-3-5])
-1 != 5

Expected :5
Actual   :-1
<Click to see difference>

a = 2, b = 3, result = 5

...

..\test_sum_instances.py:18: AssertionError

============================== 1 failed, 1 passed in 0.08s ===============================
```

Der Standardtestname `test_can_sum[2-3-5]` ist nicht immer klar, weshalb eine Anpassung erforderlich ist. Wir können benutzerdefinierte Testnamen auf zwei Arten festlegen. Eine davon ist die Verwendung von `pytest.param` vor jeder Parametergruppe und das Hinzufügen von `id` als letzten Parameter:

```python
@pytest.mark.parametrize(
    "a,b,result",
    [
        pytest.param("Can", "Add", "CanAdd", id="2 strings"),
        pytest.param(2, 3, 5, id="2 numbers")
    ]
)
def test_can_sum(a: int | str, b: int | str, result: int | str) -> None:
    assert (
            sum_instances(a, b) == result
    ), f"Sum of {a} and {b} should be equal to {result}"
```

Die andere Möglichkeit besteht darin, einen zusätzlichen `ids`-Parameter für den `@pytest.mark.parametrize` bereitzustellen:

```python
import pytest

from main import sum_instances


@pytest.mark.parametrize(
    "a,b,result",
    [
        ("Can", "Add", "CanAdd"),
        (2, 3, 5)
    ],
    ids=[
        "2 strings",
        "2 numbers"
    ]
)
def test_can_sum(a: int | str, b: int | str, result) -> None:
    assert (
           sum_instances(a, b) == result
    ), f"Sum of {a} and {b} should be equal to {result}"
```

Das Ergebnis wird identisch sein:

```
============================= test session starts ==============================
collecting ... collected 2 items

..\test_sum_instances.py::test_can_sum[2 strings]             PASSED [ 50%]
..\test_sum_instances.py::test_can_sum[2 numbers]             FAILED [100%]

test_sum_instances.py:5 (test_can_sum[test can sum 2 numbers])
-1 != 5

Expected :5
Actual   :-1
<Click to see difference>

a = 2, b = 3, result = 5

...

..\test_sum_instances.py:18: AssertionError

============================== 1 failed, 1 passed in 0.08s ===============================
```