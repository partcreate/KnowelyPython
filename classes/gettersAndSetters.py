class Temperature:
    def __init__(self, temperature: int) -> None:
        self.temperature = temperature

    def get_temperature(self) -> int:
        return self._temperature

    def set_temperature(self, temperature: int) -> None:
        if -30 < temperature < 40:
            self._temperature = temperature
        else:
            raise ValueError(f"Invalid temperature. Value should be in the range of -30 and 40, but the actual is {temperature}")

    temperature = property(get_temperature, set_temperature)


today_temperature = Temperature(27)
print(today_temperature.temperature)  # 27

today_temperature.temperature = 12
print(today_temperature.temperature)  # 12

#today_temperature.temperature = 54  # ValueError: Invalid temperature. Value should be in the range of -30 and 40, but the actual is 54

class Person:
    def __init__(self, name: str, alter: int):
        self.name = name
        # Initialisierung des Alters über den ÖFFENTLICHEN Property-Namen.
        # Dies ruft automatisch den Setter 'alter(self, value)' auf.
        self.alter = alter
        print(f"Person {self.name} initialisiert. Alter intern: {self._alter}")

    @property
    def alter(self) -> int:
        """
        Der Getter für das Attribut 'alter'.
        Gibt den Wert des internen Attributs '_alter' zurück.
        """
        print("Getter für 'alter' aufgerufen.")
        # Zugriff auf das INTERNE, "geschützte" Attribut
        return self._alter

    @alter.setter
    def alter(self, value: int):
        """
        Der Setter für das Attribut 'alter'.
        Führt Validierung durch und speichert den Wert im internen '_alter'.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError("Alter muss eine nicht-negative ganze Zahl sein.")
        print(f"Setter für 'alter' aufgerufen. Setze intern auf {value}.")
        # Speichern im INTERNEN, "geschützten" Attribut
        self._alter = value

    @alter.deleter
    def alter(self):
        """
        Der Deleter für das Attribut 'alter'.
        Entfernt das interne Attribut.
        """
        print("Deleter für 'alter' aufgerufen.")
        del self._alter

# --- Nutzung der Klasse ---
print("--- Person 1 erstellen ---")
p1 = Person("Alice", 30) # Initialisiert alter über den Setter

print(f"\nAlter von p1 (über Getter): {p1.alter}") # Ruft Getter auf

print("\n--- Alter von p1 ändern ---")
p1.alter = 31 # Ruft Setter auf
print(f"Neues Alter von p1 (über Getter): {p1.alter}")

try:
    print("\n--- Ungültiges Alter setzen ---")
    p1.alter = -5 # Ruft Setter auf, löst ValueError aus
except ValueError as e:
    print(f"Fehler: {e}")

print("\n--- Alter von p1 löschen ---")
try:
    del p1.alter # Ruft Deleter auf
    print(f"Hat p1 jetzt ein Alter-Attribut? {hasattr(p1, 'alter')}") # False
    print(p1.alter) # Würde AttributeError auslösen
except AttributeError as e:
    print(f"Fehler beim Zugriff nach Löschen: {e}")