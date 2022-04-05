#!/usr/bin/python

#Importação
from tqdm import tqdm
from tqdm import trange
from getpass import getpass
import confi
import os
from sys import argv, executable
from threading import Thread
import time
from webbrowser import open
from email.message import Message
from smtplib import SMTP
##############################

#Cores
BRANCO='\033[1;29m'
VermelhoAll='\e[01;37;41m'
NADA='\033[0m'
CINZA='\033[02;37m'
DESTACAR='\033[01;37m'
RED='\033[1;31m'
AZUL='\033[36m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
AMARELO='\033[33m'
SCOLOR='\033[0m'
SEMCOR='\033[8m'
BrancoAll='\033[03;37;47m'
LETRAPRETA='\033[02;30;47m'
PURPULA='\033[35m'
###############################

#Atualizar...
print(f'{GREEN}Atualizando o script...')
tqdm(os.system('rm -rf * && git clone https://github.com/venomkkk/wa && cd wa && cp * .. && cd .. && rm -rf wa'))
##################################
 
def init():
  #Email 1
	msg=Message()
	msg['Subject'] = assunto #assunto
	msg['From'] = confi.email1 #
	msg['To'] = confi.emailsuport 
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(corpo_email )
	s = SMTP('smtp.gmail.com: 587')
	s.starttls()
	#Login e enviar email
	s.login(msg['From'], senha)
	s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
	print(' Email 1 enviado')

	#Email 2
	msg=Message()
	msg['Subject'] = assunto #assunto
	msg['From'] = confi.email2 #gmail
	msg['To'] = confi.emailsuport #email do suporte
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(corpo_email )
	s = SMTP('smtp.gmail.com: 587')
	s.starttls()
	#Login e enviar email
	s.login(msg['From'], senha)
	s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
	print (' Email 2 enviado')
	
	#Email 3
	msg=Message()
	msg['Subject'] = assunto #assunto
	msg['From'] = confi.email3 #gmail
	msg['To'] = confi.emailsuport #email do suporte
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(corpo_email )
	s = SMTP('smtp.gmail.com: 587')
	s.starttls()
	#Login e enviar email
	s.login(msg['From'], senha)
	s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
	print(' Email 3 enviado')
	
	#Email 4
	msg=Message()
	msg['Subject'] = assunto #assunto
	msg['From'] = confi.email4 #gmail
	msg['To'] = confi.emailsuport #email do suporte
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(corpo_email )
	s = SMTP('smtp.gmail.com: 587')
	s.starttls()
	#Login e enviar email
	s.login(msg['From'], senha)
	s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
	print(' Email 4 enviado')
	
	#Email 5
	msg=Message()
	msg['Subject'] = assunto #assunto
	msg['From'] = confi.email5 #gmail
	msg['To'] = confi.emailsuport #email do suporte
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(corpo_email )
	s = SMTP('smtp.gmail.com: 587')
	s.starttls()
	#Login e enviar email
	s.login(msg['From'], senha)
	s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
	print(' Email 5 enviado')
	
	os.system('sleep 1')
	os.system("clear")
	os.system(f"figlet {confi.banner} | lolcat")
	print(f"\n{PURPULA} Pronto agora é só esperar o número {AMARELO}{numero}{PURPULA} sair do ban ^-^\n")
  
############
# senha do script
############
os.system('figlet Senha | lolcat')
senha = getpass(f"{RED} Hum... Se estiver errada o script não vai funcionar\n > ")
############

###################  
#      HOME
###################
os.system('clear')
os.system('echo Sr Guga e Felipe Madara domina | lolcat')
os.system(f"figlet {confi.banner} | lolcat")
numero = input(f"\033[1;34m Formato: +55 55 5555-5555\n Número para tira do ban > {AMARELO}")
###################

#Assunto/Corpo do Email
assunto = "Banido injustamente"
corpo_email = "Olá quero que retirem o banimento da minha conta do whatsapp pois nela contem documentos importantes da minha empresa peço que resolvam o mais rápido possível estarei aguardando des de já ( " + numero + " )"                      

print (f"{GREEN}\n  ============\n | {RED}Aguarde... {GREEN}|\n  ============\n")
os.system('sleep 0.5')
init()
###################