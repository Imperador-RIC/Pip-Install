# Pip-Install

Script for installing Python dependencies through native package managers.

Some operating systems limit the use of pip to installing Python dependencies, and make them available through the system's package manager.

This script is used to install all the dependencies from a requirements file, through the system's own package manager, thus saving the work of installing the dependencies through a single command that will do all this work for the user.

This process of installing dependencies without our script could be very time-consuming, as it would be necessary to write a command, or multiple commands, to install all the dependencies of a given program.

## Program operation

The program's operation is simple, it first checks whether the user is running as an administrator or not.

After that, it checks which package manager the system has.

And finally, it generates a command to install each dependency listed in the requirements file and executes it until all dependencies are installed.

## Compatibility

There is no confirmation of which operating systems usually or do not limit the functioning of pip, and there are several existing operating systems, so the program was created to try to be compatible with the widest range of operating systems possible, without knowing for sure which ones. systems limit the functioning of pip or not, or which package managers are typically used by these distributions or not.

The program is theoretically compatible with the 10 most famous package managers used in current Linux distributions, but has not been properly tested in all environments.

## Manual

To install the tool, run the install.sh installation script using the `./install.sh` command.

Then you can run the `pip-install` command to use the script, or, you can run the tool passing some argument that is the name of a dependency file, if the standard naming convention used by the community is not used, called requirements.
