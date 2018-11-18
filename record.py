import pyaudio
import wave
import time

current_milli_time = lambda: int(round(time.time() * 1000))

WAVE_OUTPUT_FILENAME = "/tmp/out.wav"
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 512
RECORD_SECONDS = 10
device_index = 2
audio = pyaudio.PyAudio()
index = 1

stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,input_device_index = index,
                frames_per_buffer=CHUNK)
Recordframes = []

print("recording started")
start=current_milli_time()
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    Recordframes.append(data)
end=current_milli_time()
print("recording stopped, total ms recorded = ", str(end - start))

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(Recordframes))
waveFile.close()

# BASE: https://stackoverflow.com/questions/40704026/voice-recording-using-pyaudio
