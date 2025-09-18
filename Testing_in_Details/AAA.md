Gerne erkläre ich dir die vier Schritte eines Tests genauer, die du auf deiner Lernkarte gefunden hast: **Arrange/Setup**, **Act**, **Assert** und **Cleanup/Teardown**.

Ein Test überprüft das Ergebnis eines bestimmten Verhaltens und stellt sicher, dass dieses Ergebnis mit den Erwartungen übereinstimmt. Das "Verhalten" bezieht sich darauf, wie ein System auf eine spezifische Situation reagiert.

Die vier Schritte sind wie folgt definiert:

1.  **Arrange/Setup**
    *   Dieser Schritt dient dazu, alles für den Test vorzubereiten.
    *   Dazu gehören das **Vorbereiten von Objekten**, das **Starten oder Beenden von Diensten**, das **Einfügen von Datensätzen in eine Datenbank** oder das **Erstellen von Anmeldeinformationen** für einen Benutzer, der noch nicht existiert.
    *   Im `unittest`-Framework wird die Vorbereitung (Arrange) häufig in der Methode `setUp()` durchgeführt, die **vor jeder Testmethode** aufgerufen wird. Für klassenweite Vorbereitung gibt es `setUpClass()`, die **bevor alle Tests in einer Klasse ausgeführt wurden**, aufgerufen wird und als `classmethod()` deklariert werden muss.
    *   In Pytest wird der Setup-Schritt durch **Fixtures** realisiert, die mit `@pytest.fixture` dekoriert werden. Diese ermöglichen es, einen generischen Setup-Schritt zu definieren, der wiederverwendet werden kann. Eine Fixture kann wie `setUp()` aus unittest funktionieren, aber du kannst spezifisch definieren, welche Fixture für eine Testfunktion benötigt wird.

2.  **Act**
    *   Dies ist die eigentliche **Aktion, die das zu testende Verhalten auslöst**.
    *   Typischerweise handelt es sich dabei um den Aufruf einer Funktion oder Methode.
    *   Der Test wird in den Schritten **Act** und **Assert** ausgeführt, wobei das Verhalten zwischen diesen beiden Schritten stattfindet.

3.  **Assert**
    *   In diesem Schritt wird das **Ergebnis der Aktion überprüft** und sichergestellt, dass es wie erwartet funktioniert.
    *   Es wird also überprüft, ob das System das korrekte Verhalten gezeigt hat.

4.  **Cleanup/Teardown**
    *   Hier räumt der Test **nach sich selbst auf**, um sicherzustellen, dass er andere Tests nicht versehentlich beeinflusst. Dies ist wichtig für die Isolation und Wiederholbarkeit der Tests.
    *   Im `unittest`-Framework wird die Bereinigung (Teardown) in der Methode `tearDown()` vorgenommen, die **nachdem die Testmethode aufgerufen und ihr Ergebnis gespeichert wurde**, aufgerufen wird. Sie wird auch dann aufgerufen, wenn die Testmethode eine Ausnahme auslöst. Für klassenweite Bereinigung gibt es `tearDownClass()`, die **nachdem alle Tests in einer Klasse ausgeführt wurden**, aufgerufen wird und als `classmethod()` deklariert werden muss.
    *   Pytest-Fixtures bieten ein vorteilhaftes Teardown-System. Dazu wird die `yield`-Anweisung anstelle von `return` verwendet. Jeglicher Teardown-Code für eine Fixture wird **nach der `yield`-Anweisung platziert**. Pytest ermittelt eine Reihenfolge für die Fixtures, führt sie bis zum `yield` aus und kehrt dann nach Beendigung des Tests in umgekehrter Reihenfolge zurück, um den Teardown-Code nach dem `yield` auszuführen.

Es ist wichtig zu beachten, dass die Schritte **Act** und **Assert** den Kern des Tests bilden, während **Arrange/Setup** und **Cleanup/Teardown** **optionale Schritte** sind.

**Mocking** ist ein verwandtes Konzept, das oft im Rahmen des Setup-Schritts verwendet wird, um Abhängigkeiten zu isolieren und das Testen zu vereinfachen.
*   Im `unittest`-Framework wird Mocking durch die Bibliothek `unittest.mock` bereitgestellt, insbesondere mit `patch()` als **Decorator** oder **Context Manager**.
*   Pytest bietet einen ähnlichen Mechanismus namens `monkeypatch`.

Der **Gültigkeitsbereich (Scope)** von Fixtures in Pytest (z.B. `function`, `class`, `module`, `package`, `session`) definiert, wann eine Fixture erstellt und wieder zerstört wird. Beispielsweise hat `scope="function"` den Standard-Gültigkeitsbereich, bei dem die Fixture am Ende der Testfunktion zerstört wird, während `scope="module"` bewirkt, dass eine Fixture nur einmal pro Testmodul aufgerufen wird, ähnlich wie `setUpClass()` und `tearDownClass()` in `unittest`.