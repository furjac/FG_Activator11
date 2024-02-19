"""
MIT License

Copyright (c) 2024 Furjack

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
import webbrowser
import subprocess
import sys


badge_url = "https://img.shields.io/github/v/release/furjac/FG_Activator11"

def clear():
    os.system('cls')

def get_resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # In development, use the script's directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def windows():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    path = get_resource_path(os.path.join("activation", "windows.cmd"))

    subprocess.call(["cmd.exe", "/c", path], shell=True)

def office():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    path = get_resource_path(os.path.join("activation", "ohook.cmd"))

    subprocess.call(["cmd.exe", "/c", path], shell=True)

def trouble():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    path = get_resource_path(os.path.join("activation", "troubleshoot.cmd"))

    subprocess.call(["cmd.exe", "/c", path], shell=True)

def change():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    path = get_resource_path(os.path.join("activation", "change_editions.cmd"))

    subprocess.call(["cmd.exe", "/c", path], shell=True)

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
            ||          [3] {YELLOW}Troubleshoot{CYAN}               |       [4] {RED}Change Editions{CYAN}                    ||
            ||{"-" * 88}||
            ||          [5] {RED}Donate us{CYAN}                  |       [0] {RED}Exit{CYAN}                               ||
            {CYAN}{"-" * 92}
"""
print(RESET)
while True:
    clear()  # Clear the screen
    print(menu+'\n\n\n\n')

    op = input("Please specify what you want to activate: ")

    while op not in ['1', '2', '3','4','5', '0']:
        print("Invalid option. 😒 choose a correct one")
        op = input("Please specify what you want to activate: ")

    if op == '1':
        clear()
        windows()
        input("Press Enter to continue...")
    elif op == '2':
        clear()
        office()
        input('Press enter to continue....')
    elif op == '3':
        clear()
        trouble()
        input('Press enter to continue...')
    elif op == '4':
        clear()
        change()
        input('Press enter to continue...')
    elif op == '5':
        webbrowser.open('https://fg-repacks.site/p/donate.html')
    elif op == '0':
        clear()
        print(Fore.BLUE + 'Thanks for using my tool' + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + 'Plz checkout my other works too' + Style.RESET_ALL)
        break
