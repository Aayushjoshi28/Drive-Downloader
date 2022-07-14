import colorama
import gdown
import re
from colorama import Fore, Back
colorama.init(autoreset=True)
print(Fore.LIGHTGREEN_EX + '██████      ██████    ██████   ██    ██     ██  ███    ██')
print(Fore.LIGHTYELLOW_EX + '██   █      ██   █   ██    ██  ██    ██     ██  ██ █   ██')
print(Fore.LIGHTRED_EX + '██   ██ ███ ██   ██  ██    ██  ██    ██     ██  ██  █  ██')
print(Fore.LIGHTBLUE_EX + '██   ██     ██   ██  ██    ██   ██  ██ ██  ██   ██   █ ██')
print(Fore.LIGHTCYAN_EX + '██████      ██████    ██████     ████   ████    ██    ███')
print('\n')
print('**********************************************************')
print('*               Copyright of Mr.EncodedGuy               *')
print('**********************************************************')
print(Fore.GREEN + Back.LIGHTWHITE_EX + 'URl Format - [+] https://drive.google.com/file/d/1sAO0p0prqVVjjgEMei564Hg/view?usp=sharing [+]')
print('\n')
file_type = input(Fore.LIGHTRED_EX + Back.LIGHTWHITE_EX + 'What do you want to download - File Or Folder')
if file_type == 'File':
    input_url = input(Fore.RED + 'Enter File Url: ')
    split_url = re.split('/', input_url)
    part1 = 'https://drive.google.com/u/1/uc?id='
    part2 = split_url[5]
    part3 = '&export=download'
    url = part1+part2+part3
    output = input(Fore.RED + 'Output File Name: ')
    gdown.download(url, output)
elif file_type == 'Folder':
    input_url = input(Fore.RED + 'Enter Folder Url: ')
    split_url = re.split('/', input_url)
    part1 = 'https://drive.google.com/u/1/uc?id='
    part2 = split_url[4]
    part3 = '&export=download'
    url = part1 + part2 + part3
    output = input(Fore.RED + 'Output Folder Name: ')
    gdown.download_folder(url, output)
else:
    print('File Type is case sensitive')