import os, webbrowser,sys
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def Colombia():
	limpiar()
	print '''
                                   \033[1;32m 1. Usersherlock
                                   \033[1;32m 2. Usersearch
                                   \033[1;32m 3. Namechk
                                   \033[1;32m 4. linkedin
                                   \033[1;32m 5. About.me
                                   \033[1;32m 6. Pipl
	                           \033[1;32m 7. GoogleProfile
         	                   \033[1;32m 8. Twitter
	                           \033[1;32m 9. Facebook
	                           \033[1;32m 10.Instagram
	                           \033[1;32m 11.EPS
	                           \033[1;32m 12.Libreta militar
	                           \033[1;32m 13. Comparendos
	                           \033[1;32m 14. Antecedentes
	                           \033[1;32m 15. RUNT
	                           \033[1;32m 16. Sisben
				   \033[1;32m 17. exit
	'''
	k = raw_input("\033[1;30m DOXING ERROR404 > ")
	if k == "1":
		webbrowser.open('http://usersherlock.com')
	if k == "3":
 		webbrowser.open('http://namechk.com/')
	if k == "4":
 		webbrowser.open('http://www.linkedin.com/')
	if k == "6":
 		webbrowser.open('https://pipl.com/')
	if k == "7":
 		webbrowser.open('https://profiles.google.com/')
	if k == "8":
	    	webbrowser.open('https://twitter.com/')
	if k == "9":
   		webbrowser.open('http://www.facebook.com/')
	if k == "10":
    		webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
	if k == "11":
    		webbrowser.open('http://www.fosyga.in/fosyga/')
	if k == "12":
    		webbrowser.open('https://www.libretamilitar.mil.co/modules/consult/militarysituation')
	if k == "13":
   		webbrowser.open('https://www.simbogota.com.co/index.php?option=com_content&view=article&id=419&Itemid=376')
	if k == "14":
		webbrowser.open('https://antecedentes.policia.gov.co:7005/WebJudicial/formAntecedentes.xhtml')
	if k == "15":
  		webbrowser.open('https://www.runt.com.co/consultaCiudadana/#/consultaPersona')
	if k == "16":
		 webbrowser.open('http://www.sisben.gov.co/atencion-al-ciudadano/Paginas/consulta-del-puntaje.aspx')
	if k == "17":
		sys.exit()
while True:
	Colombia()
