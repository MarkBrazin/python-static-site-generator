from pathlib import Path

class Site:
    def __init__(self,source,dest):
        source=Path(self.source) 
        dest=Path(self.dest) 


    def create_dir(self,path):
        directory      =    self.dest / relative_to(self.source)


        