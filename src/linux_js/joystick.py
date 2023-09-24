from typing_extensions import Self


class ButtonEvent:
    id: int
    value: bool


class AxisEvent:
    id: int
    value: int


class Joystick:
    def __init__(self: Self, device_number: int):
        self._device_number = device_number
        self._file = open(f"/dev/input/js{device_number}", "rb")

    def poll(self: Self) -> None | ButtonEvent | AxisEvent:
        buffer = self._file.read(8)
        input_value = int.from_bytes(buffer[4:6], "little", signed=True)
        input_type = int.from_bytes([buffer[6]], "little", signed=False)
        input_id = int.from_bytes([buffer[7]], "little", signed=False)

        if input_type == 1:
            event = ButtonEvent()
            event.id = input_id
            event.value = input_value == 1
            return event
        elif input_type == 2:
            event = AxisEvent()
            event.id = input_id
            event.value = input_value
            return event
        return None
