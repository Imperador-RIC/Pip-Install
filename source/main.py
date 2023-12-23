#!/usr/bin/env python3

# IMPORTING LIBRARIES AND DEPENDENCIES

import argparse, subprocess
from os import geteuid
from re import match

# PROGRAM ARGUMENT HANDLING

parser = argparse.ArgumentParser (prog = 'PIP-Install', usage = 'pip-i [install | uninstall] [packages | filename]')

parser.add_argument ('action', choices = ['install', 'uninstall', 'freeze'], default = 'install', nargs = 1)
parser.add_argument ('packages', default = 'requirements.txt', nargs = '*')

args = parser.parse_args ()

# INTERNAL FUNCTION OF THE PROGRAM

def check (list_program: list) -> (str | None):
    """Function that checks if a binary is installed on the system and returns its name if it is installed, otherwise, returns None"""

    for program in list_program:
        if program == None: return None
        try: subprocess.check_output (f'which {program}', shell = True) ; return program
        except (subprocess.SubprocessError): pass

# LIST OF SUPPORTED PACKAGE MANAGERS

class Managers:
    PACKAGE = ['apk', 'apt', 'apt-get', 'dnf', 'emerge', 'pacman', 'pkg', 'yay', 'yum', 'zypper', None]
    PIP = ['pip3', 'pip', None]

# PROGRAM EXECUTION

def main ():

    if args.action == ['install'] or args.action == ['uninstall']:

        if geteuid () == 0:

            package_manager = check (Managers.PACKAGE)

            if package_manager == None:
                print ('No compatible package managers were found!')
                exit ()

            else:

                if args.action == ['install']:

                    if package_manager == 'apk': syntax = 'add --no-cache'
                    elif package_manager == 'emerge': syntax = '-a'
                    elif package_manager == 'pacman' or package_manager == 'yay': syntax = '-S --noconfirm'
                    else: syntax = 'install -y'

                else:

                    if package_manager == 'apk': syntax = 'del -y'
                    elif package_manager == 'emerge': syntax = '-C'
                    elif package_manager == 'pacman': syntax = '-R --noconfirm'
                    elif package_manager == 'yay': syntax = '-Rns --noconfirm'
                    elif package_manager == 'zypper': syntax = 'remove --non-interactive'
                    else: syntax = 'remove -y'

                if len (args.packages) == 1:

                    try:
                        with open (str (args.packages), 'r') as file:

                            for package in file:

                                package = match (r'^[a-zA-Z0-9-]+', package)
                                subprocess.run (f'{package_manager} {syntax} python3-{package.group (0)}', shell = True)

                            file.close ()
                            exit ()

                    except FileNotFoundError:
                        pass

                for package in args.packages:
                    subprocess.run(f'{package_manager} {syntax} {package}', shell = True)

        else:
            print ('Run the program with administrator privileges to use this function!')
            exit ()

    elif args.action == ['freeze']:

        package_manager = check (Managers.PIP)

        if package_manager == None:
            print ('The pip and pip3 package managers were not found!\nThey are a requirement to run the "freeze" command!')
            exit ()

        else:
            subprocess.run (f'{package_manager} freeze', shell = True)
            exit ()

if __name__ == '__main__':
    main ()
