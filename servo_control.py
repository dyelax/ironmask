import RPi.GPIO as GPIO
import time

SERVO_PIN = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)

p = GPIO.PWM(SERVO_PIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

def servo_test():
	try:
		while True:
			for x in range(10, 20, 1):
				p.ChangeDutyCycle(x/2.0)
				time.sleep(0.03)

			for x in range(20, 10, -1):
				p.ChangeDutyCycle(x/2.0)
				time.sleep(0.03)
	except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()

def mask_off():
	try:
		for x in range(5, 10, 0.5):
			p.ChangeDutyCycle(x)
			time.sleep(0.03)
	except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()

def mask_on():
	try:
		for x in range(10, 5, -0.5):
			p.ChangeDutyCycle(x)
			time.sleep(0.03)
	except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()
