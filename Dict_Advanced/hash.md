
## Hash

Um zu verstehen, warum Dictionaries so schnell arbeiten, müssen wir die **Hash-Funktion**, die **Hash-Tabelle**, **Kollisionen**, die **Größenanpassung der Tabelle (table resizing)** sowie die Magic-Methoden **`__getitem__`** und **`__setitem__`** besprechen.

[](#hash-function)

### Hash-Funktion

Eine Hash-Funktion akzeptiert ein Objekt und gibt einen numerischen Wert zurück – die eingebaute Python-Funktion `hash()` führt dieses Hashing durch. Für eine ganze Zahl gibt die Hash-Funktion die Zahl selbst zurück:

```python
print(hash(1))		# 1
print(hash(2))		# 2
print(hash(33)) 	# 33
```

Der Hash-Wert von `-1` ist `-2`. Dies ist eine Ausnahme, da `-1` ein reservierter Wert ist, um zu verhindern, dass Hash-Funktionen einen Hash-Wert von `-1` erzeugen:

```python
print(hash(-1))		# -2
```

Die Hash-Funktion für boolesche Werte gibt `1` für `True` und `0` für `False` zurück, da `True` äquivalent zur ganzen Zahl `1` und `False` zu `0` ist:

```python
print(hash(True))	# 1
print(hash(False))	# 0
```

Für andere unveränderliche (immutable) Datentypen ändert sich der Hash-Wert bei jedem Programmlauf:

```python
print(hash("a"))	    # -5691950878225878745
print(hash("Sun"))	    # -4125737227946105794
print(hash(1.23))	    # 530343892119149569

print(hash(None))	    # 269828332
print(hash((1,)))	    # -6644214454873602895
print(hash((1, "a")))	# 8571628832376313798
```

In diesen Beispielen haben wir Hash-Werte nur für unveränderliche Datentypen gezeigt, und das aus gutem Grund, denn wenn wir versuchen, einen veränderlichen (mutable) Typ zu hashen, tritt ein Fehler auf:

```python
print(hash([1, 2, 3]))

>> TypeError: unhashable type: "list"
```

**Wir können den Hash-Wert für `list`, `dict` und `set` nicht erhalten**, da nur hashbare Objekte gehasht werden können und im Allgemeinen nur unveränderliche Datentypen hashbar sind. Es gibt jedoch Ausnahmen. Eine davon ist, wenn ein unveränderliches `tuple` einen veränderlichen Wert enthält, z. B.:

```python
print(hash((4, [1, 2, 3])))

>> TypeError: unhashable type: "list"
```

Der zweite Fall ist ein Hash für ein Klassenobjekt:

```python
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


first_user = User("Mariia", 19)
print(hash(first_user))		# 271734727
```

Übrigens gibt es in der Klasse eine Methode `__hash__()`, die der Funktion `hash()` entspricht:

```python
print(hash(first_user))			# 271734727
print(first_user.__hash__())		# 271734727
```

Wenn wir jedoch die Hash-Funktion für die Klasse selbst anstelle einer Instanz aufrufen, funktioniert die Funktion, aber die Methode `__hash__()` wird nicht aufgerufen:

```python
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


print(hash(User))		# 312353220	
print(User.__hash__())	
# TypeError: descriptor "__hash__" of "object" object needs an argument
```

Zusammenfassend lassen sich einige Merkmale der Hash-Funktion festhalten:

  * Die Ausführungszeit der Hash-Funktion ist konstant — `O(1)`.
  * Die Hash-Funktion gibt für dieselben Objekte immer dieselben Werte zurück:

<!-- end list -->

```python
print(hash("Hello, World!"))	# 5815467602854934636		
print(hash("Hello, World!"))	# 5815467602854934636
print(hash(1.25))		        # 576460752303423489
print(hash(1.25))		        # 576460752303423489
```

```
```