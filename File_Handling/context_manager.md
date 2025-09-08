Super\! Hier ist der konvertierte Markdown-Code aus dem von Ihnen bereitgestellten HTML.

[](https://www.google.com/search?q=%23context-managers-in-files)

## Context Managers in Files

Wenn wir vergessen, eine Datei nach dem Öffnen zu schließen, kann dies zu Problemen führen, die Python mit Kontext-Managern verhindern kann. Bei Verwendung der `with`-Anweisung schließen Kontext-Manager die Datei automatisch, wenn der Geltungsbereich verlassen wird, zum Beispiel:

```python
# Solution 1

file = open("errors.txt", "r")
# Some actions with file
file.close()


# Solution 2

with open("errors.txt", "r") as file:
	# Some actions with file
```

In beiden Lösungen wird die Datei geöffnet und geschlossen, aber der zweite Fall ist eleganter, braucht weniger Platz und garantiert, dass die Datei auch bei einem Fehler geschlossen wird\! Zum Beispiel wird diese Datei geschlossen:

```python
with open("errors.txt", "w+") as file:
	file.read()
    file.write(1/0)
```

Kontext-Manager funktionieren nicht nur mit Dateien, aber wir werden die alternativen Anwendungsfälle später behandeln. Die wichtigsten Punkte, die Sie sich bei der Arbeit mit Kontext-Managern merken sollten, sind:

1.  Ein Kontext-Manager enthält immer zwei spezielle Methoden: `__enter__` und `__exit__`.
2.  Die `__enter__`-Methode gibt ein Objekt zurück, das einer Variable nach dem `as`-Schlüsselwort zugewiesen wird. Der Standardwert ist `None` und er ist optional.
3.  Wenn in `__init__` oder `__enter__` ein Fehler auftritt, wird der Codeblock nie ausgeführt und `__exit__` wird nicht aufgerufen.
4.  Nach dem Betreten eines Codeblocks wird `__exit__` immer aufgerufen, selbst wenn eine Ausnahme auftritt.

Hier ist die Struktur eines Kontext-Managers:

```python
class CustomContextManager():
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def __del__(self):
        pass
```