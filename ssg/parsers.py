from os import read
from typing import List
from pathlib import Path

class Parser:
    extensions: List[str]  =  []
    def valid_extension(self,extension):
        return extension in self.extensions
    
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedErrort
    
    def read(self,path):
        with open(path,'r') as file:
            return read(file)

        