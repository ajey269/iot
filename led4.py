import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

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
  GPIO.output(16, True)
  print("ON")
  GPIO.output(16, False)
  print("OFF")

print("Done")
GPIO.cleanup()
