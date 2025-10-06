## `os`

Das `os`-Modul ermöglicht die Verwendung von Funktionen, die vom Betriebssystem (daher der Name) abhängen, auf **portable** Weise, wodurch sichergestellt wird, dass das Programm auf verschiedenen Betriebssystemen ausgeführt werden kann. Wir importieren das `os`-Modul wie folgt:

```python
import os
```

Hier ist, was wir mit dem `os`-Modul tun können:

  * `os.environ` greift auf ein **Wörterbuch** von Umgebungsvariablen zu, die auf Betriebssystemebene gespeichert sind und oft **Konfigurationsdaten** enthalten.
  * `os.getcwd()` gibt das **aktuelle Arbeitsverzeichnis** (current working directory) des Prozesses zurück.

Es wird mit dem eingebauten `os.path`-Modul geliefert, das Methoden für die Arbeit mit Pfaden bietet:

  * `os.path.exists()` prüft, ob ein **angegebener Pfad existiert**.
  * `os.path.join()` **verbindet** auf intelligente Weise eine oder mehrere Pfadkomponenten.

`os.path` ist besonders nützlich, da sich die Verzeichnis- und Dateipfadformate je nach Betriebssystem unterscheiden, wie das folgende Beispiel zeigt. Mit diesem Eingabecode:

```python
import os

print(os.getcwd())
print(os.path.exists("file.txt")) # There is "file.txt" in working directory
print(os.path.exists("not_existed_file.txt")) # There is no "not_existed_file.txt" file in working directory
```

erhalten wir:

```
/Users/UserName/Desktop/projects/os_module_theory.py
True
False
```

```
```