
## `dataclasses`

Das `dataclasses`-Modul bietet einen Dekorator und Funktionen zur automatischen Ergänzung von generierten speziellen Methoden wie `__init__()` und `__repr__()` zu benutzerdefinierten Klassen. Wir können das `dataclasses`-Modul mit folgendem Code importieren:

```python
import dataclasses
```

Das `dataclasses`-Modul vereinfacht die Arbeit mit Datencontainer-Klassen, indem es Boilerplate-Code reduziert und Objekte in einem lesbaren Format darstellt. Mit seinem Dekorator, `@dataclass`, können wir eine einfache Klasse erstellen:

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

Erstellung derselben Klasse unter Verwendung des `@dataclass`-Dekorators aus dem `dataclasses`-Modul:

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
```

Typ-Annotationen sind erforderlich; Felder ohne sie werden ignoriert. Wir können einen spezifischen Typ oder `Any` aus `typing` verwenden. Dies gibt uns automatisch die `Person`-Klasse mit implementierten Methoden `__init__()`, `__repr__()`, `__str__()` und `__eq__()`. Es bleibt eine reguläre Klasse, sodass wir davon erben, Methoden hinzufügen und Standardwerte festlegen können:

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Student(Person):
    marks: List[int]
    has_scholarship: bool = False
```

⚠️ Alle Attribute mit Standardwerten müssen am Ende platziert werden. Die Reihenfolge ist wichtig\!

```
```