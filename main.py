import pyaudio
import keyboard
import speech_recognition as sr
import time

def record_speech():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("Recording started. Hold down Space bar to record...")
    
    frames = []

    while not ( keyboard.is_pressed('space') ):
        print("Hold down the Space bar...")
        time.sleep(1)

    while keyboard.is_pressed('space'):
        #print("Keyboard pressed...")
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("Recording stopped.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return frames

def transcribe_audio(frames):
    audio_data = b''.join(frames)
    
    r = sr.Recognizer()
    with sr.AudioFile(audio_data) as source:
        audio = r.record(source)
        
    try:
        transcript = r.recognize_google(audio)
        return transcript
    except sr.UnknownValueError:
        return "Unable to recognize speech."
    except sr.RequestError:
        return "Speech recognition service unavailable."

# Main program
if __name__ == '__main__':
    frames = record_speech()
    transcript = transcribe_audio(frames)
    print("Transcript:", transcript)
