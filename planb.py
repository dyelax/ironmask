from button_control import button_is_pressed, cleanup
from servo_control import open_mask, close_mask

mask_open = False
toggle_ready = True

if __name__ == '__main__':
  try:
    while True:
      if button_is_pressed():
        if toggle_ready:
          if mask_open:
            print("close mask")
            close_mask()
          else:
            print("open mask")
            open_mask()

        toggle_ready = False
      else:
        toggle_ready = True

  except KeyboardInterrupt:
    cleanup()
