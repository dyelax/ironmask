import RPi.GPIO as GPIO

BUTTON_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # initial value  = off


def button_is_pressed():
  return (GPIO.input(BUTTON_PIN) == GPIO.HIGH)


def cleanup():
  GPIO.cleanup()