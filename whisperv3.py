import whisper
from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")

def transcribe_audio(file_path):
    # Load the model
    model = whisper.load_model("base")

    # Transcribe the audio
    result = model.transcribe(file_path)

    # Print the transcribed text
    print("Transcription: " + result["text"])

if __name__ == "__main__":
    mp3_file = r"your_file_.mp3"
    wav_file = r"your_file_.wav"

    # Uncomment the line below if you want to convert MP3 to WAV first
    # convert_mp3_to_wav(mp3_file, wav_file)
    
    # Transcribe the audio (use mp3_file or wav_file depending on your preference)
    transcribe_audio(mp3_file)
