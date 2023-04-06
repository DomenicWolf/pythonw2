"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    


    def __init__(self,path):
        self.path = path
        file = open(path)
        counter = 0
        for line in file:
            counter += 1
        file.close()

        print(f"{counter} files read") 

    def random(self):
        file = open(self.path)
        words = [word.strip() for word in file]

        return random.choice(words)

class SpecialWordFinder(WordFinder):

    def __init__(self,path):
        super.__init__(path)

    def random(self):
         file = open(self.path)
         words = [word.strip() for word in file if word.strip() and not word.startswith("#")] 
         return random.choice(words)

        


