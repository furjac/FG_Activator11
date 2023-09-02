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

def run_command(command):
    try:
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")


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
    print("Activating Office 365 ProPlus for FREE - FG_Teams")

    # Change directory to the Office installation folder
    office_path = os.environ.get("ProgramFiles", "") + "\\Microsoft Office\\Office16"
    if not os.path.exists(office_path):
        office_path = os.environ.get("ProgramFiles(x86)", "") + "\\Microsoft Office\\Office16"

    if os.path.exists(office_path):
        os.chdir(office_path)
    else:
        print("Office not found in the expected directory.")
        return

    # Install license files
    license_dir = "..\\root\\Licenses16"
    for license_file in os.listdir(license_dir):
        if license_file.startswith("proplusvl_kms") or license_file.startswith("proplusvl_mak"):
            run_command(f"cscript ospp.vbs /inslic:\"{os.path.join(license_dir, license_file)}\"")

    print("Activating your Office...")
    run_command("cscript //nologo slmgr.vbs /ckms >nul")
    run_command("cscript //nologo ospp.vbs /setprt:1688 >nul")
    run_command("cscript //nologo ospp.vbs /unpkey:WFG99 >nul")
    run_command("cscript //nologo ospp.vbs /unpkey:DRTFM >nul")
    run_command("cscript //nologo ospp.vbs /unpkey:BTDRB >nul")

    # Set the product key
    product_key = "XQNVK-8JYDB-WJ9W3-YJ8YR-WFG99"
    run_command(f"cscript //nologo ospp.vbs /inpkey:{product_key} >nul")

    # KMS servers
    kms_servers = ["kms7.MSGuides.com", "e8.us.to", "e9.us.to"]

    for i, kms_server in enumerate(kms_servers, start=1):
        if i > 10:
            print("Server is busy and can't respond to your request. Please try again.")
            break

        print(f"Trying KMS server {i}...")
        run_command(f"cscript //nologo ospp.vbs /sethst:{kms_server} >nul")

        # Activate
        activation_result = subprocess.run(
            "cscript //nologo ospp.vbs /act", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        if "successful" in activation_result.stdout.decode().lower():
            print("Activation successful!")
            break
        else:
            print("Activation failed. Trying another server...")

    print("Sorry, your version is not supported.")


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
