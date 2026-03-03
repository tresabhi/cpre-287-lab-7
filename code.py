import time
import board
import analogio

INPUT_VOLTAGE = 2.5
PIN_MAX = 51000

analog_pin = analogio.AnalogIn(board.A0)

def get_voltage(pin):
    return (pin* INPUT_VOLTAGE) / PIN_MAX

while True:
    adc = analog_pin.value
    v = get_voltage(adc)
    print(f"v = {v:.3g}V\tadc = {adc}")
    time.sleep(0.1)
