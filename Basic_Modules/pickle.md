
## `pickle`

Das **`pickle`**-Modul wird für die **Serialisierung und Deserialisierung von Python-Objekten** verwendet – jedes solche Objekt kann "gepickelt" und auf der Festplatte gespeichert werden. **`pickle`** ist **schneller** als **`json`** und unterstützt eine **breitere Palette** von Python-Typen, einschließlich benutzerdefinierter Objekte. Wir importieren das **`pickle`**-Modul so:

```python
import pickle
```

`pickle` bietet Funktionen zum bequemen Speichern und Laden von Objekten:

  * `pickle.dump()` – schreibt ein serialisiertes Objekt in eine Datei.
  * `pickle.dumps()` – gibt ein serialisiertes Objekt als Byte-Stream zurück.
  * `pickle.load()` – lädt ein Objekt aus einer Datei.
  * `pickle.loads()` – lädt ein Objekt aus einem Byte-Stream.

Hier ist ein Beispiel:

```python
import pickle


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


user_1 = Person("Mariia", 19)
user_2 = Person("Vitalii", 26)
user_list = [user_1, user_2]

with open("mentors.pickle", "wb") as pickle_file:
    for user in user_list:
        pickle.dump(user, pickle_file)
```

Dies erstellt die Datei `mentors.pickle`:

```
7__main__Person)}(nameMariiaageKub.8__main__Person)}(nameVitaliiageKub.
```

Solch ein Datensatz mag verwirrend aussehen, aber wenn wir ihn mit der **`load()`**-Methode aus dem **`pickle`**-Modul lesen, wird alles korrekt angezeigt:

```python
import pickle


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


with open("mentors.pickle", "rb") as pickle_file:
    user_1 = pickle.load(pickle_file)
    user_2 = pickle.load(pickle_file)

print(user_1.__dict__)	# {"name": "Mariia", "age": 19}
print(user_2.__dict__)		# {"name": "Vitalii", "age": 26}
```

```
```