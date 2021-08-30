import pydub as pd


class Segmenter:
    def load(self, input_path):
        self.audio = pd.AudioSegment.from_file(input_path, format="webm")

    def save_segment(self, output_path, start, finish):
        segment = self.audio[start:finish]
        segment.export(output_path, format="wav")
