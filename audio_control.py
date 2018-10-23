import pyaudio
import wave

from button_control import button_is_pressed

p = pyaudio.PyAudio()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = int(p.get_device_info_by_index(0)['defaultSampleRate'])


def record(output_path='/tmp/ironmask.wav'):
  stream = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

  print("* start recording")

  frames = []
  while button_is_pressed():
    # for i in range(0, int(RATE / CHUNK * 5)):
    data = stream.read(CHUNK, exception_on_overflow=False)
    frames.append(data)

  print("* done recording")

  stream.stop_stream()
  stream.close()
  # p.terminate()

  wf = wave.open(output_path, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(b''.join(frames))
  wf.close()

  return output_path


if __name__ == '__main__':
  record()
