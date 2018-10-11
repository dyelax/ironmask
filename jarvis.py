from flask import Flask, request
from flask_cors import CORS

from wit import Wit
from pydub import AudioSegment
import mimetypes
import json
import os
from pprint import pprint

WIT_PUB_KEY = 'DKZUYDUTBR3Z5XN6XR4VB2ORKLH7TJDT'
wit_client = Wit(WIT_PUB_KEY)

app = Flask(__name__)
CORS(app)


# def test_wit_response():
#   with open('test-audio/close-mask-verbose.mp3', 'rb') as f:
#     return get_wit_response(f)

def to_mp3(in_path, out_path):
  AudioSegment.from_file(in_path).export(out_path, format="mp3")

def get_wit_response(audio_file):
  return wit_client.speech(audio_file, headers={'Content-Type': 'audio/mpeg3'})

def parse_wit_response(res):


@app.route('/voice', methods=['POST'])
def voice_control():
  audio_file = request.files['speech']
  orig_ext = os.path.splitext(audio_file.filename)[1]

  if orig_ext == '.mp3':
    res = get_wit_response(audio_file)
  else:
    orig_path = '/tmp/ironmask' + orig_ext
    if os.path.exists(orig_path):
      os.remove(orig_path)

    mp3_path = '/tmp/ironmask.mp3'
    if os.path.exists(mp3_path):
      os.remove(mp3_path)

    audio_file.save(orig_path)
    to_mp3(orig_path, mp3_path)

    with open(mp3_path, 'rb') as f:
      res = get_wit_response(f)

  return json.dumps(res)


