# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_icg20660 import icg20660

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
icg = icg20660.ICG20660(i2c)

icg.acceleration_range = icg20660.RANGE_8G

while True:
    for acceleration_range in icg20660.acceleration_range_values:
        print("Current Acceleration range setting: ", icg.acceleration_range)
        for _ in range(10):
            accx, accy, accz = icg.acceleration
            print(f"x:{accx:.2f}m/s2, y:{accy:.2f}m/s2, z{accz:.2f}m/s2")
            print()
            time.sleep(0.5)
        icg.acceleration_range = acceleration_range
