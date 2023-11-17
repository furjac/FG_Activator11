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
import os
import time
from colorama import Fore, Style

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RED = Fore.RED
RESET = Style.RESET_ALL


def activate_windows(selected_option):
    keys = {
        '1': 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
        '2': '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH',
        '3': 'W269N-WFGWX-YVC9B-4J6C9-T83GX',
        '4': 'NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J',
        '5': 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
        '6': '6TP4R-GNPTD-KYYHQ-7B7DP-J447Y',
        '7': 'NPPR9-FWDCX-D2C8J-H872K-2YT43',
    }

    if selected_option in keys:
        print('[+] Please wait while we are checking')
        print('[+] Message boxes will pop up; just press yes/ok')
        os.system(f'slmgr /ipk {keys[selected_option]}')
        time.sleep(2)
        os.system('slmgr /skms kms.loli.best')
        time.sleep(2)
        os.system('slmgr /ato')
    else:
        print("Invalid option. Please choose a correct one")


def windows_edition_selection():
    print('\n\n\n\n')
    selected_option = input('Select your Windows edition wisely > ')

    while selected_option not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid option. 😒 Choose a correct one")
        selected_option = input("Please specify what you want to activate: ")

    activate_windows(selected_option)


def main():
    print(f"            {CYAN}{'-' * 92}")
    print(f"            ||                                      {GREEN}FG_Activator{CYAN}                                      ||")
    print(f"            ||{'-' * 88}||")
    print(f"            ||   [1] {GREEN}Windows Core         {CYAN}              |       [2] {GREEN}Core Single language              ||")
    print(f"            ||{'-' * 88}||")
    print(f"            ||   [3] {YELLOW}Professional         {CYAN}              |       [4] {RED}Professional Workstation          ||")
    print(f"            ||{'-' * 88}||")
    print(f"            ||   [5] {YELLOW}Education            {CYAN}              |       [6] {RED}Professional Education            ||")
    print(f"            ||{'-' * 88}||")
    print(f"            ||   [7] {YELLOW}Enterprise           {CYAN}              |       [0] {RED}Not implemented yet               ||")
    print(f"            {CYAN}{'-' * 92}")

    windows_edition_selection()
    print(RESET)


if __name__ == "__main__":
    main()
