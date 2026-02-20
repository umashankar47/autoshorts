import speech_recognition as sr
from pydub import AudioSegment

audio_file = 'D:/DP/pyTon Env Testing/RedVidtoYt/Source.mp3'
# Extract audio and transcribe
###
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    # print(audio_file)
    audio = AudioSegment.from_file(audio_file)
    audio.export("temp.wav", format="wav")
    
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        # text = recognizer.recognize_google(audio_data)
        text = recognizer.recognize_whisper(audio_data)
    return text

# Get transcription
transcription = transcribe_audio("D:/DP/pyTon Env Testing/RedVidtoYt/Source.mp3")
print(transcription)


