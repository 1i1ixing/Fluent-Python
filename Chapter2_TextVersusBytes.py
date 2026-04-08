# Encode and Decode
s = 'café' 
print(len(s))
b = s.encode('utf-8') # Unicode characters that can be represented in UTF-8 Bytes encoding.
print(b)
print(len(b))
print(b.decode('utf-8')) # Decoding the bytes back to a Unicode string using UTF-8 encoding.

# Bytes
cafe = bytes('café', encoding='utf-8')
print(cafe)
print(cafe[0]) # each item in bytes or bytearray is an integer in the range 0-255 representing a byte value.
print(cafe[:1]) # a slice of a binary sequence always produce a binary sequence of the same type.
print(cafe[-1:])

# BOM (Byte Order Mark)
print('El Niño'.encode('utf-16')) # b'\xff\xfeE denote little endian
print('El Niño'.encode('utf-16le')) # explicatly little endian
print('El Niño'.encode('utf-16be')) # explicatly big endian

# Normalizing Unicode
from unicodedata import normalize
s1 = 'café'  # composed "e" with acute accent
s2 = 'cafe\u0301'  # decomposed "e" and acute accent
print(len(s1), len(s2))
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2)) # composed normalization
print(normalize('NFD', s1) == normalize('NFD', s2)) # decomposed normalization

# Sorting
import pyuca # The pyuca library provides a Unicode Collation Algorithm implementation for sorting Unicode strings according to their linguistic rules.
coll = pyuca.Collator() # Otherwise, you need to import locale, and use locale.setlocale(locale.LC_COLLATE, <<your_locale>>) and sorted(, key=locale.strxfrm) for sorting
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)
