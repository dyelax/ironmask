from wit import Wit
from pydub import AudioSegment
import os

WIT_PUB_KEY = 'DKZUYDUTBR3Z5XN6XR4VB2ORKLH7TJDT'
wit_client = Wit(WIT_PUB_KEY)


def to_mp3(in_path, out_path):
  AudioSegment.from_file(in_path).export(out_path, format="mp3")


def wit_mp3(audio_file):
  return wit_client.speech(audio_file, headers={'Content-Type': 'audio/mpeg3'})


def get_wit_response(audio_path='test-audio/close-mask-verbose.mp3'):
  with open(audio_path, 'rb') as f:
    orig_ext = os.path.splitext(audio_path)[1]

    if orig_ext == '.mp3':
      res = wit_mp3(f)
    else:
      mp3_path = '/tmp/ironmask.mp3'
      to_mp3(audio_path, mp3_path)

      with open(mp3_path, 'rb') as f:
        res = wit_mp3(f)

    return res
