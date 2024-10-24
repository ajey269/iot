**Single LED Blinking**

1. **Connect the LED:** Connect the positive (longer) leg of the LED to GPIO pin 11 on the Raspberry Pi. Connect the negative (shorter) leg to a GND pin. [cite: 26, 60]

2. **Write the Code:**
   ```python
   import RPi.GPIO as GPIO
   import time

   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(11, GPIO.OUT)

   for i in range(5):
       GPIO.output(11, True)
       print("ON")
       time.sleep(1)
       GPIO.output(11, False)
       print("OFF")
       time.sleep(1)

   print("Done")
   GPIO.cleanup()
   ```

3. **Run the Code:** Save the code (e.g., as `single_led.py`) and run it using `python3 single_led.py`.

**Three LED Blinking**

1. **Connect the LEDs:** Connect the positive legs of three LEDs to GPIO pins 11, 13, and 15. Connect the negative legs to GND. [cite: 26, 60]

2. **Write the Code:**
   ```python
   import RPi.GPIO as GPIO
   import time

   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(11, GPIO.OUT)
   GPIO.setup(13, GPIO.OUT)
   GPIO.setup(15, GPIO.OUT)

   for i in range(5):
       GPIO.output(11, True)
       print("ON")
       GPIO.output(11, False)
       print("OFF")
       GPIO.output(13, True)
       print("ON")
       GPIO.output(13, False)
       print("OFF")
       GPIO.output(15, True)
       print("ON")
       GPIO.output(15, False)
       print("OFF")

   print("Done")
   GPIO.cleanup()
   ```

3. **Run the Code:** Save the code (e.g., as `three_led.py`) and run it using `python3 three_led.py`.
