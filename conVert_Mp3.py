from pydub import AudioSegment
from pydub.utils import which
import os
import pyfiglet

AudioSegment.converter = which("ffmpeg")

def display_title():
    ascii_title = pyfiglet.figlet_format("ConVert.mp3")
    print(ascii_title)

def convert_wav_to_mp3(input_wav, output_mp3, bitrate="128k", sample_rate=44100):
    print("\nProcessing Conversion...\n")
    audio = AudioSegment.from_wav(input_wav)
    
    audio_re = audio.set_frame_rate(sample_rate)

    audio_re.export(output_mp3, format="mp3", bitrate=bitrate)
    print(f"Conversion Complete: {output_mp3}")

if __name__== "__main__":
    display_title()

    input_wav = input("Enter Path to WAV file: ").strip()
    if not os.path.isfile(input_wav):
        print("Error: File Not Found.")
        exit(1)

    output_mp3 = input("Enter the output Mp3 desired file path including file name: ").strip()
    bitrate = "128k"
    sample_rate = 44100

    try:
        sample_rate = int(sample_rate) if sample_rate else 44100
    except ValueError:
        print("invalid sample rate. Going default. ")
        sample_rate = 44100

    convert_wav_to_mp3(input_wav, output_mp3, bitrate, sample_rate)

