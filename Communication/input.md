Die Interaktion mit dem Benutzer über die Konsole ist in Python sehr einfach. Du verwendest dafür die Funktionen **`input()`** für die Eingabe und **`print()`** für die Ausgabe.

-----

### Frage stellen und Antwort bekommen

Mit der `input()`-Funktion kannst du den Benutzer eine Frage stellen. Der Text, den du in die Klammern schreibst, wird dem Benutzer angezeigt. Sobald der Benutzer etwas eingibt und die Eingabetaste drückt, gibt `input()` die Eingabe als **String** zurück. Diesen String kannst du dann in einer Variable speichern.

Hier ist ein einfaches Beispiel:

```python
# Die input()-Funktion stellt die Frage und wartet auf eine Eingabe des Benutzers.
# Die Eingabe wird in der Variable 'name' gespeichert.
name = input("Wie heißt du? ")

# Die print()-Funktion gibt die gespeicherte Antwort aus.
print(f"Hallo, {name}!")

# Beispiel für die Konsoleingabe/-ausgabe:
# Wie heißt du? Max
# Hallo, Max!
```

-----

### Wichtiger Hinweis zur Eingabe

`input()` gibt immer einen **String** zurück, auch wenn der Benutzer eine Zahl eingibt. Wenn du mit der Eingabe rechnen möchtest, musst du sie zuerst in einen numerischen Typ wie `int` (ganze Zahl) oder `float` (Kommazahl) umwandeln.

Hier ein Beispiel:

```python
# Frage nach dem Alter
alter_str = input("Wie alt bist du? ")

# Versuch, mit dem Alter zu rechnen, was einen Fehler verursacht,
# wenn der Benutzer z. B. '30' eingibt (ein String).
# print(alter_str + 5) -> TypeError

# Korrekte Vorgehensweise: Umwandeln in einen Integer
alter_int = int(alter_str)
print(f"Du wirst in 5 Jahren {alter_int + 5} sein.")

# Beispiel für die Konsoleingabe/-ausgabe:
# Wie alt bist du? 25
# Du wirst in 5 Jahren 30 sein.
```