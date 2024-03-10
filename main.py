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
import shutil

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


def copy_to_desktop(source_path, destination_folder):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    destination_path = os.path.join(desktop_path, destination_folder)

    # Create destination folder on the desktop
    os.makedirs(destination_path, exist_ok=True)

    # Copy files to the destination folder
    for file_name in os.listdir(source_path):
        full_file_path = os.path.join(source_path, file_name)
        if os.path.isfile(full_file_path):
            shutil.copy(full_file_path, destination_path)

    return destination_path


def run_on_desktop(file_path):
    subprocess.call(["cmd.exe", "/c", file_path], shell=True)


def windows():
    path = get_resource_path(os.path.join("activation", "windows.cmd"))
    desktop_path = copy_to_desktop(os.path.dirname(path), "Activation_Files")
    run_on_desktop(os.path.join(desktop_path, "windows.cmd"))


def office():
    path = get_resource_path(os.path.join("activation", "ohook.cmd"))
    desktop_path = copy_to_desktop(os.path.dirname(path), "Activation_Files")
    run_on_desktop(os.path.join(desktop_path, "ohook.cmd"))


def trouble():
    path = get_resource_path(os.path.join("activation", "troubleshoot.cmd"))
    desktop_path = copy_to_desktop(os.path.dirname(path), "Activation_Files")
    run_on_desktop(os.path.join(desktop_path, "troubleshoot.cmd"))


def change():
    path = get_resource_path(os.path.join("activation", "change_editions.cmd"))
    desktop_path = copy_to_desktop(os.path.dirname(path), "Activation_Files")
    run_on_desktop(os.path.join(desktop_path, "change_editions.cmd"))


def KMS38():
    path = get_resource_path(os.path.join("activation", "KMS8.cmd"))
    desktop_path = copy_to_desktop(os.path.dirname(path), "Activation_Files")
    run_on_desktop(os.path.join(desktop_path, "KMS38.cmd"))


def KMS():
    path = get_resource_path(os.path.join("activation", "KMS.cmd"))
    desktop_path = copy_to_desktop(os.path.dirname(path), "Activation_Files")
    run_on_desktop(os.path.join(desktop_path, "KMS.cmd"))


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
            ||          [5] {RED}Online KMS activation{CYAN}      |       [6] {RED}KMS38[38 years]{CYAN}                    ||
            ||{"-" * 88}||
            ||          [7] {RED}Donate us{CYAN}                  |       [0] {RED}Exit{CYAN}                               ||
            {CYAN}{"-" * 92}
"""
print(RESET)
while True:
    clear()  # Clear the screen
    print(menu + '\n\n\n\n')

    op = input("Please specify what you want to activate: ")

    while op not in ['1', '2', '3', '4', '5', '6', '7', '0']:
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
        clear()
        KMS()
        input('Press enter to continue...')
    elif op == '6':
        clear()
        KMS38()
        input('Press enter to continue...')
    elif op == '7':
        webbrowser.open('https://fg-repacks.site/p/donate.html')
    elif op == '0':
        clear()
        print(Fore.BLUE + 'Thanks for using my tool\ncleaning up things for u' + Style.RESET_ALL)
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Activation_Files")
        shutil.rmtree(desktop_path)
        print(Fore.LIGHTMAGENTA_EX + 'Plz checkout my other works too' + Style.RESET_ALL)
        break
