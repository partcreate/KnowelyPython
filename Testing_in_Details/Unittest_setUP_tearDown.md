[](https://www.google.com/search?q=%23testing-in-detail)

# Testing in Detail

Ein Test prüft das Ergebnis eines bestimmten Verhaltens und stellt sicher, dass das Ergebnis mit der Erwartung übereinstimmt. "Verhalten" bezeichnet die Art und Weise, wie ein System auf eine bestimmte Situation reagiert. Wie oder warum etwas getan wird, ist jedoch nicht so wichtig wie das, was getan wurde.

Ein Test besteht aus den folgenden Schritten:

1.  **Arrange/Setup** — Hier bereiten wir alles für unseren Test vor:
      * Objekte
      * Starten/Beenden von Diensten
      * Eingabe von Datensätzen in eine Datenbank
      * Erstellung von Anmeldeinformationen für einen noch nicht existierenden Benutzer.
2.  **Act** ist die Aktion, die das zu testende Verhalten auslöst, normalerweise eine Funktion oder eine Methode.
3.  **Assert** — Hier überprüfen wir das Ergebnis und stellen sicher, dass es wie erwartet funktioniert.
4.  **Cleanup/Teardown** — Hier räumt der Test nach sich selbst auf, um eine versehentliche Beeinflussung anderer Tests zu vermeiden.

Der Test wird in den Schritten **Act** und **Assert** ausgeführt, nachdem der **Arrange**-Schritt den Kontext vorbereitet hat. Das Verhalten findet zwischen **Act** und **Assert** statt. *Arrange/Setup* und *Cleanup/Teardown* sind optionale Schritte.

-----

[](https://www.google.com/search?q=%23organizing-unittest-code)

## Organizing Unittest Code

Hier sehen wir uns an, wie die Schritte **Arrange** und **Cleanup** im `unittest`-Framework durchgeführt werden.

-----

[](https://www.google.com/search?q=%23setup-and-teardown)

### `setUp()` und `tearDown()`

Die Methode `setUp()` wird **vor** der Testmethode aufgerufen, um den Test vorzubereiten. Jede Ausnahme (außer `AssertionError` oder `SkipTest`-Ausnahmen), die von `setUp()` ausgelöst wird, wird als Fehler und nicht als Testfehler betrachtet.

Die Methode `tearDown()` wird **nachdem** die Testmethode aufgerufen wurde und ihr Ergebnis gespeichert wurde, aufgerufen. Sie wird auch dann aufgerufen, wenn die Testmethode eine Ausnahme auslöst, sodass die Implementierung in Unterklassen besonders vorsichtig bei der Überprüfung des internen Zustands sein muss.

Hier ist ein Beispiel für die Verwendung der Methoden `setUp()` und `tearDown()`.

Die Datei `main.py`:

```python
class Person:
	def __init__(self, name: str, surname: str, age: int):
		self.name = name
		self.surname = surname
		self.age = age


	def personal_info(self) -> str:
		return f"{self.name} {self.surname} (age: {self.age})"
	
	def adult_info(self) -> str:
		if self.age < 18:
			return f"{self.name} is not an adult"
		return f"{self.name} is an adult"
```

Die Datei `test_main.py`:

```python
from unittest import TestCase

from main import Person

class TestPerson(TestCase):
	def setUp(self) -> None:
		"""this code will run before each test"""
		print("test started")
		self.person = Person(name="John", surname="Smith", age=20)
	
	def tearDown(self) -> None:
		"""this code will run after each test"""
		print("test finished")
	
	def test_adult_info(self):
		self.person.age = 15 # When we change self.person.age here, it will not touch other tests
		assert self.person.adult_info() == "John is not an adult"
	
	def test_personal_info(self):
		assert self.person.personal_info() == "John Smith (age: 20)"
```

Das Ergebnis dieser Tests ist:

```
============================= test session starts =============================
collecting ... collected 2 items

test_main.py::TestPerson::test_adult_info
test_main.py::TestPerson::test_personal_info

============================== 2 passed in 0.03s ==============================

Process finished with exit code 0
PASSED [ 50%]test started
test finished
PASSED [100%]test started
test finished
```

-----

[](https://www.google.com/search?q=%23setupclass-and-teardownclass)

### `setUpClass()` und `tearDownClass()`

Die Methode `setUpClass()` wird **bevor** alle Tests in einer einzelnen Klasse ausgeführt wurden, aufgerufen.

Die Methode `tearDownClass()` wird **nachdem** alle Tests in einer einzelnen Klasse ausgeführt wurden, aufgerufen.

> 💡 Sowohl `setUpClass()` als auch `tearDownClass()` werden mit der Klasse als einzigem Argument aufgerufen und müssen als `classmethod()` deklariert werden.

Betrachten wir ein Beispiel:

```python
# test_main.py
from unittest import TestCase

from main import Person

class TestPerson(TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		"""this code will run before all tests"""
		print("tests started")
		cls.person = Person(name="John", surname="Smith", age=20)
	
	@classmethod
	def tearDownClass(cls) -> None:
		"""this code will run after all tests"""
		print("all tests are finished")
	
	def test_adult_info(self):
		self.person.age = 15 # When we cange self.person.age here, test_personal_info will not pass
		assert self.person.adult_info() == "John is not an adult"
	
	def test_personal_info(self):
		assert self.person.personal_info() == "John Smith (age: 20)"
```

Das Ergebnis dieser Tests ist:

```
============================= test session starts =============================
collecting ... collected 2 items

test_main.py::TestPerson::test_adult_info
test_main.py::TestPerson::test_personal_info tests started
PASSED [ 50%]
FAILED [100%]
test_main.py:22 (TestPerson.test_personal_info)
'John Smith (age: 15)' != 'John Smith (age: 20)'
...
test_main.py:24: AssertionError
all tests are finished

========================= 1 failed, 1 passed in 0.16s =========================
```

⚠️ Dieses Beispiel ist keine bewährte Vorgehensweise, bitte vermeiden Sie es, Daten aus der Methode `setUpClass()` zu ändern.