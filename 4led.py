**4 LED Blinking Pattern Using Raspberry Pi** [cite: 27, 26]

This practical involves creating a blinking pattern with four LEDs connected to your Raspberry Pi. Here's how you can set it up:

**Hardware Requirements:**

* Raspberry Pi Model A/B/B+
* 4 LEDs
* Jumper wires (Female to Female)
* Breadboard

**Software Requirements:**

* Raspbian Stretch OS
* Python 3

**Steps:**

1. **Connect the LEDs:** Connect the positive leg (longer lead) of each LED to GPIO pins 11, 13, 15, and 16 on your Raspberry Pi through the breadboard. Connect the negative leg (shorter lead) of each LED to a ground (GND) pin on the Raspberry Pi through the breadboard. [cite: 27, 26]

2. **Write the Python Code:** Open a text editor and paste the following Python code:

```python
import RPI.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

for i in range(5):
    GPIO.output(11,True)
    print("ON")
    GPIO.output(11,False)
    print("OFF")
    GPIO.output(13, True)
    print("ON")
    GPIO.output(13,False)
    print("OFF")
    GPIO.output(15, True)
    print("ON")
    GPIO.output(15,False)
    print("OFF")
    GPIO.output(16, True)
    print("ON")
    GPIO.output(16,False)
    print("OFF")

print("Done")
GPIO.cleanup()
```

3. **Save the Code:** Save the code as a Python file (e.g., "4led_blink.py"). [cite: 27, 26]

4. **Run the Code:** Open a terminal window and navigate to the directory where you saved the Python file. Execute the code using the command `python3 4led_blink.py`. [cite: 27, 26]

**Explanation:**

* The code initializes the GPIO pins and sets them as outputs.
* It then loops through a sequence of turning each LED on and off with a delay in between.
* The `print` statements indicate the on/off state of the LEDs in the terminal.
* Finally, it cleans up the GPIO configuration.

**Output:**

You should observe the four LEDs blinking in sequence, one at a time, repeatedly. The terminal will display "ON" and "OFF" messages corresponding to the LED states. [cite: 27, 26]
