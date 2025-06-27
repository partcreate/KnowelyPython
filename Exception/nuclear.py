from typing import Any


class SlowResponse(Exception):

    min_response = 51
    max_response = 75

    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

    def __str__(self) -> str:
        return (f"Warning! {self.name} has "
                f"a slow response of {self.response} ms.")


class ExtraSlowResponse(SlowResponse):
    min_response = 76
    max_response = 100

    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

    def __str__(self) -> str:
        return (f"Alarm! {self.name} has "
                f"a very slow response of {self.response} ms.")


class DangerouslySlowResponse(ExtraSlowResponse):
    min_response = 101

    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

    def __str__(self) -> str:
        return (f"Nuclear power station is in danger! {self.name} has "
                f"a dangerously slow response of {self.response} ms.")


def check_device_response(device: dict[str, Any]) -> None:
    if SlowResponse.min_response <= device["response"] <= SlowResponse.max_response:
        raise SlowResponse(device["name"], device["response"])

    if ExtraSlowResponse.min_response <= device["response"] <= ExtraSlowResponse.max_response:
        raise ExtraSlowResponse(device["name"], device["response"])

    if device["response"] >= DangerouslySlowResponse.min_response:
        raise DangerouslySlowResponse(device["name"], device["response"])


def check_station_devices(devices: list[dict[str, Any]]) -> None:

    for device in devices:
        check_device_response(device)

    print("Responses of all devices does not exceed the norm.")


# check_station_devices([
#  {"name": "Polar crane", "response": 52},
#  {"name": "Reactor shaft", "response": 81},
#  {"name": "Pressure compensator", "response": 149},
#  {"name": "Steam generator", "response": 40},
# ])
# Warning! Polar crane has a slow response of 52 ms. Pay attention!
# Alarm! Reactor shaft has a very slow response of 81 ms. Needs to be repaired!
# Nuclear power station is in danger! Pressure compensator has a dangerously slow response of 149 ms. We are in serious trouble!

check_station_devices([
  {"name": "Reactor shaft", "response": 40},
  {"name": "Polar crane", "response": 25},
  {"name": "Steam generator", "response": 11},
  {"name": "Pressure compensator", "response": 50},
])
# Responses of all devices does not exceed the norm.
