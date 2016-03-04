import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
rows = []
ascii_representation = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
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
    ascii_representation += [ascii_char]
print(ascii_representation, file=sys.stderr)
def char_index(char):
    try:
        return alphabet.index(char.upper())
    except e:
        return char_index("?")
print(char_index("E"), file=sys.stderr)
for y in range(h):
    t_row = ""
    for symbol in range(len(t)):
        letter = t[symbol]
        letter_index = char_index(letter)
        letter_ascii = ascii_representation[letter_index]
        letter_row = letter_ascii[y]
        t_row += letter_row
    print(t_row)

