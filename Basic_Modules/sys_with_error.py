import sys


# 1. Benutzerdefinierte Exception-Klasse definieren
class MissingArgumentError(Exception):
    """Exception, die signalisiert, dass ein erforderliches Kommandozeilenargument fehlt."""

    def __init__(self, message="Ein erforderliches Argument fehlt."):
        self.message = message
        super().__init__(self.message)


def process_arguments():
    # 2. Prüfen der Länge
    if len(sys.argv) < 2:
        # 3. Spezifische Exception auslösen
        raise MissingArgumentError("Bitte geben Sie einen Dateinamen als Argument an.")

    # Wenn das Argument vorhanden ist, wird der Wert zurückgegeben
    return sys.argv[1]


# Hauptausführung des Skripts
if __name__ == "__main__":
    try:
        filename = process_arguments()
        print(f"Verarbeite Datei: {filename}")
        # Hier würde die eigentliche Logik folgen...

    except MissingArgumentError as e:
        # Die spezifische Exception abfangen
        print(f"FEHLER: {e}")
        print("Nutzung: python skriptname.py <dateiname>")
        sys.exit(1)  # Programm mit Fehler-Code beenden

    # Hier könnten Sie auch andere Fehler abfangen, z.B. FileNotFoundError