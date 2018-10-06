from wit import Wit

client = Wit('DKZUYDUTBR3Z5XN6XR4VB2ORKLH7TJDT')

with open('test-audio/close-mask-verbose.mp3', 'rb') as f:
  res = client.speech(f, headers={'Content-Type': 'audio/mpeg3'})
  print(res)

