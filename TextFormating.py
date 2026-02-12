import json
from os import path

class TextFormatter:
    def __init__(self, text_file:str=None, author:str=None, book:str=None, position:int=0):
        self.this_folder = path.dirname(path.abspath(__file__))
        self.raw_data_folder = path.join(self.this_folder, 'data\\raw_data')
        self.text_file = f"{self.raw_data_folder}\\{text_file}"
        self.title = text_file.split('.')[0]
        self.raw_text = self._read_text_file()
        self.author = author
        self.book = book
        self.position = position
    
    def __str__(self):
        # return f"TextFormatter(this_folder={self.this_folder}, raw_data_folder={self.raw_data_folder})"
        return self.raw_text
    
    def _read_text_file(self):
        """Get the content of a text file

        Returns:
            dict: The content of the text file separated by paragraphes 
        """
        with open(self.text_file, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    
    def enumerate_strophe(self):
        """Separate the text into strophes and enumerate them
        
        Returns:
            dict: A dictionary with the strophes as values and the keys as "strophe_1", "strophe_2", etc.
        """
        
        dict_strophes = {}
        for i, p in enumerate(self.raw_text.split('\n\n')):
            dict_strophes[f"strophe_{i+1}"] = p
        return dict_strophes   
      
    def enumerate_vers(self, text:str|dict=None):
        """Separate the text into vers and enumerate them
        
        Args:
            text (str|dict, optional): The text to separate into vers. If None, the raw text will be used. Defaults to None.
        
        Returns:
            dict: A dictionary with the vers as values and the keys as "vers_1", "vers_2", etc.
        """
        
        text = text if text is not None else self.raw_text
        dict_vers = {}
        i = 1
        if isinstance(text, dict):
            for key, value in text.items():
                # print(key)
                vers_dict = {}
                for vers in value.split("\n"):
                    # print(f"Vers {i} : {vers}")
                    vers_dict[f"vers_{i}"] = vers
                    i += 1
                dict_vers[key] = vers_dict
        return dict_vers
    
    def set_metadata(self, formatted_text:dict=None):
        """Set the metadata of the text file
        
        Args:
            formatted_text (dict, optional): The formatted text to set the metadata for. If None, the raw text will be used. Defaults to None.
            
        Returns:
            dict: A dictionary with the metadata of the text file and the formatted text
        """
        complete_file = {
            "author": self.author,
            "title": self.title,
            "book": self.book,
            "content": formatted_text,
            "position": self.position
        }
        return complete_file
    
    def create_json(self, formatted_text:dict=None):
        """Create a JSON file with the formatted text and the metadata"""
        with open(f"{self.this_folder}\\data\\formated_data\\{self.title}.json", "w", encoding='utf-8') as f:
            json.dump(formatted_text, f, indent=4, ensure_ascii=False)
    
    def main(self):
        """Main function to format the text file and set the metadata"""
        formatted_text = self.enumerate_strophe()
        formatted_text = self.enumerate_vers(text=formatted_text)
        complete_file = self.set_metadata(formatted_text)
        self.create_json(complete_file)

if __name__ == "__main__":
    formatter = TextFormatter(text_file="Je suis.txt", author="Daniel Escoval", book="Dialogues", position=1)
    formatter.main()
    