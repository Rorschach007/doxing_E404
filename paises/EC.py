# -*- coding: utf-8 -*-
import sys,os
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def Ecuador():
	limpiar()
    	print '''
    {0}Aqui podras obtener datos de Ecuador
    {3}1.{1}{2} Datos de Interes
    {3}2.{1}{2} Gestion Fiscalias
    {3}3.{1}{2} Paginas Amarillas
    {3}4.{1}{2} SRI
    {3}5.{1}{2} Salir
    '''.format(GREEN, END, CYAN, RED)
	d = raw_input("\033[36m ECUADOR > ") 
	if d == "1":
    		print ('\033[1;33m Llena el campo para obtener la informacion')
    		ID=raw_input('\33[46m Ingrese su Cedula: \033[0m')
    		num = "http://si.secap.gob.ec/sisecap/servicioObtieneDatosRegistroCivil.php?num_doc="
    		ID=str(ID)
     		if len(ID) != 10:
			print ('La cedula debe tener 10 digitos')
			wait = raw_input("PRESIONA ENTER PARA CONTINUAR.")
     		else: 
        		print ('Estamos buscando la info requerida')
			output=os.system('curl '+num+ID)
    	   		print ('')
        		print ('')
			print ('Busqueda Finalizada')
			print ('')
			wait = raw_input("PRESIONA ENTER PARA CONTINUAR.")
while True:
	Ecuador()
