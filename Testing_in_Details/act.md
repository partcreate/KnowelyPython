Gerne erkläre ich Ihnen den 'Act'-Schritt in einem Test genauer, basierend auf den bereitgestellten Quellen.

Der **'Act'-Schritt** repräsentiert die **Aktion, die das zu testende Verhalten auslöst**. Dies ist typischerweise der Aufruf einer Funktion oder Methode, deren Funktionalität Sie überprüfen möchten. Es ist der Moment, in dem das System die Operation ausführt, die im Mittelpunkt des Tests steht.

Im Rahmen eines Tests ist der 'Act'-Schritt der zweite von vier grundlegenden Schritten, die oft als **Arrange-Act-Assert-Cleanup** bezeichnet werden.

1.  **Arrange/Setup**: Zuerst bereiten Sie alles für den Test vor. Dazu gehören das Initialisieren von Objekten, das Starten oder Beenden von Diensten, das Eingeben von Datensätzen in eine Datenbank oder das Erstellen von Anmeldeinformationen.
2.  **Act**: Nach der Vorbereitung führen Sie die eigentliche Aktion aus, die das zu testende Verhalten startet.
3.  **Assert**: Anschließend überprüfen Sie das Ergebnis dieser Aktion, um sicherzustellen, dass es wie erwartet funktioniert.
4.  **Cleanup/Teardown**: Zum Schluss räumt der Test auf, um sicherzustellen, dass keine anderen Tests unbeabsichtigt beeinflusst werden.

Die Schritte **Act** und **Assert** sind die Kernschritte, in denen der eigentliche Test ausgeführt wird. Das "Verhalten" des Systems findet zwischen dem 'Act'-Schritt und dem 'Assert'-Schritt statt. Während 'Arrange/Setup' und 'Cleanup/Teardown' optionale Schritte sind, sind 'Act' und 'Assert' der wesentliche Teil eines jeden Tests, da sie das Verhalten auslösen und überprüfen.

Ein Test hat das übergeordnete Ziel, das **Ergebnis eines bestimmten Verhaltens zu prüfen und sicherzustellen, dass es mit den Erwartungen übereinstimmt**. "Verhalten" bezieht sich dabei darauf, wie ein System auf eine spezifische Situation reagiert, wobei der Fokus mehr auf dem "Was getan wurde" liegt als auf dem "Wie oder Warum". Der 'Act'-Schritt ist genau derjenige, der dieses "Was getan wurde" in Gang setzt.