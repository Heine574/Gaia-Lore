from random import randint
import urllib.request
from getch import *
import sys

word_site = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
gadoran_words = 'http://216.188.247.2/Universe/Andromeda%20Galaxy/Gadoran%20Empire/dictionary.py'

f = open('english_words', 'r')
WORDS = f.readlines()
f.close()
gad_file = open('gad_words.txt', 'a')

def print_line_break():
    pass
    #print('═══════════════════════════════════════════', file=gad_file)

def remove_word(word):
    f = open('english_words', 'r')
    words = f.readlines()
    f.close()

    for line in words:
        if not line == word + '\n':
            f.write(line)

def leagal_char(char, word, chars):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    #Rule 1, no triplets of characters:
    try:
        if word[-1] == char and word[-2] == char:
            return False
    except IndexError:
        pass

    #Rule 2, words that end with "n" must start with a vowel:
    if len(word) + 1 == chars: #check this is the last chaacter
        if char == 'n':
            if not word[0] in vowels:
                return False

    #Rule 3, no duoble consonants:
    try:
        if word[-1] in consonants and char in consonants:
            #Special cases:
            if char == 'd' and word[-2] in vowels:
                pass
            elif char == 'p':
                if word[-2] in consonants and word[-1] != 'd' and word[-1] in consonants:
                    return False
                else:
                    pass
            elif char == 'h':
                if word[-2] in consonants and word[-1] != 'p' and word[-1] in consonants:
                    return False
                else:
                    pass
            else:
                return False
    except IndexError:
        pass 

    #Rule 4, no duoble "u"s:
    try:
        if char == 'u' and word[-1] =='u':
            return False
    except IndexError:
        pass

    #Return True if char doesn't break any rules:
    return True

def generate_words():
    words = 200000#int(input('how many words: '))
    min_size = 2#int(input('minimum word length: '))
    max_size = 3#int(input('maximum word length: '))
    if max_size < min_size + 2:
                max_size += 3
    print_line_break()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(words):
        word = ''
        chars = randint(min_size, randint(min_size + 2, max_size))
        for c in range(chars):
            while True:
                char = alphabet[randint(0, len(alphabet) - 1)]
                if leagal_char(char, word, chars):
                    word += char
                    break
        print(word, '-', WORDS[randint(0, len(WORDS) - 1)].strip('\n'), file=gad_file)

    print_line_break()

#print('Gadoran words generator 1.4', file=gad_file)
print_line_break()
##while True:
##    action = 'words'#input('input action (type "help" for a list of commands): ')
##    if action == 'words' or action == 'generate words':
##        print_line_break()
##        generate_words()
##    if action == 'exit':
##        print_line_break()
##        exit()
##    if action == 'help':
##        print_line_break()
##        print('commands:')
##        print('help -> shows this help message')
##        print('exit -> terminates the program')
##        print('words -> generates gadoran words')
##        print('generate words -> the same as words')
##        print_line_break()
generate_words()

gad_file.close()
