import RPi.GPIO as GPIO
import time

SERVO_PIN = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)

p = GPIO.PWM(SERVO_PIN, 50)  # GPIO 22 for PWM with 50Hz
p.start(2.5)  # Initialization

# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

# duty cycle for 0 degree = (0.5/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%


ANGLE_MASK_OPEN = 0
ANGLE_MASK_CLOSE = 180
DC_MASK_OPEN = 2.5
DC_MASK_CLOSE = 12.5
# DC_MASK_OPEN = 5
# DC_MASK_CLOSE = 8
SLEEP_TIME = 0.03


def servo_test():
  try:
    # while True:
    #   for x in range(10, 20, 1):
    #     p.ChangeDutyCycle(x / 2.0)
    #     time.sleep(0.03)
    #
    #   for x in range(20, 10, -1):
    #     p.ChangeDutyCycle(x / 2.0)
    #     time.sleep(0.03)

    while True:
      print('open')
      open_mask()
      time.sleep(1)
      print('close')
      close_mask()
      time.sleep(1)
  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()


def open_mask():
  move_mask(DC_MASK_CLOSE, DC_MASK_OPEN, step=-1)


def close_mask():
  move_mask(DC_MASK_OPEN, DC_MASK_CLOSE)


def move_mask(start_dc, end_dc, step=1):
  try:
    for dc in range(int(start_dc * 2), int(end_dc * 2), step * 2):
      p.ChangeDutyCycle(dc // 2)
      time.sleep(SLEEP_TIME)
  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
