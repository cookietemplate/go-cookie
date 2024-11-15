import os
import pathlib
import json
import shutil
import subprocess

import requests

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_ROOT = pathlib.Path(PROJECT_DIRECTORY)

LICENSES_DICT = {
    "Proprietary": None,
    "Apache-2.0": "Apache-2.0",
    "MIT": "MIT",
    "BSD-4-Clause": "BSD-4-Clause",
    "BSD-3-Clause": "BSD-3-Clause",
    "BSD-2-Clause": "BSD-2-Clause",
    "GPL-2.0-only": "GPL-2.0",
    "GPL-2.0-or-later": "GPL-2.0",
    "GPL-3.0-only": "GPL-3.0",
    "GPL-3.0-or-later": "GPL-3.0",
    "LGPL-2.1-only": "LGPL-2.1",
    "LGPL-2.1-or-later": "LGPL-2.1",
    "LGPL-3.0-only": "LGPL-3.0",
    "LGPL-3.0-or-later": "LGPL-3.0",
    "ISC": "ISC",
}


def download_license_from_github(license_name):
    """Download the license file from GitHub"""
    license_name = LICENSES_DICT[license_name]
    if license_name:
        url = 'https://api.github.com/licenses/{}'.format(license_name)
        response = requests.get(url)
        if response.status_code == 200:
            license_content = json.loads(response.content.decode('utf-8'))['body']
            return license_content
    return None


def write_license_file(license_name):
    """Write the license file to the project directory"""
    license_content = download_license_from_github(license_name)
    if license_content:
        with open(os.path.join(PROJECT_DIRECTORY, 'LICENSE'), 'w') as f:
            f.write(license_content)

def remove_folder(folder_path):
    """Remove the folder"""
    folder_path = PROJECT_ROOT / folder_path
    if folder_path.exists():
        shutil.rmtree(folder_path)

def init_go_modules():
    """Initialize go modules"""
    subprocess.run(["go", "mod", "tidy"], cwd=PROJECT_DIRECTORY)

if __name__ == '__main__':
    if "{{ cookiecutter.open_source_license }}" != "Proprietary":
        write_license_file("{{ cookiecutter.open_source_license }}")

    if not {{cookiecutter.use_protoc}}:
        remove_folder("api")
        remove_folder("third_party")
    
    if "{{cookiecutter.ci}}" == "None":
        remove_folder(".github")

    init_go_modules()
