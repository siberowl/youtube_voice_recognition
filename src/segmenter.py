import pydub as pd


def save_segment(input_path, output_path, start, finish):
    audio = pd.AudioSegment.from_wav(input_path)
    segment = audio[start:finish]
    segment.export(output_path, format="wav")
