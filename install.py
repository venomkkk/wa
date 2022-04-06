#!/usr/bin/python
import os 

GREEN='\033[1;32m'

os.system('clear')
print(f"{GREEN}\n instalando as dependências...\n ")

os.system('apt update')
os.system('apt upgrade')
os.system('pkg install figlet')
os.system('pkg install ruby')
os.system('gem install lolcat')
os.system('pip install tqdm')
os.system('pip install progressbar')


os.system('clear')
os.system('figlet wa ban | lolcat -a -d 1')
os.system('echo "Instalação concluida agora pode usar python main.py" | lolcat')
