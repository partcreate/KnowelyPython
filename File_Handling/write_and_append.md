[](https://www.google.com/search?q=%23writing-and-appending)

### Writing and Appending

Um Informationen in eine Datei zu schreiben, verwenden wir den Modus `w` (write). Dieser Modus erstellt eine neue Datei, falls sie nicht existiert, oder überschreibt eine bestehende Datei. Die eingebaute Methode `write()` ist eine Möglichkeit, Informationen in eine Datei zu schreiben; sie akzeptiert nur Strings als Argumente:

```python
file = open("errors.txt", "w")
file.write("17:00 14/09/2022 value error")

file.close()
```

`errors.txt` enthält nun den String "17:00 14/09/2022 value error", der die alten Informationen überschreibt. Wenn wir Daten anhängen möchten, **ohne** die bestehenden Informationen zu verlieren, können wir die Datei im Modus `a` (append) öffnen. Dieser Modus erstellt die Datei, falls sie nicht existiert, oder hängt neue Daten an. Kombinieren wir dies mit der Methode `write()`, um in die Datei zu schreiben:

```python
file = open("errors.txt", "a")
file.write("17:00 14/09/2022 value error")

file.close()
```

In der Konsole werden wir sehen:

```
10:53 12/09/2022 too many requests
21:17 13/09/2022 user admin not found
17:00 14/09/2022 value error
```

Diese Beispiele veranschaulichen den Unterschied zwischen dem Schreib- und dem Anhängemodus. Im ersten Beispiel werden die bestehenden Informationen durch neue Informationen ersetzt. Im zweiten Beispiel werden die neuen Informationen an das Ende der Datei angefügt, wobei der vorhandene Inhalt erhalten bleibt.