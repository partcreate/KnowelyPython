from typing import Dict, Any, List

# --- 1. Definition der benutzerdefinierten Exceptions ---


# Basis-Exception für alle langsamen Reaktionen
class SlowResponse(Exception):
    """
    Ausnahme für langsame Geräteantwortzeiten (51-75 ms).
    """
    def __init__(self, name: str, response: int):
        # Speichert Gerätename und Antwortzeit als Attribute der Exception
        self.device_name = name
        self.response_time = response
        # Der Fehlertext wird hier formuliert und an die Basisklasse übergeben.
        # Dies wird von str(exception) und print(exception) verwendet.
        super().__init__(f"Warning! {name} has a slow response of {response} ms.")


class ExtraSlowResponse(SlowResponse):
    """
    Ausnahme für sehr langsame Geräteantwortzeiten (76-100 ms).
    Erbt von SlowResponse, um die Hierarchie abzubilden.
    """
    def __init__(self, name: str, response: int):
        # Ruft den Konstruktor der direkten Elternklasse (SlowResponse) auf.
        # Dies initialisiert self.device_name und self.response_time und setzt die Nachricht.
        super().__init__(name, response)
        # Überschreibt die Fehlermeldung mit der spezifischen Nachricht für ExtraSlowResponse.
        self.args = (f"Alarm! {name} has a very slow response of {response} ms.",)


class DangerouslySlowResponse(ExtraSlowResponse):
    """
    Ausnahme für gefährlich langsame Geräteantwortzeiten (> 100 ms).
    Erbt von ExtraSlowResponse, um die Hierarchie abzubilden.
    """
    def __init__(self, name: str, response: int):
        # Ruft den Konstruktor der direkten Elternklasse (ExtraSlowResponse) auf.
        super().__init__(name, response)
        # Überschreibt die Fehlermeldung mit der spezifischen Nachricht für DangerouslySlowResponse.
        self.args = (f"Nuclear power station is in danger! {name} has a dangerously slow response of {response} ms.",)


# --- Konstanten für die Schwellenwerte der Reaktionszeiten ---
MAX_NORMAL_RESPONSE_TIME = 50
SLOW_THRESHOLD_MIN = 51
EXTRA_SLOW_THRESHOLD_MIN = 76
DANGEROUSLY_SLOW_THRESHOLD_MIN = 101 # Alle Werte > 100ms


# --- 2. Funktion: check_device_response ---
def check_device_response(device: Dict[str, Any]) -> None:
    """
    Überprüft die Reaktionszeit eines einzelnen Geräts und löst die entsprechende Ausnahme aus.

    Args:
        device (Dict): Ein Dictionary mit 'name' (str) und 'response' (int) des Geräts.
    
    Raises:
        SlowResponse: Wenn die Antwortzeit zwischen 51 und 75 ms liegt.
        ExtraSlowResponse: Wenn die Antwortzeit zwischen 76 und 100 ms liegt.
        DangerouslySlowResponse: Wenn die Antwortzeit länger als 100 ms ist.
    """
    device_name = device["name"]
    response_time = device["response"]

    if response_time > MAX_NORMAL_RESPONSE_TIME:
        if DANGEROUSLY_SLOW_THRESHOLD_MIN <= response_time: # Oder response_time > 100
            raise DangerouslySlowResponse(name=device_name, response=response_time)
        elif EXTRA_SLOW_THRESHOLD_MIN <= response_time: # Oder 76 <= response_time <= 100
            raise ExtraSlowResponse(name=device_name, response=response_time)
        elif SLOW_THRESHOLD_MIN <= response_time: # Oder 51 <= response_time <= 75
            raise SlowResponse(name=device_name, response=response_time)
    # Wenn die Antwortzeit <= MAX_NORMAL_RESPONSE_TIME ist, wird keine Ausnahme ausgelöst.


# --- 3. Funktion: check_station_devices ---
def check_station_devices(devices_list: List[Dict[str, Any]]) -> None:
    """
    Überprüft eine Liste von Geräten, handhabt Ausnahmen und gibt entsprechende Meldungen aus.

    Args:
        devices_list (List[Dict]): Eine Liste von Geräte-Dictionaries.
    """
    all_normal_responses = True  # Flag, um zu verfolgen, ob alle Antworten im Normbereich liegen

    for device in devices_list:
        try:
            # Versucht, die Geräteantwort zu überprüfen. Wenn eine Ausnahme auftritt,
            # wird der entsprechende 'except'-Block ausgeführt.
            check_device_response(device)
            # Wenn keine Ausnahme ausgelöst wird, ist die Antwortzeit im Normbereich.
            # Für diese Aufgabe wird nichts explizit ausgegeben, wenn es normal ist,
            # außer der abschließenden Nachricht.
        except SlowResponse as e:
            # Fängt SlowResponse und alle davon abgeleiteten Ausnahmen (ExtraSlowResponse, DangerouslySlowResponse) ab.
            all_normal_responses = False  # Eine Ausnahme ist aufgetreten, also nicht mehr 'alles normal'.
            
            # Die Nachricht der Ausnahme ist bereits formatiert (z.B. "Warning! ...")
            error_message = str(e)  # Holt die formatierte Nachricht der Exception

            # Fügt die zusätzliche Nachricht basierend auf dem genauen Exception-Typ hinzu
            if isinstance(e, DangerouslySlowResponse):
                extra_message = " We are in serious trouble!"
            elif isinstance(e, ExtraSlowResponse):
                extra_message = " Needs to be repaired!"
            elif isinstance(e, SlowResponse):  # Dieser Zweig fängt nur die 'reine' SlowResponse ab
                extra_message = " Pay attention!"
            else:
                extra_message = "" # Fallback, sollte nicht erreicht werden

            print(f"{error_message}{extra_message}")
        except Exception as e:
            # Dies fängt andere unerwartete Ausnahmen ab, die nicht von SlowResponse erben.
            # Sollte in diesem spezifischen Szenario nicht vorkommen, aber ist gute Praxis.
            all_normal_responses = False
            print(f"Unerwarteter Fehler bei Gerät {device['name']}: {e}")

    # Am Ende, wenn keine Ausnahmen aufgetreten sind, gib die Erfolgsmeldung aus.
    if all_normal_responses:
        print("Responses of all devices does not exceed the norm.")


# --- Testfälle gemäß Aufgabenstellung ---

print("--- Testfall 1: Gemischte Antworten ---")
check_station_devices([
    {"name": "Polar crane", "response": 52},        # Slow (51-75)
    {"name": "Reactor shaft", "response": 81},      # ExtraSlow (76-100)
    {"name": "Pressure compensator", "response": 149}, # DangerouslySlow (>100)
    {"name": "Steam generator", "response": 40},    # Normal (<=50)
])
# Erwartete Ausgabe:
# Warning! Polar crane has a slow response of 52 ms. Pay attention!
# Alarm! Reactor shaft has a very slow response of 81 ms. Needs to be repaired!
# Nuclear power station is in danger! Pressure compensator has a dangerously slow response of 149 ms. We are in serious trouble!

"""
print("\n--- Testfall 2: Alle Antworten im Normbereich ---")
check_station_devices([
    {"name": "Reactor shaft", "response": 40},
    {"name": "Polar crane", "response": 25},
    {"name": "Steam generator", "response": 11},
    {"name": "Pressure compensator", "response": 50},
])
# Erwartete Ausgabe:
# Responses of all devices does not exceed the norm.

print("\n--- Zusätzlicher Testfall: Nur DangerouslySlow ---")
check_station_devices([
    {"name": "Main Pump", "response": 101}, # DangerouslySlow
    {"name": "Cooling System", "response": 45}, # Normal
])

print("\n--- Zusätzlicher Testfall: Nur ExtraSlow ---")
check_station_devices([
    {"name": "Control Rods", "response": 76}, # ExtraSlow
    {"name": "Emergency Core", "response": 30}, # Normal
])
"""
