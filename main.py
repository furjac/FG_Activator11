"""
MIT License

Copyright (c) 2023 Furjack

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from colorama import Fore, Style
from activation.office import activate_office
from activation.windows import activate_windows
import os
import webbrowser
import re
import requests
import wget

badge_url = "https://img.shields.io/github/v/release/furjac/FG_Activator11"

def main():
    activate_windows()

def office():
    activate_office()

def clear():
    os.system('cls')


# Define colors
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RED = Fore.RED
RESET = Style.RESET_ALL

# ASCII art border for the menu
menu = f"""
            {CYAN}{"-" * 92}
            ||                                      {GREEN}FG_Activator{CYAN}                                      ||
            ||{"-" * 88}||
            ||          [1] {GREEN}Windows   {CYAN}                 |       [2] {GREEN}Microsoft Office{CYAN}                   ||
            ||{"-" * 88}||
            ||          [3] {YELLOW}Donate us{CYAN}                  |       [0] {RED}Exit{CYAN}                               ||
            {CYAN}{"-" * 92}
"""
print(RESET)
while True:
    clear()  # Clear the screen
    print(menu+'\n\n\n\n')

    op = input("Please specify what you want to activate: ")

    while op not in ['1', '2', '3', '0']:
        print("Invalid option. 😒 choose a correct one")
        op = input("Please specify what you want to activate: ")

    if op == '1':
        clear()
        main()
        input("Press Enter to continue...")
    elif op == '2':
        clear()
        office()
        input('Press enter to continue....')
    elif op == '3':
        webbrowser.open('https://fg-repacks.site/p/donate.html')
    elif op == '0':
        clear()
        print(Fore.BLUE + 'Thanks for using my tool' + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + 'Plz checkout my other works too' + Style.RESET_ALL)
        break
