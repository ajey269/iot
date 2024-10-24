**Hardware Requirements:**

1. Raspberry Pi Model A/B/B+
2. ADS1115 ADC
3. Breadboard
4. Jumper Wires [cite: 47, 48, 49, 50, 51, 52, 53, 54]

**Software Requirements:**

1. Raspbian Stretch OS
2. Adafruit module for interfacing with the ADS1115 ADC chip
3. Python Module matplotlib used for data visualization [cite: 47, 48, 49, 50, 51, 52, 53, 54]

**Steps:**

1. **Connect the ADC:** Connect the ADS1115 ADC to the Raspberry Pi's GPIO pins. Refer to the pinout diagram for your specific ADC model. [cite: 55, 56]

2. **Install Dependencies:** Install the required libraries:
   ```bash
   sudo pip3 install adafruit-circuitpython-ads1x15
   sudo pip3 install adafruit-blinka
   ```

3. **Clone Repository:** Clone the Adafruit ADS1x15 repository:
   ```bash
   git clone https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15
   ```

4. **Run Example Code:** Navigate to the examples directory and run the `ads1x15_simpletest.py` script:
   ```bash
   cd Adafruit_CircuitPython_ADS1x15/examples
   python3 ads1x15_simpletest.py
   ```

**Code:**
```python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format("raw", "v"))

while True:
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    time.sleep(0.5)
```
**Explanation:**

* The provided code reads the analog input from channel 0 of the ADS1115 ADC and prints the raw and voltage values.
* You can modify the code to read from other channels or to plot the data on a graph using the matplotlib library.

**Additional Notes:**

* The ADS1115 is a 16-bit ADC, providing higher resolution than the 12-bit MCP3008.
* You can adjust the sampling rate and gain of the ADS1115 to suit your needs.
* For more advanced oscilloscope functionalities, you can explore libraries like `drawnow` for real-time plotting and consider using a graphical user interface (GUI) for better visualization.
