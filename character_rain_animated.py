#! /usr/bin/env python3

# Program to create "character rain"

import random
import tkinter as tk

charlist = []

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

def animation(label, string_length):
	def animate():
		global charlist
		for x in charlist:
			x[1] += 1
			x[1] %= string_length
		output = create_output_string(charlist, string_length)
		label.config(text=output)
		label.after(10, animate)
	animate()

def main():
	input_string = input('Input string: ')
	string_length = len(input_string)
	
	root = tk.Tk()
	root.title('Character Rain')
	label = tk.Label(root, text='')
	
	global charlist
	charlist = assign_random_values(input_string, string_length)
	output = create_output_string(charlist, string_length)
	
	label.config(text=output)
	label.pack()
	animation(label, string_length)
	root.mainloop()
	
if __name__ == '__main__':
	main()
