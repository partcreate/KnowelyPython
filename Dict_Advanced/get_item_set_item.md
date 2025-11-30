### `__setitem__()` and `__getitem__()`

Die `__getitem__()`-Methode ist eine "magische Methode", die einen Wert über einen Schlüssel abruft, ähnlich wie wenn
man bei einem Dictionary mit eckigen Klammern auf einen Schlüssel zugreift. Hier ist ein Beispiel, das diese Aktion auf
verschiedene Weisen zeigt:

```python
my_dictionary = {"one": 1, "two": 2}

my_dictionary["one"]                 # 1
my_dictionary.__getitem__("one")  # 1
```

`__setitem__()` ist auch eine "magische Methode"; sie erlaubt es, Werte über einen Schlüssel in das Dictionary zu
schreiben:

```python
my_dictionary = {"one": 1, "two": 2}

my_dictionary["three"] = 3
my_dictionary.__setitem__("four", 4)
```

Die algorithmische Komplexität der `__setitem__()`- und `__getitem__()`-Methoden ist `O(1)`.