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
import shutil
import tkinter as tk
from tkinter import messagebox


def clear():
    os.system('cls')


# Define colors
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RED = Fore.RED
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

# ASCII art border for the menu
menu = f"""
            {CYAN}{"-" * 92}
            ||                                      {GREEN}FG_Activator{CYAN}                                      ||
            ||{"-" * 88}||
            ||          [1] {GREEN}Windows   {CYAN}                 |       [2] {GREEN}Microsoft Office{CYAN}                   ||
            ||{"-" * 88}||
            ||          [3] {YELLOW}Troubleshoot{CYAN}               |       [4] {YELLOW}Change Editions{CYAN}                    ||
            ||{"-" * 88}||
            ||          [5] {Fore.LIGHTBLUE_EX}Online KMS activation{CYAN}      |       [6] {Fore.LIGHTBLUE_EX}KMS38[38 years]{CYAN}                    ||
            ||{"-" * 88}||
            ||          [7] {MAGENTA}Extract OEM Folder{CYAN}         |       [8] {MAGENTA}Check activation status{CYAN}            ||
            ||{"-" * 88}||
            ||          [9] {RED}Donate us{CYAN}                  |       [0] {RED}exit{CYAN}                               ||
            {CYAN}{"-" * 92}
"""
print(RESET)
def message():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

        # Display the message box
    messagebox.showinfo("Project Under Development", 
                            "Sorry, the software is under development. The developer can't keep up with the project.\nDonate to keep the project up and running.")

        # Close the tkinter window after the user closes the message box
    root.quit()

while True:
    clear()  # Clear the screen
    print(menu + '\n\n\n\n')

    op = input("Please specify what you want to activate: ")

    while op not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        print("Invalid option. 😒 choose a correct one")
        op = input("Please specify what you want to activate: ")

    if op == '1':
        clear()
        print('Sorry the software is under development the developer cant keep up the project\n donate to keep the project up and running')
        message()
        input("Press Enter to continue...")
    elif op == '2':
        clear()
        print('Sorry the software is under development the developer cant keep up the project\n donate to keep the project up and running')
        message()
        input('Press enter to continue....')
    elif op == '3':
        clear()
        print('Sorry the software is under development the developer cant keep up the project\n donate to keep the project up and running')
        message()
        input('Press enter to continue...')
    elif op == '4':
        clear()
        print('Sorry the software is under development the developer cant keep up the project\n donate to keep the project up and running')
        message()
        input('Press enter to continue...')
    elif op == '5':
        clear()
        print('Sorry the software is under development the developer cant keep up the project\n donate to keep the project up and running')
        message()
        input('Press enter to continue...')
    elif op == '6':
        clear()
        print('Sorry the software is under development the developer cant keep up the project\n donate to keep the project up and running')
        message()
        input('Press enter to continue...')
    elif op == '7':
        clear()
        print('Sorry the software is under development the developer cant keep up the project\n donate to keep the project up and running')
        message()
        input('Press enter to continue...')
    elif op == '8':
        clear()
        print('Sorry the software is under development the developer cant keep up the project\n donate to keep the project up and running')
        message()
        input('Press enter to continue...')
    elif op == '9':
        clear()
        print('you can donate in upi/crypto:')
        print('UPI: furjack@ybl')
        print('XMR: ')
        print('BTC: 14GSZ1293s65JjytCjMz3AFNSUa4ZVN2V')
        input('Press enter to continue...')
    elif op == '0':
        clear()
        print(Fore.BLUE + 'Thanks for using my tool\ncleaning up things for u' + Style.RESET_ALL)
        desktop_path = os.path.join(os.path.expanduser(
            "~"), "Desktop", "Activation_Files")
        try:
            shutil.rmtree(desktop_path)
        except:
            pass
        print(Fore.LIGHTMAGENTA_EX +
              'Plz checkout my other works too' + Style.RESET_ALL)
        break
