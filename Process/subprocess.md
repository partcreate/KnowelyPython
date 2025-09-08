Um einen Shell-Befehl in Python auszuführen, kannst du das **`subprocess`**-Modul verwenden. Es ist der moderne und empfohlene Weg, um externe Prozesse zu starten und mit ihnen zu interagieren.

-----

### Die einfachste Methode: `subprocess.run()`

Die Funktion `subprocess.run()` ist die einfachste Möglichkeit, einen Shell-Befehl auszuführen und auf das Ergebnis zu warten.

```python
import subprocess

# Ausführen eines einfachen Befehls
# Auf Windows wäre das "dir", auf Linux/macOS ist es "ls"
befehl = ["ls", "-l"] # Liste der Befehlsargumente
ergebnis = subprocess.run(befehl, capture_output=True, text=True)

# Ausgabe des Befehls anzeigen
print("Standardausgabe:")
print(ergebnis.stdout)

print("Fehlerausgabe:")
print(ergebnis.stderr)

# Überprüfen, ob der Befehl erfolgreich war
if ergebnis.returncode == 0:
    print("Befehl wurde erfolgreich ausgeführt.")
else:
    print("Befehl schlug fehl.")

```

### Wichtige Parameter von `subprocess.run()`:

  * **`capture_output=True`**: Sammelt die Standardausgabe (`stdout`) und die Fehlerausgabe (`stderr`) des Befehls. Ohne diesen Parameter werden die Ausgaben direkt in der Konsole angezeigt.
  * **`text=True`**: Konvertiert die Ausgabe von Bytes in Strings, was die Handhabung stark vereinfacht.
  * **`check=True`**: Wenn dieser Parameter gesetzt ist, wird eine `CalledProcessError`-Exception ausgelöst, falls der Befehl einen Fehler zurückgibt (Exit-Code ungleich 0). Dies ist nützlich, um Fehler sofort zu erkennen.

### Warum `subprocess` und nicht `os.system()`?

Früher wurde oft `os.system()` verwendet. Es ist jedoch veraltet und hat mehrere Nachteile:

  * **Sicherheitsrisiko:** `os.system()` ist anfällig für "Shell Injection", wenn du unsichere Benutzereingaben direkt an den Befehl weitergibst.
  * **Keine Kontrolle:** Du hast keine einfache Möglichkeit, die Standardausgabe oder die Fehlerausgabe zu erfassen oder den Exit-Code zu überprüfen.

Deshalb solltest du immer `subprocess` verwenden.