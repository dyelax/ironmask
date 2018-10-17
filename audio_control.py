import pyaudio
import wave

p = pyaudio.PyAudio()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
# RATE = int(p.get_device_info_by_index(0)['defaultSampleRate'])
RATE = 48000

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


def record(output_path='/tmp/ironmask.wav'):
  print("* start recording")

  frames = []
  # while button_is_pressed():  # TODO: change back to button once implemented
  for i in range(0, int(RATE / CHUNK * 5)):
    data = stream.read(CHUNK)
    frames.append(data)

  print("* done recording")

  stream.stop_stream()
  stream.close()
  p.terminate()

  wf = wave.open(output_path, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(b''.join(frames))
  wf.close()

  return output_path


if __name__ == '__main__':
    record()