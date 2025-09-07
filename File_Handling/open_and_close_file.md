### Öffnungsmodi

Bevor wir mit einer Datei arbeiten, müssen wir sie mit der integrierten Methode `open()` öffnen, wobei der Dateipfad und der Öffnungsmodus in Klammern angegeben werden. Wenn wir den Modus nicht angeben, wird die Datei im **Standardmodus `r`** geöffnet, wobei `r` für `reading` steht. Es gibt einige Modi:

  * `r` liest die Datei und gibt einen Fehler zurück, wenn sie nicht existiert.
  * `w` schreibt Daten in eine Datei; wenn die Datei existiert, wird sie überschrieben, andernfalls wird eine neue erstellt.
  * `a` fügt Daten an eine Datei an; wenn die Datei nicht existiert, wird eine neue erstellt.
  * `x` schreibt Daten in eine Datei und gibt einen Fehler zurück, wenn die Datei bereits existiert (exklusive Erstellung).
  * `t` wird für Textdateien verwendet (Textmodus – wir sehen den Text).
  * `b` wird für Binärdateien wie Bilder oder Videos verwendet (Binärmodus – wir sehen `0` und `1`).
  * `+` ermöglicht sowohl das gleichzeitige Lesen als auch das Schreiben in die Datei.

Als Beispiel betrachten wir eine Datei "errors.txt", die die folgenden Daten enthält:

```
10:53 12/09/2022 too many requests
21:17 13/09/2022 user admin not found
```

Wir können diese Datei wie folgt öffnen:

```python
file = open("errors.txt")
```

Hier wurde die Datei im Standardmodus `r` geöffnet, da kein Modus angegeben wurde. Nun öffnen wir diese Datei im **Lesemodus**:

```python
file = open("errors.txt", "r")
```

Es gibt keinen Unterschied, da der **Lesemodus der Standardmodus ist.**

-----

### Schließen

Stellen Sie sich vor, wir haben ein großes Projekt, das häufig in eine Datei schreibt, und wir vergessen, sie zu schließen. Das Programm läuft weiter und schreibt unnötige Daten, die die Datei schließlich füllen und eine große Menge an Speicher belegen können - was zu Systemfehlern führen kann. Wir können dies vermeiden, indem wir die Datei mit der integrierten Methode `close()` schließen:

```python
file = open("errors.txt", "r")
file.close() # Hier haben wir die Datei geschlossen
```