#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time
from colorama import just_fix_windows_console
# necessary for color to work in the console
just_fix_windows_console()   

print('Welcome to \'Rock, Paper, Scissors\'!')
time.sleep(2)
name = input('Enter your name:')
print(f'\nHello {name}!')
time.sleep(1)

my_score = 0
comp_score = 0

while True:
  choice = input('\nPick Rock, Paper or Scissors: ')
  choices = ['Rock', 'Paper', 'Scissors']
  while choice.title() not in choices:
    choice = input('Pick Rock, Paper or Scissors: ')
  time.sleep(0.5)
  comp_choice = random.choice(choices)
  for item in ['\nThe Computer picks', '.', '.', '. ', comp_choice + '\n']:
    print(item, end='', flush=True)
    time.sleep(0.4)
  if choice.title() == comp_choice:
    # ANSI sequences are added before and after the result to add and remove color ('\033[33m' = yellow)
    print('\033[33m' + 'It\'s a draw.' + '\033[0m')
  elif choice.title() == 'Rock' and comp_choice == 'Paper':
    print('\033[31m' + 'Sorry you lost!' + '\033[0m')
    comp_score += 1
  elif choice.title() == 'Paper' and comp_choice == 'Rock':
    print('\033[32m' + 'Congratulations you won!' + '\033[0m')
    my_score += 1
  elif choice.title() == 'Paper' and comp_choice == 'Scissors':
    print('\033[31m' + 'Sorry you lost!' + '\033[0m')
    comp_score += 1
  elif choice.title() == 'Scissors' and comp_choice == 'Paper':
    print('\033[32m' + 'Congratulations you won!' + '\033[0m')
    my_score += 1
  elif choice.title() == 'Rock' and comp_choice == 'Scissors':
    print('\033[32m' + 'Congratulations you won!' + '\033[0m')
    my_score += 1
  elif choice.title() == 'Scissors' and comp_choice == 'Rock':
    print('\033[31m' + 'Sorry you lost!' + '\033[0m')
    comp_score += 1
  print(f'\n{name}: {my_score}')
  print(f'Computer: {comp_score}')

