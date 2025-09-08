Um in Python zu prüfen, ob eine Datei existiert, verwendest du am besten das Modul **`os`** oder das modernere **`pathlib`**. Beide sind Teil der Standardbibliothek, du musst also nichts extra installieren.

-----

### Methode 1: Mit `os.path.exists()`

Dies ist eine weit verbreitete Methode, die einfach und direkt ist. Sie gibt `True` zurück, wenn der angegebene Pfad existiert, unabhängig davon, ob es sich um eine Datei oder ein Verzeichnis handelt.

Wenn du **nur Dateien** überprüfen möchtest, kannst du `os.path.isfile()` verwenden.

```python
import os

dateipfad = "beispiel.txt"

# Prüfen, ob der Pfad existiert (egal ob Datei oder Verzeichnis)
if os.path.exists(dateipfad):
    print(f"Der Pfad '{dateipfad}' existiert.")
else:
    print(f"Der Pfad '{dateipfad}' existiert nicht.")

# Prüfen, ob es sich um eine Datei handelt
if os.path.isfile(dateipfad):
    print(f"'{dateipfad}' ist eine Datei.")
else:
    print(f"'{dateipfad}' ist keine Datei oder existiert nicht.")
```

`os.path.isdir()` ist das Gegenstück, um Verzeichnisse zu prüfen.

-----

### Methode 2: Mit `pathlib` (empfohlen für moderne Projekte)

Das `pathlib`-Modul ist objektorientierter und bietet eine sauberere Syntax. Es ist seit Python 3.4 Teil der Standardbibliothek und gilt als der modernere Ansatz.

```python
from pathlib import Path

dateipfad = Path("beispiel.txt")

# Prüfen, ob der Pfad existiert
if dateipfad.exists():
    print(f"Der Pfad '{dateipfad}' existiert.")
else:
    print(f"Der Pfad '{dateipfad}' existiert nicht.")

# Prüfen, ob es sich um eine Datei handelt
if dateipfad.is_file():
    print(f"'{dateipfad}' ist eine Datei.")
else:
    print(f"'{dateipfad}' ist keine Datei oder existiert nicht.")
```

`pathlib`-Objekte haben auch Methoden wie `is_dir()` für Verzeichnisse und `is_symlink()` für symbolische Links. Beide Methoden sind sehr effizient.