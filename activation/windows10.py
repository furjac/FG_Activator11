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
import subprocess


def activate_windows10():
    keys = [
        "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
        "3KHY7-WNT83-DGQKR-F7HPR-844BM",
        "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
        "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR",
        "W269N-WFGWX-YVC9B-4J6C9-T83GX",
        "MH37W-N47XK-V7XM9-C7227-GCQG9",
        "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
        "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
        "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
        "NPPR9-FWDCX-D2C8J-H872K-2YT43",
        "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4",
        "WNMTR-4C88C-JK8YV-HQ7T2-76DF9",
        "2F77B-TNFGY-69QQF-B8YKP-D69TJ",
        "W269N-WFGWX-YVC9B-4J6C9-T83GX"
    ]

    print("FG_Activator")
    for key in keys:
        subprocess.run(["cscript", "//nologo", "c:\\windows\\system32\\slmgr.vbs", "/ipk", key], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    print("************************************")
    print("Supported products:")
    print("- Windows 10 Home")
    print("- Windows 10 Professional")
    print("- Windows 10 Enterprise, Enterprise LTSB")
    print("- Windows 10 Education")
    print("************************************")


def activate_with_kms_server(server):
    subprocess.run(["cscript", "//nologo", "c:\\windows\\system32\\slmgr.vbs", "/skms", server], stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    activation_result = subprocess.run(["cscript", "//nologo", "c:\\windows\\system32\\slmgr.vbs", "/ato"],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if b"successfully" in activation_result.stdout:
        print("Activation successful!")
        choice = input("Do you want to restart your PC now [Y,N]? ").strip().lower()
        if choice == 'y':
            subprocess.run(["shutdown", "/r", "/t", "00"])
    else:
        print("The connection to the server failed! Trying to connect to another one...")


def ActivateWindows10():
    print("FG_Activator. ALL version activator")
    while True:
        activate_windows10()
        print("************************************")
        print("Server selection:")
        print("1. kms.chinancce.com")
        print("2. NextLevel.uk.to")
        print("3. GuangPeng.uk.to")
        print("4. AlwaysSmile.uk.to")
        print("5. kms.chinancce.com")
        print("6. kms.shuax.com")
        print("7. Exit")
        choice = input("Please specify the KMS server (1-7): ").strip()
        if choice == '7':
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            servers = [
                "kms.chinancce.com",
                "NextLevel.uk.to",
                "GuangPeng.uk.to",
                "AlwaysSmile.uk.to",
                "kms.chinancce.com",
                "kms.shuax.com"
            ]
            activate_with_kms_server(servers[int(choice) - 1])
        else:
            print("Invalid option. Please choose a valid option.")
