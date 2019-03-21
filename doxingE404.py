# -*- coding: utf-8 -*-
import sys, os, webbrowser, platform
from time import sleep
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
##Def funciones
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def logo():
      print '''        
       {0}    ``      {2}D O X I N G{1}      ``            
          -h-`                        -           
          dMMy     `::`     ```      :N-          
         `MMMm`.:+shMNy+-./ohNd+:.` /NM/          
         .MMMmdNMMMMMMMh/-yMMMMMMNdsyMM+          
         `NMM+yMMMMMMMm/+o:dMMMMMMMNoNM+          
          yMm`-dNMNNmNNMMMMdhmNMMMm/`dM+          
          +MN-``:++/oNMMMMMMh/+oo/-``hM/          
          `dMm/::hmNMMNMMMMMMNmho-../hm`          
         ` /MMMMNmMMMmdmmmmmNMMNNNmmMM: `         
    `-+ydmo.dMMMMMMmhy/---:ohdNMMMMMMm:hmhs/-     
./shmNMMMMMd+dMMMMMms-.-.-..:hmMMMMMddNMMMMMNdy+: 
:hNMMMMMMMMMNNMMNMMNo-.-----/dNMNNMMNMMMMMMMMMMNs 
 -sMMMMMmyys+dMMNmMNNhyo+oydNmhNmNNMsoyyyNMMMMN+` 
  :dNs::o.`:dNMMNNmNmhhyyhyyydmNNMMMNy.`:o:/hMo-  
   +do-.ym+NMMMMd.`:mNmmddmNNs.`/MMMMMhsN/`/hh.   
    -ddmMMNNMMMMM/ :hMMMMMMMNs. hMMMMMdMMNdds     
     ..yMMMMMMMMd+ -mMMMdNMMMs``yNMMMMMMMM-.      
       .mMMMdy/.   {2}ERROR 404{1}   `-ohNMMMs`       
       `+y+.           ```           `-sy:                             
       {3}Dedicado para el grupo de Error404 
  Este script esta hecho con fines eduacativos{2} '''.format(GREEN, END, CYAN, RED)

logo()
sleep(0.7)
limpiar()
sleep(0.3)
logo()
sleep(0.3)
limpiar()
sleep(0.3)
logo()
sleep(0.3)
limpiar()
sleep(0.3)
logo()
sleep(0.3)
limpiar()

def menuc():
    print '''
{3}*{1}{0} Este Script esta hecho con la Colaboracion de Varios Programadores
                Esperamos que les sea util{1} {3}Error404{0}'''.format(GREEN, END, CYAN, RED, WHITE)
def menu():
    print '''
         {3}1.{1} {2} Argentina
	 {3}2.{1} {2} Bolivia						
	 {3}3.{1} {2} Chile						
	 {3}4.{1} {2} Colombia						
	 {3}5.{1} {2} Ecuador						
	 {3}6.{1} {2} Mexico						
	 {3}7.{1} {2} Peru						
	 {3}8.{1} {2} Venezuela						
	 {3}9.{1} {2} Facebook Error404						
	 {3}10.{1}{2} Salir						
				'''.format(GREEN, END, CYAN, RED)
limpiar()
menuc()
menu()
d = raw_input("\033[1;30m DOXING ERROR404 > ")

if d == "1":
	Argentina()
elif d == "2":
	Bolivia()
elif d == "3":
	Chile()
elif d == "4":
	execfile("paises/CO.py")
elif d == "5":
	execfile("paises/EC.py")
elif d == "6":
	Mexico()
elif d == "7":
	Peru()
elif d == "8":
	Venezuela	
elif d == "9":
	webbrowser.open (' https://www.facebook.com/error4o4.org/') 
elif d == "10":
	sys.exit()
