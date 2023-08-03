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
import os
from activation.windows11 import Activate_windows11
from activation.windows10 import ActivateWindows10
from activation.msoffice import office
import webbrowser

os.system('cls')

# Define colors
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RED = Fore.RED
RESET = Style.RESET_ALL

# ASCII art border for the menu
menu = f"""
{CYAN}{"-" * 91}
||                                      {GREEN}FG_Activator{CYAN}                                      ||
||{"-" * 88}||
||          [1] {GREEN}Windows 11{CYAN}                 |       [2] {GREEN}Microsoft Office{CYAN}                   ||
||{"-" * 88}||
||          [3] {YELLOW}Windows 10{CYAN}                 |       [4] {YELLOW}Donate us{CYAN}                          ||
||{"-" * 88}||
||          [0] {RED}Exit{CYAN}                       |                                              ||
{CYAN}{"-" * 90}
"""
print(RESET)
while True:
    os.system('cls')  # Clear the screen
    print(menu)

    op = input("Please specify what you want to activate: ")

    while op not in ['1', '2', '3', '4', '0']:
        print("Invalid option. 😒 choose a correct one")
        op = input("Please specify what you want to activate: ")

    if op == '1':
        Activate_windows11()
        print('😘congrats u just activated windows 11')
        input("Press Enter to continue...")
    elif op == '2':
        office()
        print('😘congrats u just activated office')
        input("Press Enter to continue...")
    elif op == '3':
        ActivateWindows10()
        print('😘congrats u just activated windows 10')
        input("Press Enter to continue...")
    elif op == '4':
        webbrowser.open('https://fg-repacks.site/p/donate.html')
    elif op == '0':
        os.system('cls')
        print(Fore.BLUE+'Thanks for using my tool'+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX+'Plz checkout my other works too'+Style.RESET_ALL)
        break
