import time
import board
import analogio

adc_to_V = 2.57 / 51000
c_to_mV = 10
c_to_V = c_to_mV / 1000
V_to_c = 1 / c_to_V

analog_pin = analogio.AnalogIn(board.A0)

while True:
    adc = analog_pin.value
    v = adc * adc_to_V
    t = V_to_c * v

    print(f"adc = {adc}\tv = {v:.3g}V\tt = {t:.3g}deg")

    time.sleep(0.1)
