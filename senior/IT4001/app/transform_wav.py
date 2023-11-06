from pydub import AudioSegment
import os

def convert_m4a_to_wav(input_path, output_path):
    audio = AudioSegment.from_file(input_path, format="m4a")
    audio.export(output_path, format="wav")

input_file = "scenario_01.m4a"
output_file = "scenario_01.wav"

convert_m4a_to_wav(input_file, output_file)

print(f"File converted from {input_file} to {output_file}")
