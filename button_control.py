import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now

BUTTON_PIN = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # initial value  = off

def button_callback:
	print("BUTTON PUUUUUUUSHHHHH!!!!!!!!!!")

GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback)

GPIO.cleanup()
