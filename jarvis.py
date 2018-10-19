from audio_control import record
from wit_control import get_wit_response
# from button_control import button_is_pressed, cleanup
# from servo_control import mask_on, mask_off
#
# def act_on_wit_response(res):
#   entities = res['entities']
#
#   # determine if mask on/off and act
#   # TODO: play with confidence levels
#   if any(x for x in entities['intent'] if (x['value'] == 'mask' and x['confidence'] > 0.9)):
#     if any(x for x in entities['on_off'] if (x['value'] == 'on' and x['confidence'] > 0.5)):
#       print('on')
#       mask_on()
#     elif any(x for x in entities['on_off'] if (x['value'] == 'off' and x['confidence'] > 0.5)):
#       print('off')
#       mask_off()


if __name__ == '__main__':
  # try:
  #   while True:
	 #  # if button is pressed
  #     if button_is_pressed():
  #       print("button pressed")
  #
  #       # TODO: fix "Input overflowed"
  #       audio_path = record('/tmp/ironmask.wav')
  #       # res = get_wit_response(audio_path)
  #       res = get_wit_response('/tmp/ironmask.wav')
  #       # act_on_wit_response(res)
  #       print(res)
  # except KeyboardInterrupt:
  #   cleanup()

  audio_path = record()
  res = get_wit_response(audio_path)
  print(res)
  # act_on_wit_response(res)
