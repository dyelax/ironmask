from wit_control import get_wit_response
from servo_control import *

def act_on_wit_response(res):
  entities = res['entities']

  # determine if mask on/off and act
  # TODO: play with confidence levels
  if any(x for x in entities['intent'] if (x['value'] == 'mask' and x['confidence'] > 0.9)):
    if any(x for x in entities['on_off'] if (x['value'] == 'on' and x['confidence'] > 0.5)):
      print('on')
      mask_on()
    elif any(x for x in entities['on_off'] if (x['value'] == 'off' and x['confidence'] > 0.5)):
      print('off')
      mask_off()


if __name__ == '__main__':
  res = get_wit_response('test-audio/close-mask.mp3')
  print(res)
  act_on_wit_response(res)
