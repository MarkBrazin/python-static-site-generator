from os import read
from typing import List
from pathlib import Path

class Parser:
    extensions: List[str]  =  []
    def valid_extension(self,extension):
        return extension in self.extensions
    
    
    def read(path):
        with open(path) as file:
            return read(file)

        