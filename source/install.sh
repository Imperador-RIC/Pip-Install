#!/usr/bin/env bash

chmod +x main.py
sudo cp main.py /usr/bin/pip-install
sudo chown $USER:$USER /usr/bin/pip-install
echo -e '\e[32mThe program has been installed successfully! \nRun the 'pip-install' command to use the tool\e[0m'
