import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now

BUTTON_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # initial value  = off

def button_is_pressed():
	return (GPIO.input(BUTTON_PIN) == GPIO.HIGH)
	
try:
	last_state = GPIO.LOW
	
	while True:
		current_state = GPIO.input(BUTTON_PIN)
		
		if current_state == GPIO.HIGH and last_state == GPIO.LOW:
			print(button_is_pressed())
			print("BUTTON PUUUUUUUSHHHHH!!!!!!!!!!")
		
		last_state = current_state
except KeyboardInterrupt:
	GPIO.cleanup()

print(button_is_pressed())


GPIO.cleanup() # Clean up
