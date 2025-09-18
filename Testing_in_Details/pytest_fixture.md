[](https://www.google.com/search?q=%23organizing-pytest-code)

## Pytest-Code organisieren

Hier werden wir uns ansehen, wie die Schritte **Arrange** und **Cleanup** im `pytest`-Framework durchgeführt werden.

-----

[](https://www.google.com/search?q=%23set-up-fixture-in-pytest)

### Fixture-Setup in Pytest

Wir können `pytest` mitteilen, dass eine bestimmte Funktion eine Fixture ist, indem wir sie mit `@pytest.fixture` dekorieren.

Diese **Fixture ermöglicht es uns, einen generischen Setup-Schritt zu definieren**, der immer wieder verwendet werden kann, genau wie eine normale Funktion. Zwei verschiedene Tests können dieselbe Fixture anfordern und unterschiedliche Ergebnisse von dieser Fixture erhalten. Das ist dasselbe wie mit `setUp()` aus dem `unittest`, aber Sie können definieren, welche Fixture Sie akzeptieren müssen, um die Funktion zu testen.

Hier ist ein Beispiel:

```python
# test_main.py
import pytest

from main import Person


@pytest.fixture()
def person_template():
	return Person(name="John", surname="Smith", age=20)


# Um dem Test die Annahme von Fixtures zu ermöglichen, müssen wir die Fixtures als Parameter in der Testfunktion auflisten.
def test_adult_info(person_template):
	person_template.age = 15
	assert person_template.adult_info() == "John is not adult"


 # Um dem Test die Annahme von Fixtures zu ermöglichen, müssen wir die Fixtures als Parameter in der Testfunktion auflisten.
def test_personal_info(person_template):
	assert person_template.personal_info() == "John Smith (age: 20)"
```

Tests müssen nicht auf eine einzige Fixture beschränkt sein – sie können von so vielen Fixtures abhängen, wie Sie benötigen, und Fixtures können auch andere Fixtures verwenden.

-----

[](https://www.google.com/search?q=%23cleanupteardown-in-pytest)

### Cleanup/Teardown in Pytest

Fixtures in `pytest` bieten ein vorteilhaftes Teardown-System, das es uns ermöglicht, die Schritte für jede Fixture zu definieren, um sich selbst aufzuräumen.

Dazu verwenden Sie die `yield`-Anweisung anstelle der `return`-Anweisung. Führen Sie mit diesen Fixtures Code aus und geben Sie ein Objekt an die anfordernde Fixture oder den Test zurück, genau wie bei den anderen Fixtures. Die Unterschiede sind:

  * `return` wird durch `yield` ersetzt
  * jeglicher Teardown-Code für diese Fixture wird nach `yield` platziert.

Wie funktioniert das? Zuerst ermittelt `pytest` eine Reihenfolge für die Fixtures. Dann wird jede von ihnen ausgeführt, bis sie zurückgibt (`return`) oder freigibt (`yield`). Schließlich geht es zur nächsten Fixture in der Liste, um dasselbe zu tun.

Wenn der Test beendet ist, kehrt `pytest` zur Liste der Fixtures zurück, aber in umgekehrter Reihenfolge. Es nimmt jede, die freigegeben wurde, und führt den Code aus, der sich nach der `yield`-Anweisung befand. Beispiel:

```python
# test_main.py
import pytest

from main import Person


@pytest.fixture()
def person_template():
	yield Person(name="John", surname="Smith", age=20)
	print("test finished")  # Wird nach jedem Test ausgegeben.


def test_adult_info(person_template):
	person_template.age = 15
	assert person_template.adult_info() == "John is not adult"


def test_personal_info(person_template):
	assert person_template.personal_info() == "John Smith (age: 20)"
```

-----

[](https://www.google.com/search?q=%23fixture-scope)

### Fixture-Gültigkeitsbereich

Wir können das vorherige Beispiel erweitern und den Parameter `scope="module"` zum Aufruf von `@pytest.fixture` hinzufügen, um zu bewirken, dass eine `person_template`-Fixture-Funktion nur einmal pro Testmodul aufgerufen wird (der Standard ist `scope="function"` – einmal pro Testfunktion). Dann verhält sich die Fixture genauso wie die Methoden `setUpClass()` und `tearDownClass()` in `unittest`. Mögliche Werte für den Gültigkeitsbereich sind:

  * `function`
  * `class`
  * `module`
  * `package`
  * `session`.

Fixtures werden erstellt, wenn sie zuerst von einem Test angefordert werden, und werden basierend auf ihrem Gültigkeitsbereich zerstört:

  * `function`: Der Standard-Gültigkeitsbereich; die Fixture wird am Ende der Testfunktion zerstört.
  * `class`: Die Fixture wird während des Teardowns des letzten Tests in der Klasse zerstört.
  * `module`: Die Fixture wird während des Teardowns des letzten Tests im Modul zerstört.
  * `package`: Die Fixture wird während des Teardowns des letzten Tests im Paket zerstört.
  * `session`: Die Fixture wird am Ende der Testsitzung zerstört.

Betrachten wir ein Beispiel:

```python
# test_main.py
import pytest

from main import Person


@pytest.fixture(scope="module")
def person_template():
	yield Person(name="John", surname="Smith", age=20)
	print("all tests are finished")    # Wird nach allen Tests ausgegeben.


def test_adult_info(person_template):
	person_template.age = 15    # Wenn wir hier self.person.age ändern, wird test_personal_info nicht bestehen
	assert person_template.adult_info() == "John is not adult"


def test_personal_info(person_template):
	assert person_template.personal_info() == "John Smith (age: 20)"
```

-----

[](https://www.google.com/search?q=%23pytest-monkeypatch)

### Pytest Monkeypatch

`pytest` bietet auch den Mocking-Mechanismus `monkeypatch` an, der ein Analogon zu `unittest.mock` ist. Hier ist ein Beispiel für eine `main.py`-Datei:

```python
import os


def get_current_path():
	current_path = os.getcwd()
	return current_path  # Gibt das aktuelle Verzeichnis zurück
```

Eine `test_main.py`-Datei:

```python
import os

from main import get_current_path


def test_get_current_directory(monkeypatch):

	def mock_getcwd():
		return '/data/user/directory123'

	monkeypatch.setattr(os, 'getcwd', mock_getcwd)  # Mockt das Ergebnis von os.getcwd()
	assert get_current_path() == '/data/user/directory123'
```