from audio_control import record
from wit_control import get_wit_response
from button_control import button_is_pressed, cleanup
from servo_control import open_mask, close_mask


def act_on_wit_response(res):
  try:
    entities = res['entities']

    if any(x for x in entities['intent'] if (x['value'] == 'mask')):
      if any(x for x in entities['on_off'] if (x['value'] == 'on')):
        print('on')
        open_mask()
      elif any(x for x in entities['on_off'] if (x['value'] == 'off')):
        print('off')
        close_mask()
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
