#! /usr/bin/env python3

# Program to create "character rain"
# In more words: given an input string, assigns a random value X to each character C in the string
# then prints a string where each C is exactly X lines from the top of the output.
# This creates output like so:
# Input: Hello World!
# Output:H        l
#            o
#         e     o
#              W
#          l
#                   !
#           l
#                r d

import random

def assign_random_values(input_string, string_length):
    charlist = []
    for c in input_string:
        vertical_offset = random.randrange(string_length)
        charlist.append([c, vertical_offset])
    return charlist
        
def create_output_string(charlist, string_length):
    output = ''
    for i in range(string_length):
        for x in charlist:
            char = x[0]
            offset = x[1]
            if offset == i:
                output += char
            else:
                output += ' '
        output += '\n'
    return output
        
def character_rain(input_string):
    string_length = len(input_string)
    charlist = assign_random_values(input_string, string_length)
    output = create_output_string(charlist, string_length)
    return output

def main():
    print('Input string:')
    input_string = input()
    
    output = character_rain(input_string)
    
    print(output)

if __name__ == "__main__":
    main()
