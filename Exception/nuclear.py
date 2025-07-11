from typing import Any


class SlowResponse(Exception):

    min_response = 51
    max_response = 75

    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

        super().__init__(f"Warning! {name} has "
                f"a slow response of {response} ms.")


class ExtraSlowResponse(SlowResponse):
    min_response = 76
    max_response = 100

    def __init__(self, name: str, response: int) -> None:

        super().__init__(name, response)

        self.args = (f"Alarm! {name} has "
                f"a very slow response of {response} ms.",)


class DangerouslySlowResponse(ExtraSlowResponse):
    min_response = 101

    def __init__(self, name: str, response: int) -> None:

        super().__init__(name, response)

        self.args = (f"Nuclear power station is in danger! {name} has "
                f"a dangerously slow response of {response} ms.",)


def check_device_response(device: dict[str, Any]) -> None:
    if SlowResponse.min_response <= device["response"] <= SlowResponse.max_response:
        raise SlowResponse(device["name"], device["response"])

    if ExtraSlowResponse.min_response <= device["response"] <= ExtraSlowResponse.max_response:
        raise ExtraSlowResponse(device["name"], device["response"])

    if device["response"] >= DangerouslySlowResponse.min_response:
        raise DangerouslySlowResponse(device["name"], device["response"])


def check_station_devices(devices: list[dict[str, Any]]) -> None:

    true_response = True

    for device in devices:
        try:
            check_device_response(device)
        except SlowResponse as e:
            true_response = False

            error_message = str(e)

            if isinstance(e, DangerouslySlowResponse):
                extra_message = " We are in serious trouble!"
            elif isinstance(e, ExtraSlowResponse):
                extra_message = " Needs to be repaired!"
            elif isinstance(e, SlowResponse):
                extra_message = " Pay attention!"
            else:
                extra_message = ""

            print(f"{error_message}{extra_message}")

    if true_response:
        print("Responses of all devices does not exceed the norm.")


check_station_devices([
  {"name": "Polar crane", "response": 52},
  {"name": "Reactor shaft", "response": 81},
  {"name": "Pressure compensator", "response": 149},
  {"name": "Steam generator", "response": 40},
])
# Warning! Polar crane has a slow response of 52 ms. Pay attention!
# Alarm! Reactor shaft has a very slow response of 81 ms. Needs to be repaired!
# Nuclear power station is in danger! Pressure compensator has a dangerously slow response of 149 ms. We are in serious trouble!

"""
check_station_devices([
  {"name": "Reactor shaft", "response": 40},
  {"name": "Polar crane", "response": 25},
  {"name": "Steam generator", "response": 11},
  {"name": "Pressure compensator", "response": 50},
])
"""
# Responses of all devices does not exceed the norm.
