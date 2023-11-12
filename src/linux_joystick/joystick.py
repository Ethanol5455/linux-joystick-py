from typing_extensions import Self


class XBOX_CONSTANTS:
    """Tested using xpadneo"""

    ### Axis IDs:
    L_STICK_X_ID = 0
    L_STICK_Y_ID = 1
    LT_ID = 2
    R_STICK_X_ID = 3
    R_STICK_Y_ID = 4
    RT_ID = 5
    D_PAD_X_ID = 6
    D_PAD_Y_ID = 7
    TRIGGERS_COMBINED_ID = 8

    ### Button IDs
    A_BUTTON_ID = 0
    B_BUTTON_ID = 1
    X_BUTTON_ID = 2
    Y_BUTTON_ID = 3
    LB_BUTTON_ID = 4
    RB_BUTTON_ID = 5
    BACK_BUTTON_ID = 6
    START_BUTTON_ID = 7
    XBOX_BUTTON_ID = 8
    LT_BUTTON_ID = 9
    RT_BUTTON_ID = 10


class ButtonEvent:
    id: int
    value: bool


class AxisEvent:
    MAX_AXIS_VALUE = 32767
    MIN_AXIS_VALUE = -32768

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
