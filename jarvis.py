from wit import Wit

client = Wit('DKZUYDUTBR3Z5XN6XR4VB2ORKLH7TJDT')

with open('test-audio/close-mask.m4a') as f:
  res = client.speech(f, headers={'Content-Type': 'audio/m4a'})
  print(res)
