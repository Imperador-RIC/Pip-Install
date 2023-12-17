# Pip-Install

Script for installing Python dependencies through native package managers.

Some operating systems limit the use of pip to installing Python dependencies, and make them available through the system's package manager.

This script is used to install all the dependencies from a requirements file, through the system's own package manager, thus saving the work of installing the dependencies through a single command that will do all this work for the user.

This process of installing dependencies without our script could be very time-consuming, as it would be necessary to write a command, or multiple commands, to install all the dependencies of a given program.

To find out if pip is limited in your operating system, just try to install some dependency using it, if a message similar to `error: externally-managed-environment`, it means that your system is focused on stability and your pip is limited to ensure the proper functioning of your system.

## Program operation

The program basically imitates pip syntax, but adapts it to use the native package manager of the operating system it is running.

The program has the installation, uninstallation, and freeze function, despite being technically useless, as this function works perfectly even in limited environments.

## Compatibility

There is no confirmation of which operating systems usually or do not limit the functioning of pip, and there are several existing operating systems, so the program was created to try to be compatible with the widest range of operating systems possible, without knowing for sure which ones. systems limit the functioning of pip or not, or which package managers are typically used by these distributions or not.

The program is theoretically compatible with the 10 most famous package managers used in current Linux distributions, but has not been properly tested in all environments.

## Manual

To install the tool, run the install.sh installation script using the `./install.sh` command.

Then you can run the `pip-i` command followed by the install or uninstall parameter to install or uninstall a package or list of packages, if you enter the name of a dependency file such as "requirements.txt", the program will read and install or uninstall the packages listed in the file.

## Limitation

The program cannot select specific versions of dependencies, it will always install the most recent version of dependencies available.

Remember, if your operating system limits the functioning of pip it is because there is a reason behind it, use this tool wisely and only if necessary, after all, this tool is nothing more than a temporary and inadequate solution to a common problem, Use at your own risk and wisely.
