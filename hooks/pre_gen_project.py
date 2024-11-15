import re
import sys

MODULE_REGEX = r'^[a-z][a-z0-9_-]+$'

project_name = '{{ cookiecutter.project_name }}'
project_slug = '{{ cookiecutter.project_slug }}'
module_name = '{{ cookiecutter.__module_name }}'

go_version = '{{ cookiecutter.go_version }}'

if not project_name:
    print('ERROR: The project name cannot be empty')
    sys.exit(1)

if not project_slug:
    print('ERROR: The project slug cannot be empty')
    sys.exit(1)

if "/" not in project_slug:
    print('WARNING: The project slug should be in the format "owner/repo"')
    if check := input('Do you want to continue? [y/N] ').lower():
        if check != 'y':
            sys.exit(1)

if not module_name:
    print('ERROR: The module name cannot be empty')
    sys.exit(1)

if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: The module name({module_name}) is not a valid Go module name')
    sys.exit(1)
