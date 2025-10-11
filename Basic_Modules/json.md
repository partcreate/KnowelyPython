
## json

Das Modul `json` (JavaScript Object Notation) erlaubt eine einfache Kodierung und Dekodierung von Daten. Hier ist ein Beispiel für ein JSON-Objekt, das einem Wörterbuch mit Schlüsseln und Werten ähnelt:

```

{
  "name": "Boris",
  "age": 10
}

```

Wir können das Modul `json` mit folgendem Code importieren:

```python
import json
````

Es gibt zwei Hauptfunktionen für die Interaktion mit JSON-Objekten in Python:

  * `json.load()` — liest ein JSON-Dokument aus einer Datei.
  * `json.loads()` — konvertiert einen JSON-String in ein Python-Wörterbuch (Dictionary).

Hier ist ein Beispiel für die Verwendung von `json.loads()`:

```python
import json


mentors_string = '{"count": 2,"names": ["Mariia", "Petro"]}'
mentors = json.loads(mentors_string)
print(mentors)    	      # {"count": 2,"names": ["Mariia", "Petro"]}
print(type(mentors))	 # <class "dict">
```

Betrachten wir die Datei `mentors.json` mit den folgenden Daten und der Funktion `json.load()`:

```
{
 "count": 2,
 "names": ["Mariia", "Petro"]
}
```

Als Ergebnis erhalten wir:

```python
import json

with open("mentors.json", "r") as file:
   mentors = json.load(file)

print(mentors)		# {"count": 2, "names": ["Mariia", "Petro"]}
```

Wir können ein Python-Objekt mit den Funktionen `json.dump()` und `json.dumps()` in einen JSON-String konvertieren. Der Unterschied ist, dass `json.dump()` Python-Objekte als JSON-formatierte Daten in eine Datei schreibt, während `json.dumps()` ein Python-Objekt in einen JSON-formatierten String kodiert.

Hier ist ein Beispiel für die Verwendung der Funktion `json.dump()`:

```python
import json


mentors_string = {"count": 3, "names": ["Mariia", "Petro", "Ivan"]}
with open("mentors.json", "w") as file:
   mentors = json.dump(mentors_string, file)
```

Es schreibt die folgenden Daten in die Datei `mentors.json`:

```
{"count": 3, "names": ["Mariia", "Petro", "Ivan"]}
```

Und ein Beispiel für die Verwendung der Methode `json.dumps()`:

```python
import json


mentors_dictionary = {"count": 2,"names": ["Mariia", "Petro"]}
mentors = json.dumps(mentors_dictionary)
print(mentors)		    # {"count": 2, "names": ["Mariia", "Petro"]}
print(type(mentors))	# <class "str">
```