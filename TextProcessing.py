from os import path
import json

class TextProcessing:
    def __init__(self, text_file:str=None):
        self.this_folder = path.dirname(path.abspath(__file__))
        self.data = path.join(self.this_folder, 'data\\formated_data')
        self.text = _read_text_file(self, text_file)

def _read_text_file(self, text_file:str):
    """Get the content of a text file

    Args:
        text_file (str): The name of the text file to read

    Returns:
        str: The content of the text file
    """
    with open(f"{self.data}\\{text_file}", 'r', encoding='utf-8') as file:
        jsonString = file.read()
        data = json.loads(jsonString)
        print(data["content"])

if __name__ == "__main__":
    processor = TextProcessing(text_file="Je suis.json")