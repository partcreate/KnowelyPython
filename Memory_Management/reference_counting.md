Tut mir leid für mein Versäumnis. Hier ist der korrigierte Markdown-Code, bei dem der Fließtext ins Deutsche übersetzt wurde, während Code und technische Begriffe im Original belassen wurden.

-----

[](https://www.google.com/search?q=%23reference-counting)

## Referenzzählung

Anstatt nur ein Label für einen Wert zu sein, trägt jede Python-Variable auch eine Referenz auf ein Objekt (auch bekannt als ein *Pointer*). Um eine Referenz oder einen Speicherort zu finden, verwenden wir die eingebaute Funktion `id()`:

```python
age = 18 
print(id(age))      # 9789536
```

Referenzzählung markiert den Moment, in dem **der Pointer-Zähler eines Objekts null wird**, was dessen Löschung auslöst. Obwohl Python die Referenzzählung automatisch verwaltet, können wir die Funktion `getrefcount()` aus dem `sys`-Modul verwenden, um die Referenzanzahl eines Objekts zu überprüfen.

Sie gibt normalerweise einen Zähler zurück, der um `1` höher ist als erwartet, da sie eine temporäre Referenz als Argument für die Funktion beinhaltet. Zum Beispiel:

```python
from sys import getrefcount


print(getrefcount("Hello!"))		# 3
print(getrefcount(123))				# 7
print(getrefcount([1, 2, 3]))		# 1
```

Derzeit gibt es drei Referenzen auf den String `"Hello!"`, sieben auf die Ganzzahl `123` und eine auf die Liste `[1, 2, 3]`. Indem alle Variablen, die `"Hello!"` und `123` enthalten, auf denselben Speicherort verweisen, spart Python Rechenressourcen.

Da Listen veränderlich (*mutable*) sind, haben sie keinen festen Speicherort wie unveränderliche (*immutable*) Typen. Daher ist der Referenzzähler für die Liste `[1, 2, 3]` `1`, da nur einmal auf sie verwiesen wird, wenn die Funktion `getrefcount()` aufgerufen wird. Ein weiteres Beispiel:

```python
from sys import getrefcount

first_list = [1, 2, 3]				
print(getrefcount(first_list))			# 2

second_list = first_list
print(getrefcount(first_list))			# 3
```

Wenn wir eine Variable haben und sie an die Funktion `getrefcount()` übergeben, gibt es insgesamt `2` Referenzen. Aber sobald `first_list` in einer neuen Variable `second_list` gespeichert wird, steigt der Referenzzähler auf `3`. Hier ist ein ähnliches Beispiel mit einem unveränderlichen Datentyp:

```python
from sys import getrefcount

first_string = "I love Python!"
print(getrefcount(first_string))        # 4

second_string = first_string
print(getrefcount(first_string))        # 5
```

Dieses Verhalten ist typisch. Bei unveränderlichen Datentypen beginnt die Anzahl der Referenzen bei `3`, während sie bei veränderlichen Datentypen bei `1` beginnt.