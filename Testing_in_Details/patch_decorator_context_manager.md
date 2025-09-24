Die Antwort auf deiner Lernkarte ist korrekt. Wenn du ein Objekt für die Dauer deiner gesamten Testfunktion mocken möchtest, kannst du `patch()` als **Funktions-Decorator** verwenden. Lass uns das genauer betrachten:

### Was ist Mocking?
**Mocking** ist eine Technik, bei der ein **Mock-Objekt** ein echtes Objekt während des Tests ersetzt und imitiert. Es ist ein flexibles und leistungsstarkes Werkzeug zur Verbesserung der Testqualität. Anstatt echte Abhängigkeiten (wie Datenbanken, externe APIs oder komplexe Services) zu verwenden, die den Test verlangsamen oder unzuverlässig machen könnten, werden Mocks eingesetzt, um ein kontrolliertes Verhalten zu simulieren.

### `unittest.mock.patch()`
Die Bibliothek `unittest.mock` ist das Standardwerkzeug für Mocking in Python. Sie bietet eine einfache Möglichkeit, Mocks in deine Tests einzuführen. Das **`patch()`-Werkzeug** von `unittest.mock` ist besonders leistungsstark. Es sucht ein bestimmtes Objekt in einem ausgewählten Modul und **ersetzt dieses Objekt durch einen Mock**.

### Wann `patch()` als Funktions-Decorator verwenden?
Normalerweise wird `patch()` entweder als **Decorator** oder als **Context Manager** verwendet, um einen Bereich zu definieren, in dem das Zielobjekt gemockt werden kann.

Wie deine Lernkarte besagt, wählst du `patch()` als **Funktions-Decorator**, wenn du ein Objekt **für die gesamte Dauer deiner Testfunktion** mocken möchtest.

Das bedeutet:
*   **Setup:** Der Decorator stellt sicher, dass das echte Objekt am Anfang der Testfunktion durch den Mock ersetzt wird. Dies fällt in den **Arrange/Setup**-Schritt eines Tests, wo alles für den Test vorbereitet wird.
*   **Aktive Dauer:** Der Mock ist während des gesamten Verlaufs der Testfunktion aktiv, d.h., er deckt die **Act**-Phase (wo das zu testende Verhalten ausgelöst wird) und die **Assert**-Phase (wo das Ergebnis überprüft wird) ab.
*   **Cleanup:** Nachdem die Testfunktion beendet ist – egal ob sie erfolgreich war oder eine Ausnahme ausgelöst hat – sorgt der Decorator automatisch dafür, dass das ursprüngliche Objekt wiederhergestellt wird. Dies entspricht dem **Cleanup/Teardown**-Schritt, der nach dem Test aufräumt, um andere Tests nicht zu beeinflussen.

Ein Beispiel für die Verwendung von `patch()` als Decorator findest du in den Quellen.

### Wann `patch()` als Context Manager verwenden?
Es gibt auch Situationen, in denen du `patch()` als **Context Manager** anstelle eines Decorators verwenden solltest:
*   Wenn du ein Objekt **nur für einen Teil** des Testbereichs mocken möchtest. Das bedeutet, der Mock ist nur innerhalb des `with`-Blocks aktiv und wird danach sofort wieder auf den Originalzustand zurückgesetzt.
*   Wenn du bereits **zu viele Decorators oder Parameter** verwendest, was die Lesbarkeit deines Tests beeinträchtigen könnte. In solchen Fällen kann die Verwendung eines Context Managers innerhalb der Funktion für mehr Klarheit sorgen.

Zusammenfassend lässt sich sagen, dass die Verwendung von `patch()` als Funktions-Decorator eine elegante und saubere Methode ist, um sicherzustellen, dass ein bestimmtes Objekt während der gesamten Ausführung einer Testfunktion gemockt wird, wobei das Setup und Cleanup automatisch vom `unittest`-Framework gehandhabt werden.