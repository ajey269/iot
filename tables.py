Certainly, here are the pin tables for each practical involving interfacing with the Raspberry Pi:

**1. LED Blinking Patterns**

* **Single LED, Three LEDs, and Four LEDs:**

|LED Terminal|Pin Number|GPIO Number|
|:---|:---|:---|
|Led Positive|Pin 11|GPIO 17|
|Led Negative|Pin 6|Ground| [cite: 60]

**2. 4-Digit 7-Segment Display**

|TM1637 Board Pin|Function|RPI Physical Pin|Raspberry Function|
|:---|:---|:---|:---|
|GND|Ground|GND|14|
|VCC|+ 5V Power|4|5V|
|DIO|Data In|18|GPIO 24|
|CLK|Clock|16|GPIO 23| [cite: 32]

**3.  Raspberry Pi based Oscilloscope**

|ADS1115 ADC|GPIO Number|Pin Number|
|:---|:---|:---|
|VDD|Pin 17|3.3v|
|GND|Pin 9|GND|
|SCL|Pin 5|GPIO 3|
|SDA|GPIO 2|Pin 3| [cite: 56]

**4.  Fingerprint Sensor interfacing with Raspberry Pi**

|Pin No|Pin Name|Details|
|:---|:---|:---|
|1|5V|Regulated 5V DC|
|2|GND|Common Ground|
|3|TXD|Data output - Connect to MCU RX|
|4|RXD|Data Input - Connect to MCU TX|
|5|TOUCH|Active Low output when there is touch on sensor by finger|
|6|3.3V|Use this wire to give 3.3V to sensor instead of 5V| [cite: 69]

**5.  Interfacing GPS module with Raspberry Pi**

|Neo 6m V2 GPS Board Pin|Details|Raspberry Pi Physical Pin|Raspberry Pi Function|
|:---|:---|:---|:---|
|VCC|Power|Pin 2|3.3V Power|
|GND|Common Ground|Pin 6|GND|
|TXD|Data Output|Pin 10|(UART\_RXD0) GPIO15|
|RXD|Data Input|Not required|(UART\_TXD0) GPIO14| [cite: 100]

**6.  Interface Raspberry Pi with Pi Camera**

No pin table is available for this practical.

**7.  Interfacing Raspberry Pi with RFID**

|RFID Reader Board Pin|RPI Physical Pin|Raspberry Function|
|:---|:---|:---|
|SDA|24|GPIO8 (SPI\_CEO\_N)|
|SCK|23|GPIO11 (SP10-\_CLK)|
|MOSI|19|GPIO10 (SPIO\_MOSI)|
|MISO|21|GPIO9 (SPIO\_MISO)|
|IRQ|NOT USED|
|GND|6|GND|
|RST|22|GPIO25 (GPIO\_GEN6)|
|3.3V|1|3.3V PWR| [cite: 133]
