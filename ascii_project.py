import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
rows = []
ascii=[]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
small_alphabet = "abcdefghijklmnopqrstuvwxyz?"
for i in range(h):
    row = input()
    rows += [row]
    print(row, file=sys.stderr)
for char in range(len(alphabet)):
    ascii_char = []
    for y in range(h):
        char_line = rows[y][l*char:l+l*char]
        #print(char_line, file=sys.stderr)
        ascii_char += [char_line]
    #print(ascii_char, file=sys.stderr)
    ascii += [ascii_char]
print(ascii, file=sys.stderr)
def char_index(char):
    for index in range(len(alphabet)):
        if char == alphabet[index]:
            return index
        elif char == small_alphabet[index]:
            return index
    return char_index("?")
print(char_index("E"), file=sys.stderr)
for y in range(h):
    t_row = ""
    for symbol in range(len(t)):
        letter = t[symbol]
        letter_index = char_index(letter)
        letter_ascii = ascii[letter_index]
        letter_row = letter_ascii[y]
        t_row += letter_row
    print(t_row)

