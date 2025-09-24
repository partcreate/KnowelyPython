Da ist was dran. Ich werde den bereitgestellten HTML-Code in die deutsche Umgangssprache übersetzen.

-----

\<a id="test-coverage"\>\</a\>

## Testabdeckung

Die Messung der Abdeckung wird typischerweise verwendet, um die Effektivität von Tests zu bewerten. Sie kann aufzeigen, welche Teile deines Codes durch Tests abgedeckt werden und welche nicht.

Für die Messung der Code-Abdeckung kannst du das Werkzeug `сoverage.py` verwenden. Es überwacht dein Programm, zeichnet auf, welche Codeteile ausgeführt wurden, und analysiert dann den Code, der hätte ausgeführt werden können, aber nicht ausgeführt wurde.

Um die Abdeckungsmessung auszuführen:

Verwende den Befehl `coverage run`, um deine Tests auszuführen und die Daten zu sammeln. Du kannst deinen Test-Runner unter Coverage ausführen, so wie du ihn normalerweise startest. Wenn dein Testausführungsbefehl normalerweise mit `python` beginnt, ersetzt du das anfängliche `python` durch `coverage run` — `coverage run -m pytest`. Verwende anschließend den Befehl `coverage report`, um die Ergebnisse zu melden:

```
$ coverage report
Name                 Stmts      Miss      Cover      Missing
-----------------------------------------------------------
main.py              7          3         57%        8-10
test_main.py         6          0         100%
-----------------------------------------------------------
TOTAL                13         3         77%
```

Für **PyCharm Pro** klicke auf die Schaltfläche **Run with Coverage** in der Hauptsymbolleiste. Dies startet die ausgewählte Ausführungs-/Debug-Konfiguration:
