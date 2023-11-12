import time

from linux_joystick import AxisEvent, ButtonEvent, Joystick

js = None
while True:
    while True:
        try:
            # Create joystick device (/dev/input/js0)
            # Joystick creation will fail with FileNotFoundError if device does not exist
            js = Joystick(0)
            break
        except FileNotFoundError:
            print("Controller not connected. Retrying in 5 seconds...")
            time.sleep(5)

    print("Controller connected!")
    while True:
        event = None
        try:
            # Get next event (blocking)
            # poll() will fail with OSError if device is disconnected while polling
            event = js.poll()
        except OSError:
            break

        if isinstance(event, AxisEvent):
            print(f"Axis {event.id} is {event.value}")
        elif isinstance(event, ButtonEvent):
            print(f"Button {event.id} is {event.value}")
