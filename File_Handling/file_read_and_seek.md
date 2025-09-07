### Lesen

Um die gesamte Datei in eine Variable zu lesen, verwenden wir die Methode `read()`:

```python
file = open("errors.txt", "r")

print(file.read())
# 10:53 12/09/2022 too many requests
# 21:17 13/09/2022 user admin not found

file.close() # And do not forget to close your file
```

Wenn wir der Methode `read()` ein numerisches Argument übergeben, gibt sie die angegebene Anzahl von Zeichen aus der Datei zurück:

```python
file = open("errors.txt", "r")
print(file.read(10))     # 10:53 12/0
file.close()
```

Um das Lesen an einer anderen Position als dem Anfang der Datei zu beginnen, verwenden Sie die Methode `seek()` und geben die Anzahl der zu überspringenden Bytes an:

```python
file = open("errors.txt", "r")

file.seek(10)
print(file.read())
# 9/2022 too many requests
# 21:17 13/09/2022 user admin not found

file.close()
```

Um eine Datei zeilenweise zu lesen, verwenden wir eine Schleife mit der Methode `readline()` oder `readlines()`. Die Methode `readline()` gibt jeweils eine Zeile zurück, während `readlines()` alle Zeilen als Liste zurückgibt, wobei jedes Element eine Zeile in der Datei ist. Zum Beispiel:

```python
file = open("errors.txt", "r")

print("Readline method working")
print(file.readline())

file.close()
```

In der Konsole werden wir sehen:

```
Readline method working
10:53 12/09/2022 too many requests
```

Hier ist die Methode `readlines()` in Aktion:

```python
file = open("errors.txt", "r")

line_number = 1		# Variable for seeing the number of a line 
print("Readlines method working")
for line in file.readlines():
    print(f"Line number {line_number}")	
    print(line)
    line_number += 1

file.close()
```

In der Konsole werden wir sehen:

```
Readlines method working
Line number 1
10:53 12/09/2022 too many requests
Line number 2
21:17 13/09/2022 user admin not found
```

Ein Vorteil dieser Methoden ist, dass sie den Speicher effizient verwalten, indem sie nur eine Zeile nach der anderen lesen – im Gegensatz zur Methode `read()`, die die gesamte Datei liest. Dies ermöglicht es uns, auch große Dateien Zeile für Zeile zu verarbeiten. Eine weitere Möglichkeit, zeilenweise zu lesen, ist die Iteration über die Datei mit einer `for`-Schleife:

```python
file = open("errors.txt", "r")

line_number = 1		# Variable for seeing the number of a line 
for line in file:
    print(f"Line number {line_number}")	
    print(line)
    line_number += 1

file.close()
```

In der Konsole werden wir sehen:

```
Line number 1
10:53 12/09/2022 too many requests
Line number 2
21:17 13/09/2022 user admin not found
```