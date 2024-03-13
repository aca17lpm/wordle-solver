# Have a txt file of 475k words https://github.com/dwyl/english-words/tree/master
# Need to get all 5 letter words

import re

def clean(string : str):
    string = string.strip()
    string = string.lower()
    return string

def word_conditions(word : str):
    return [
        (len(word) == 5),
        (all(char.isalpha() for char in word)),
    ]

def main():
    fivers = []
    with open('words.txt', 'r') as f:
        for word in f:
            if all(word_conditions(word.strip())):
                fivers.append(clean(word))
            
    with open('fivers.txt', 'w') as f:
        for fiver in fivers:
            f.write(fiver + '\n')
        
if __name__ == '__main__':
    main()