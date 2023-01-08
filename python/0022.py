#! /usr/bin/env python3

def alphabetical_value(word: str) -> int:
    """ Give the sum of the places of the characters in the alphabet, e.g. COLIN is worth 3 + 15 + 12 + 9 + 14 = 53. """
    return sum([ord(char) - ord('a') + 1 for char in word.lower()])


with open("0022_names.txt", "r") as file:
    names = file.readlines()[0].replace("\"", '').split(',')

names.sort()

print(sum([alphabetical_value(name) * (i+1) for i, name in enumerate(names)]))
