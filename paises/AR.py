import os, webbrowser,sys
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def Argentina():
	limpiar()
	print '''
               {0}Aqui podras obtener datos de Argentina 
                {3}1.{1}{2} Usersherlock
                {3}2.{1}{2} Usersearch
                {3}3.{1}{2} Namechk
                {3}4.{1}{2} linkedin
                {3}5.{1}{2} Pipl
	        {3}6.{1}{2} GoogleProfile
         	{3}7.{1}{2} Twitter
	        {3}8.{1}{2} Facebook
	        {3}9.{1}{2} Instagram
		{3}10.{1}{2} Salir
	'''.format(GREEN, END, CYAN, RED)
	a = raw_input("\033[1;30m DOXING ERROR404 > ")
	if a == "1":
		webbrowser.open('http://usersherlock.com')
        if a == "2":
		webbrowser.open('https://usersearch.org/')
	if a == "3":
 		webbrowser.open('http://namechk.com/')
	if a == "4":
 		webbrowser.open('http://www.linkedin.com/')
	if a == "5":
 		webbrowser.open('https://pipl.com/')
	if a == "6":
 		webbrowser.open('https://profiles.google.com/')
	if a == "7":
	    	webbrowser.open('https://twitter.com/')
	if a == "8":
   		webbrowser.open('http://www.facebook.com/')
	if a == "9":
    		webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
	if a == "10":
		sys.exit()
while True:
	Argentina()
