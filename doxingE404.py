# -*- coding: utf-8 -*-
import sys, os, webbrowser, platform
<<<<<<< HEAD
from time import sleep
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
=======
>>>>>>> 83ce73646894b8c4fe0026f8755848e34c33fe79
##Def funciones
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
<<<<<<< HEAD
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
sleep(1)
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

=======
def menu():
	limpiar()
def Colombia():
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
	                              	\033[1;32m 17. Salir  	  
	'''
	k = raw_input("\033[1;30m DOXING ERROR404 > ")
	if k == "1":
			webbrowser.open('http://usersherlock.com/')
    	menu()
	if k == "3":
    		webbrowser.open('http://namechk.com/')
    	menu()	
	if k == "4":
    		webbrowser.open('http://www.linkedin.com/')
    	menu()
	if k == "6":
    		webbrowser.open('https://pipl.com/')
    	menu()
	if k == "7":
    		webbrowser.open('https://profiles.google.com/')
    	menu()
	if k == "8":
    		webbrowser.open('https://twitter.com/')
    	menu()
	if k == "9":
    		webbrowser.open('http://www.facebook.com/')
    	menu()
	if k == "10":
    		webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
    	menu()
	if k == "11":
    		webbrowser.open('http://www.fosyga.in/fosyga/')
    	menu()
	if k == "12":
    		webbrowser.open('https://www.libretamilitar.mil.co/modules/consult/militarysituation')
	   	menu()
	if k == "13":
   			webbrowser.open('https://www.simbogota.com.co/index.php?option=com_content&view=article&id=419&Itemid=376')
    	menu()
	if k == "14":
			webbrowser.open('https://antecedentes.policia.gov.co:7005/WebJudicial/formAntecedentes.xhtml')
    	menu()
	if k == "15":
    		webbrowser.open('https://www.runt.com.co/consultaCiudadana/#/consultaPersona')
    	menu()
	if k == "16":
		 	webbrowser.open('http://www.sisben.gov.co/atencion-al-ciudadano/Paginas/consulta-del-puntaje.aspx')
    	menu()
	if k == "17":
    		sys.exit()
## Fin funcion Colombia

print """
				\033[1;31m        PRUEBA DE HERRAMIENTAS
				\033[1;34m           ERROR404 
				\033[1;35m  Recopilacion De Informacion
                            `--------.```   ```.--------`                               
                         `----.   `-:/+oosssssssoo+/:.`  `-::--`                          
                      --:-` `-/shdmmmmddhyyyyyyyhdmmmmmdyo/-` `-::.                       
                   -::` `:ohmmmdyo/:.`            ``-:+oydmmdy+-` .::.                    
                `::` `/ydmmyo:.                          `./ohmmds:` .::`                 
              .:-  :sdmds/`                                   ./ymmds- `::`               
            .:- `/hmmy/`                                         ./hmmh: `-:`             
          `:- `+dmdo.    ``                                        `-smmh: `::            
         -/` :hmmo.     `ys`                                   `      -smmy- `/.          
        :- `smmy-       +mmd+                                 +h        :hmdo` ::         
      `/. -hmd/`        hmmmm:       :sh+        `--        `/mm.        `ommy. -/        
     `/` :dmh-         .mmmmm:  .:+oodmmdo+-`.-/ohmdy+-.    ommm-          :dmd- ./       
     +` /dmh.          -mmmmm+shdmmmmmmmmmms/+hmmmmmmmmdhs:.+mmm-           -dmd- ./      
    /. :dmh`           .mmmmdymmmmmmmmmmmy.   .hmmmmmmmmmmmddmmm-            -dmd. -:     
   -- .dmd.             dmmm+`hmmmmmmmmmm+:/oo:ommmmmmmmmmms-dmm-             :mmh` /.    
  `+  ymm:              smmm` /mmmmmmmmmmdmmmmmy+dmmmmmmmmh` ymm-              +mm+  +    
  /. -mmy               /mmd   :oyhyyo+ymmmmmmmmy:+shdmmho.  ymm-              `hmd. :-   
  +  ymm-               -mmm/    -::-:smmmmmmmmmmd/---..`    omm-               +mm+  +   
 ./ `mmd                 smmd/```-dmmmmmmmmmmmmmmmmmhys`    -smy`               `mmh  +   
 :. -mms                 `hmmmhhh+ymmmmmmdmmdmmmmmmmddmhyo+odmd.                 hmm` /.  
 +` /mm+             `..  smmmmmmmmmmmmho/hdhhy+ydmmmmmmmmmmmmo `.`              smm- --  
 +` /mm+         `-/shddo`-dmmmmmmmmmysyo:....-+yhsdmmmmmmmmmd::hdhy+:.`         smm- -:  
 /` /mm+    `.:/shmmmmmmmh/:hmmmmmmmhhd:```    `.+ysdmmmmmmmh/smmmmmmmdh+:-`     smm- :-  
 :- -mms   sydmmmmmmmmmmmmms/mmmmmmmmm+.:-: +``--`ymmmmmmmmh+dmmmmmmmmmmmmmhy:   hmm` /`  
 `/ `dmd   ysmmmmmmmmmmmmmmmmmmmmmmmmm+```.`.``..-hmmmmdmmmmmmmmmmmmmmmmmmmds:  .mmy  +   
  +  smm:  .:+mmmmmmmmdddhhsymmmmmhmmmmo//s-oooyommhsmhhmmmdsydddddmmmmmmmy/-   omm/ `+   
  :- .mmh`  `/hmmddhhd-..`.:ommmmdhmmmmdmyo/oohdmds+dmhmmmmh/-``..odhddmmm:/   .dmd` /.   
   +  omm+   /.mdo.``/o` `smmmmmmddhdmh+osyyyyso+oymhdddmmmmmd:  -s-`.-hms-.   smm/ `+    
   ./ `hmm-    hd/-  .my`ymmmmmmm:-`.smmhyssooshdmd/`.-ommmmmmm-:do  .:sd+    /mms  +`    
    :- .dmd-    /dso/hmmhommmmmmms   `ommmmmmmmmmd-   .dmmmmmmh/mmms:hyh.    :mmh` :-     
     /. -dmd-   `shommmmmdmmmmmmmm: :sdmmmmmmmmmmmho` ymmmmmmmdmmmmmhsy:    /dmh. -:      
      /. -hmd/   `.`smmmmmmmmmmmmd+ ./mmmmmdymmmmmh-`.hdmmmmmmmmmmmm.`    `+mmy` -:       
       :- `ymms`  .`.dmmmmmmmdy+-`    ymmddy:dddmm-    ./shdmmmmmmmo`.   .ymmo` :-        
        -:` +dmd/`  `:dmmdh+:.        ./-.`  ``-:/        `-/sdmmmh:`  `+dmh: `/.         
         `/. .smmy:` /oy/.                                    `:oso- `/hmdo` -/`          
           -:` -ymmh/``                                          ```+hmds. ./.            
             ::` -sdmdo-`                                       `:sdmdo. `:-              
              `::` .+hmmho:`                                 `:sdmdy/` .:-                
                 -:-` -+hdmdyo:.`                       `./ohmmdy+. `::.                  
                   `-:-` .:ohdmmdys+/:-.``     ``.-:/oshdmmdyo:` `::-                     
                      `-::-  `-/oyhdmmmmmmddddmmmmmmmdhso/-` `-::-                        
                          `-----`   `--://+++++//:-.`   `-:---`                           
                               `.-----------------------.                                 
           ███████╗██████╗ ██████╗  ██████╗ ██████╗     ██╗  ██╗ ██████╗ ██╗  ██╗
           ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██║  ██║██╔═████╗██║  ██║
           █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝    ███████║██║██╔██║███████║
           ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗    ╚════██║████╔╝██║╚════██║
           ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║         ██║╚██████╔╝     ██║
           ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝         ╚═╝ ╚═════╝      ╚═╝
						\033[1;32m 1. Argentina
						\033[1;32m 2. Bolivia
						\033[1;32m 3. Chile
						\033[1;32m 4. Colombia
						\033[1;32m 5. Ecuador
						\033[1;32m 6. Mexico
						\033[1;32m 7. Peru
						\033[1;32m 8. Venezuela
						\033[1;32m 9. Facebook Error404
						\033[1;32m 10. Salir
				"""
>>>>>>> 83ce73646894b8c4fe0026f8755848e34c33fe79
d = raw_input("\033[1;30m DOXING ERROR404 > ")

if d == "1":
	Argentina()
elif d == "2":
	Bolivia()
elif d == "3":
	Chile()
elif d == "4":
<<<<<<< HEAD
	execfile("paises/CO.py")
elif d == "5":
	execfile("paises/EC.py")
=======
	Colombia()
elif d == "5":
	ID=input('Ingrese numero de cedula: ')
	num = "http://si.secap.gob.ec/sisecap/servicioObtieneDatosRegistroCivil.php?num_doc="
	ID=str(ID)
	if len(ID) != 10:
		print ('La cedula debe tener 10 digitos')
	else: 
		output=os.system('curl '+num+ID)
		print ('')
		print ('')
>>>>>>> 83ce73646894b8c4fe0026f8755848e34c33fe79
elif d == "6":
	Mexico()
elif d == "7":
	Peru()
elif d == "8":
	Venezuela	
elif d == "9":
	webbrowser.open (' https://www.facebook.com/error4o4.org/') 
elif d == "10":
<<<<<<< HEAD
	sys.exit()
=======
	sys.exit()
>>>>>>> 83ce73646894b8c4fe0026f8755848e34c33fe79
