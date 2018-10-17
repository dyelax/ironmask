from flask import Flask, request
from flask_cors import CORS
from wit import Wit
from pydub import AudioSegment
import mimetypes
import json
import os
from pprint import pprint
import RPi.GPIO as GPIO
import time

# ------------------------------------- WIT ------------------------------------
WIT_PUB_KEY = 'DKZUYDUTBR3Z5XN6XR4VB2ORKLH7TJDT'
wit_client = Wit(WIT_PUB_KEY)

app = Flask(__name__)
CORS(app)

def test_wit_response():
	with open('test-audio/close-mask-verbose.mp3', 'rb') as f:
		act_on_wit_response(f)

def to_mp3(in_path, out_path):
	AudioSegment.from_file(in_path).export(out_path, format="mp3")

def act_on_wit_response(audio_file):
	# get wit response
	wit_res = wit_client.speech(audio_file, headers={'Content-Type': 'audio/mpeg3'})['entities']
	
	# determine if mask on/off and act
	# TODO: play with confidence levels
	if any(x for x in wit_res['intent'] if (x['value'] == 'mask' and x['confidence'] > 0.9)):
		if any(x for x in wit_res['on_off'] if (x['value'] == 'on' and x['confidence'] > 0.5)):
			print('on')
			mask_on()
		elif any(x for x in wit_res['on_off'] if (x['value'] == 'off' and x['confidence'] > 0.5)):
			print('off')
			mask_off()

test_wit_response()

# def parse_wit_response(res):
#
#
# @app.route('/voice', methods=['POST'])
# def voice_control():
#   audio_file = request.files['speech']
#   orig_ext = os.path.splitext(audio_file.filename)[1]
#
#   if orig_ext == '.mp3':
#     res = get_wit_response(audio_file)
#   else:
#     orig_path = '/tmp/ironmask' + orig_ext
#     if os.path.exists(orig_path):
#       os.remove(orig_path)
#
#     mp3_path = '/tmp/ironmask.mp3'
#     if os.path.exists(mp3_path):
#       os.remove(mp3_path)
#
#     audio_file.save(orig_path)
#     to_mp3(orig_path, mp3_path)
#
#     with open(mp3_path, 'rb') as f:
#       res = get_wit_response(f)
#
#   return json.dumps(res)

# ------------------------------------ SERVO -----------------------------------
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

def servo_test():
	try:
		while True:
			for x in range(5, 10, 0.5):
				p.ChangeDutyCycle(x)
				time.sleep(0.03)

			for x in range(10, 5, -0.5):
				p.ChangeDutyCycle(x)
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
