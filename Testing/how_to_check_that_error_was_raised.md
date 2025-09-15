
### Die `pytest.raises`-Methode

Um zu testen, ob unser Code die korrekte Ausnahme auslöst, verwenden wir `pytest.raises` als Kontextmanager. Dieser fängt die Ausnahme des angegebenen Typs ab:

```python
def sum_instances(a: int | str, b: int | str) -> int | str:
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    return a + b
```

Testen wir, ob ein `TypeError` ausgelöst wird, wenn keine gültigen Daten bereitgestellt werden:

```python
import pytest

from main import sum_instances

def test_cannot_add_int_and_str() -> None:
    with pytest.raises(TypeError):
        sum_instances(2, "3")


def test_cannot_add_2_lists() -> None:
    with pytest.raises(TypeError):
        # but it will not rise TypeError, because actually we can use ‘+’ with lists
        sum_instances([2], ["3"])  
```

...und führen wir `pytest` aus:

```python
(venv) .../py-testing> pytest
=============================== test session starts ===============================
platform win32 -- Python 3.10.4, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: .../py-testing
collected 2 items                                                                 

test_sum_instances.py .F                                                  [100%]

===================================== FAILURES =====================================
____________________________________ test_error ____________________________________

    def test_error():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

test_sum_instances.py:24: Failed
=========================== short test summary info ============================
FAILED test_sum_instances.py::test_error - Failed: DID NOT RAISE <class 'Type...
========================= 1 failed, 1 passed in 0.07s ========================= 
```