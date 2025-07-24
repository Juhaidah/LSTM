import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg

data = gutenberg.raw('shakespeare-hamlet.txt')
with open('hamlet.txt', 'w') as file:
    file.write(data)