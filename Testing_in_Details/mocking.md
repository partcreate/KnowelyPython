[\<a href="\#mocking" target="\_self"\>Mocking\</a\>]

## Mocking

Ein Mock-Objekt ersetzt und imitiert ein echtes Objekt während des Tests. Es ist ein flexibles und leistungsstarkes Werkzeug zur Verbesserung der Testqualität.

[\<a href="\#magicmock" target="\_self"\>MagicMock\</a\>]

### MagicMock

`unittest.mock` ist die Bibliothek für Mocking in Python. Sie bietet eine einfache Möglichkeit, Mocks in Ihre Tests einzuführen. Zum Beispiel, die Datei `main.py`:

:

```python
import time

def delay(seconds: int, func):
	time.sleep(seconds)
	return func()
```

Die Datei `test_main.py`:

```python
from unittest import mock

from main import delay

def test_function_has_called():
	mock_function = mock.MagicMock()
	delay(3, mock_function)
	mock_function.assert_called_once()
```

[\<a href="\#mocking-with-an-unittest-mockpatch" target="\_self"\>Mocking With an Unittest `mock.patch`\</a\>]

### Mocking With an Unittest `mock.patch`

`unittest.mock` bietet ein leistungsstarkes Werkzeug zum Mocken von Objekten: `patch()`. Es sucht ein Objekt im ausgewählten Modul und ersetzt dieses Objekt durch einen Mock.

Normalerweise verwenden wir `patch()` als **Decorator** oder als **Context Manager**, um einen Bereich bereitzustellen, in dem Sie das Zielobjekt mocken können.

Wenn Sie ein Objekt für die Dauer Ihrer gesamten Testfunktion mocken möchten, können Sie `patch()` als **Funktions-Decorator** verwenden.

Ein Beispiel für die Verwendung von `patch()`:

```python
# test_main.py
from unittest import mock

from main import delay

@mock.patch("time.sleep")
def test_function_has_called(mocked_sleep):
	delay(100, lambda: None)
	mocked_sleep.assert_called_once_with(100)
```

[\<a href="\#mocking-with-a-context-manager" target="\_self"\>Mocking With a Context Manager\</a\>]

### Mocking With a Context Manager

Manchmal müssen Sie `patch()` als Context Manager anstelle eines Decorators verwenden, zum Beispiel wenn:

  * Sie ein Objekt nur für einen Teil des Testbereichs mocken möchten.
  * Sie bereits zu viele Decorators oder Parameter verwenden, was die Lesbarkeit des Tests beeinträchtigt.

Beispiel:

```python
from unittest import mock

from main import delay

def test_function_has_called():
    with mock.patch("time.sleep") as mocked_sleep:
        delay(100, lambda: None)
        mocked_sleep.assert_called_once_with(100)
```