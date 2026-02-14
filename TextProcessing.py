from os import path
import json

class TextProcessing:
    def __init__(self, text_file:str=None):
        self.this_folder = path.dirname(path.abspath(__file__))
        self.data = path.join(self.this_folder, 'data\\formated_data')
        self.raw_text = self._read_text_file(f"{self.data}\\{text_file}")

    def _read_text_file(self, text_file:str):
        """Get the content of a text file

        Args:
            text_file (str): The name of the text file to read

        Returns:
            str: The content of the text file
        """
        with open(text_file, 'r', encoding='utf-8') as file:
            jsonString = file.read()
            data = json.loads(jsonString)
        return data["content"]

    def _flatten_dict(self):
        text_as_list = []
        for vers in self.raw_text.values():
            for v in vers.values():
                text_as_list.append(v)
        # print(text_as_list)
        return " ".join(text_as_list)

    def main(self):
        text = self._flatten_dict()
        print(text)

if __name__ == "__main__":
    processor = TextProcessing(text_file="Je suis.json")
    processor.main()