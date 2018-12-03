# Project Euler Solutions
This project contains an encrypted version of my solution to the Project Euler problem along with a package containing a command line tool to decrypt the solutions.

## Important information
* Each solution file contains instruction to create the password for that file.
* A decrypted solution file may contain more than one solution to the given problem.
* Some of the solutions may solve the problem in general.
* If you are recruiter that I have already spoken to and want to see a particular solution feel free to email me and ask.

## Usage
This section will describe how to install and use the pe_crypto command line tool to decrypt a solution.
### Install
Installing the pe_crypto package with pip is the easiest way to set up the pe_crypto tool. This require python 3 and I recommend doing the install in a virtual environment.
1. Open a terminal and navigate to the Project_Euler directory
2. Run `pip install .\pe_crypto`
Doing this will install the pe_cyrpto tool and any necessary libraries into your python environment.
### Using pe_crypto
To use pe_crypto to decrypt a file you need to get the password for that solution, each solution contains instructions for obtaining the password. Once you have obtained the password use the 'decrypt' command in pe_crypto to decrypt the solution.
The arguments to pe_crypto decrypt are as follows
* Number: The Project Euler problem number 0 padded to 4 decimals.
  * Ex. The number argument for Project Euler Problem \#1 is '0001'
* Password: The password as describe by that solution
* SRC: The solution being decrypted
* DST: The file you want the decrypted file to be.
#### Example
If you where trying to decrypt the solution file for Problem 1 and the password for that solution was 'Password' the command for decrypting that file, if you are in the Project_Euler directory, would be.
```
    pe_crypto decrypt 0001 Password .\\0001-0100\\PE0001.txt PE0001.py
```
## Using a decrypted solution
Every solution is set up to be used as a command line tool. To get information on how to use that command line tools run.
```
    python [solution file] -h
```
Example for Project Euler Problem \#1
```
    python PE0001.py -h
```
