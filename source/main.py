#!/usr/bin/env python3

from os import geteuid
from sys import argv
from re import match

import subprocess

package_managers = ['apk', 'apt', 'apt-get', 'dnf', 'emerge', 'pacman', 'pkg', 'yay', 'yum', 'zypper']

if geteuid () == 0:

    try: filename = argv [1]
    except IndexError: filename = 'requirements.txt'

    for package_manager in package_managers:

        try:
            subprocess.check_output (f'which {package_manager}', shell = True)

            if package_manager == 'apk':
                syntax = 'add --no-cache'

            elif package_manager == 'emerge':
                syntax = '-a'

            elif package_manager == 'yay' or package_manager == 'pacman':
                syntax = '-S --noconfirm'

            else:
                syntax = 'install -y'

            try:
                with open (filename, 'r') as file:

                    for package in file:

                        package = match (r'^[a-zA-Z0-9-]+', package)
                        subprocess.run (f'{package_manager} {syntax} python3-{package.group (0)}', shell = True)

                    file.close ()
                    exit ()

            except FileNotFoundError:
                print ('Error: File not found')
                exit ()

        except subprocess.SubprocessError:
            pass

else:
    print ('Error: Run the tool with administrator privileges')
    exit ()
