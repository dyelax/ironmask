import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now

BUTTON_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # initial value  = off


def button_callback(channel):
	print("BUTTON PUUUUUUUSHHHHH!!!!!!!!!!")
	
GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback)

def button_is_pressed():
	return (GPIO.input(BUTTON_PIN) == GPIO.HIGH)

GPIO.cleanup() # Clean up
