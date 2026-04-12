# Iterables
## an object is considered iterable not only when it implements the special method __iter__,
## but also when it implements __getitem__, as long as __getitem__ accepts int keys starting from 0.
## Whenever the interpreter needs to iterate over an object x, it automatically calls iter(x)，
## If __iter__ is not implemented, but __getitem__ is implemented, Python creates
## an iterator that attempts to fetch items in order, starting from index 0 (zero).
import re
import reprlib
RE_WORD = re.compile('\w+')
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  

    def __getitem__(self, index):
        return self.words[index] 
      
    def __len__(self):   
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

s = Sentence('"The time has come," the Walrus said,')
print(s)
for word in s: # s is iterable, since it implements __getitem__
    print(word)

# Ierators: Python obtains iterators from iterables, that sequence is always iterable
s3 = Sentence('Lixing Liu')
it = iter(s3)
print(it)
print(next(it))
print(next(it))
print(next(it)) # Stop Iteration error

# Relationship between iterables and iterators example
import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self): # Sentense is iterable since it implements __iter__
        return SentenceIterator(self.words) # __iter__ fulfills the iterable protocol by instantiating and returning an iterator.
      
class SentenceIterator:
    def __init__(self, words):
        self.words = words   
        self.index = 0   
    def __next__(self): #  iterators are supposed to implement both __next__ and __iter__
        try:
            word = self.words[self.index]   
        except IndexError:
            raise StopIteration()   
        self.index += 1   
        return word   
    def __iter__(self):   
        return self

# Generator Function: they are iterators that produce the values of the expressions pass to "yield", so use next() to a generator
import re
import reprlib
RE_WORD = re.compile('\w+')
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        '''
        __iter__ is a generator function which, when called, builds a generator object that implements the
        iterator interface, so the SentenceIterator class is no longer needed.
        '''
        for word in self.words:   
            yield word
        return 
    
# Generator Expression and Lasy Implementation: generator expression produces a generator
import re
import reprlib
RE_WORD = re.compile('\w+')
class Sentence:
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        '''
        RE_WORD.finditer(self.text) is a generator, it would not build an iterable in advance, which is opposite to RE_WORD.findall(text)
        call iter returns a generator because of the generator expression
        '''
        return (match.group() for match in RE_WORD.finditer(self.text))
