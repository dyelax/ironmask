from button_control import button_is_pressed, cleanup
from servo_control import open_mask, close_mask

mask_open = False
toggle_ready = True

if __name__ == '__main__':
  try:
    while True:
      if button_is_pressed():
        print("button pressed")
        if toggle_ready:
          if mask_open:
            close_mask()
          else:
            open_mask()

        toggle_ready = False
      else:
        toggle_ready = True

  except KeyboardInterrupt:
    cleanup()
