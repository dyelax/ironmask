from audio_control import record
from wit_control import get_wit_response
from button_control import button_is_pressed, cleanup
from servo_control import mask_on, mask_off


def act_on_wit_response(res):
  try:
    entities = res['entities']

    # determine if mask on/off and act
    # TODO: play with confidence levels
    if any(x for x in entities['intent'] if (x['value'] == 'mask')):
      if any(x for x in entities['on_off'] if (x['value'] == 'on')):
        print('on')
        mask_on()
      elif any(x for x in entities['on_off'] if (x['value'] == 'off')):
        print('off')
        mask_off()
  except KeyError:
    print('Bad response. Try again.')


if __name__ == '__main__':
  try:
    while True:
      if button_is_pressed():
        print("button pressed")

        audio_path = record()
        res = get_wit_response(audio_path)
        print(res)
        act_on_wit_response(res)

  except KeyboardInterrupt:
    cleanup()
