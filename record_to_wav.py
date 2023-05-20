import pyaudio
import wave
import keyboard
import speech_recognition as sr
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILENAME = "recording.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording started. Press Ctrl+C to stop recording.")

frames = []

while not ( keyboard.is_pressed('space') ):
    print("Hold down the Space bar...")
    time.sleep(.5)

while keyboard.is_pressed('space'):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording stopped.")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Recording saved as {OUTPUT_FILENAME}.")
