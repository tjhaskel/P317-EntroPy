from __future__ import division	# Allows for a float to be created by dividing integers
import math	# Used for the log function
import string	# Used for its lisst of punctuation

token = ''	# An empty string now, but will be filled and emptied for every token
tokens = []	# A list of every token from the input
languages = ['brainfuck', 'c++', 'haskell', 'java', 'python', 'scheme'] # Pardon my French

def log2(x):	# This function finds the base 2 log of some float x
  return math.log(x) / math.log(2)

def main(file):       # This is the central program in the script. It opens a file and
  f = open(file, 'r') #  iterates through it one character at a time, passing each 
  byte = f.read(1)    #  character to the tokenize function. When all characters have
  while byte != '':   #  been sorted, it calculates the entropy and prints the
    tokenize(byte)    #  results in a text file to be analyzed and stored.
    byte = f.read(1)
  
  result = entropy(tokens)
  print(tokens)	# It also prints out the full list of tokens and result for each language
  print(result)	# in the console it is run from. Mostly because it's cool to look at.
  f.close()
  r.write(file + ': ' + str(result) + '\n')

def entropy(list):	# This program takes a list of elements and find the entropy
  entropySum = 0.0	# using Shannon's equation for entropy of a signal.
  seen = []
  for x in list:
    if x not in seen:
      probability = list.count(x) / len(list)
      entropySum += probability * log2(probability)
      seen.append(x)
  return -entropySum

def tokenize(byte):		  # This function takes a character and decides whether to group
  global token			  #  it with other characters as a single token or interpret it as 
  if byte == ' ' or byte == '\n': #  its very own token. Spaces are ignored, but this may change
    if token != '':		  #  in the future as some languages do have significant whitespace
      tokens.append(token)
    token = ''
  elif byte in string.punctuation:
    if token != '':
      tokens.append(token)
    tokens.append(byte)
    token = ''
  else:
    token += byte

task = input('Filename: ')	# This asks the user which task should be analyzed

r = open('results.txt', 'w')	# Opens the file in which results will be stored. 
for lang in languages:	# Runs the code for each language defined earlier
  main(lang + '/' + task)
  tokens = []
r.close()	# Close your files so you dont eat up memory!
