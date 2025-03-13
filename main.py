import os 
import sys
from gnu import gcc
from java import Java
from ruby import ruby
from rust import rust
from go import go
from ada import ada
import tkinter as tk


class Language():
    def __init__(self):
        self.urls = []
        self.supportedLang = [ada(),go(),gcc(),Java(),ruby(),rust()]
        self.existingLang = []
        self.find_existing_lang()
        self.versions = {"ada":ada().versions,"go":go().versions,"c/cpp":["Latest"],"rust":["Latest"],"ruby":[1.8,1.9,2.0,2.1,"Latest"],"java":[8,11,15,17,23]}
        
        

    def find_existing_lang(self):
        for lang in self.supportedLang:
            if lang.detect() == True:
                self.existingLang += [lang.name] 
            
    def run(self,choice,version):
        choiceMenu = {"go":go().run,"gnu":gcc().run,"rust":rust().run,"ruby":ruby().run,"java":Java().run}
        choiceMenu[choice](version)


if __name__ == "__main__":
    pass
        