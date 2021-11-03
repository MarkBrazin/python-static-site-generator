from os import read
from typing import List
from pathlib import Path

class Parser:
    extensions: List[str]  =  []
    def valid_extension(self,extension):
        return extension in self.extensions
    
    def valid_extensions (self,extensions):
        return extensions in self.extensions
    
    def read(self,path):
        with open(path,'r') as file:
            return read(file)

        