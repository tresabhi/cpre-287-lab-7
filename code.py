import time
import board
import analogio

INPUT_VOLTAGE = 2.57
PIN_MAX = 51000

analog_pin = analogio.AnalogIn(board.A0)

def get_voltage(pin):
    return (pin.value * INPUT_VOLTAGE) / PIN_MAX

while True:
    v = get_voltage(analog_pin)
    print(f"v = {v:.3g}V")
    time.sleep(0.1)
