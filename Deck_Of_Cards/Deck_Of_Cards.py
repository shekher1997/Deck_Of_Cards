import sys
import os
import random
import itertools

ans = input("Want to suffel a deck (Y/N): ")

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

random.shuffle(deck)

if ans == 'Y' or ans == 'y':
    print("\nYou got: ",deck[1][0], "of" , deck[1][1] , "\n")
else:
    print("\nBad input, closing program.\n")
    exit()
      

