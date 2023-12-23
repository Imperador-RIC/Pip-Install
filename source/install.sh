#!/usr/bin/env bash

chmod +x main.py
sudo cp main.py /usr/bin/pip-i
sudo chown $USER:$USER /usr/bin/pip-i
echo -e '\e[32mThe program has been installed successfully! \nRun the "pip-i" command to use the tool\e[0m'
