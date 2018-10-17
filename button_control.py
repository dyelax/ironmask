import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now

BUTTON_PIN = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # initial value  = off

try:
	while True:
		if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
			print("BUTTON PUUUUUUUSHHHHH!!!!!!!!!!")
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
