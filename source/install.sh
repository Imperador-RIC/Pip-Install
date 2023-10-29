#!/usr/bin/env bash

chmod +x main.py
sudo mv main.py /usr/bin/pip-install
echo -e '\e[32mThe program has been installed successfully! \nRun the 'pip-install' command to use the tool\e[0m'
rm -f $0
