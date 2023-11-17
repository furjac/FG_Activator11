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


def office():
    activate_office()
