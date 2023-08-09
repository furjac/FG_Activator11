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
import subprocess


def activate_office():
    office16_path = [
        "C:\\Program Files\\Microsoft Office\\Office16",
        "C:\\Program Files (x86)\\Microsoft Office\\Office16"
    ]

    ospp_vbs_found = False
    for path in office16_path:
        ospp_vbs_path = os.path.join(path, "ospp.vbs")
        if os.path.exists(ospp_vbs_path):
            os.chdir(path)
            ospp_vbs_found = True
            break

    if not ospp_vbs_found:
        print("ospp.vbs not found in Office16 installation directory.")
        return
    licenses_path = os.path.join("..", "root", "Licenses16")
    xrm_files = [f for f in os.listdir(licenses_path) if f.startswith("ProPlus2021VL_KMS") and f.endswith(".xrm-ms")]
    for xrm_file in xrm_files:
        xrm_path = os.path.join(licenses_path, xrm_file)
        subprocess.run(["cscript", "ospp.vbs", "/inslic:" + xrm_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["cscript", "ospp.vbs", "/inpkey:FXYTK-NJJ8C-GB6DW-3DYQT-6F7TH"], stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    subprocess.run(["cscript", "ospp.vbs", "/sethst:kms.msgang.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["cscript", "ospp.vbs", "/act"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def office_365():
    # Change the working directory to the Office16 folder
    office16_path = os.path.join(os.environ.get("ProgramFiles", ""), "Microsoft Office", "Office16")
    if not os.path.exists(office16_path):
        office16_path = os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Microsoft Office", "Office16")
    os.chdir(office16_path)

    # Install licenses
    licenses_path = os.path.join("..", "root", "Licenses16")
    for license_file in os.listdir(licenses_path):
        if license_file.startswith("proplusvl_kms") and license_file.endswith(".xrm-ms"):
            subprocess.run(["cscript", "ospp.vbs", "/inslic:" + os.path.join(licenses_path, license_file)],
                           stdout=subprocess.PIPE)
        elif license_file.startswith("proplusvl_mak") and license_file.endswith(".xrm-ms"):
            subprocess.run(["cscript", "ospp.vbs", "/inslic:" + os.path.join(licenses_path, license_file)],
                           stdout=subprocess.PIPE)

    # Activate Office using KMS servers
    kms_servers = ["kms7.MSGuides.com", "kms8.MSGuides.com", "kms9.MSGuides.com"]
    for i, kms_server in enumerate(kms_servers, 1):
        subprocess.run(["cscript", "ospp.vbs", "/sethst:" + kms_server], stdout=subprocess.PIPE)
        result = subprocess.run(["cscript", "ospp.vbs", "/act"], stdout=subprocess.PIPE, text=True)
        if "successful" in result.stdout:
            print("Office activation successful.")
            break
        elif i == len(kms_servers):
            print("Failed to activate Office.")
            return False
        else:
            print("Trying to connect to another KMS server... Please wait.")
    return True


def office():
    print('Plz chose the office version correctly\n\n')
    print('1. Microsoft office 365')
    print('2. Microsoft office 2021 (ltsc)')

    of = input('Enter: ')

    while of not in ['1', '2']:
        print("Invalid option. 😒 dont test my patience")
        of = input('Enter: ')

    if of == '1':
        office_365()
    elif of == '2':
        activate_office()
