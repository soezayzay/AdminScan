import threading
import requests
import argparse
from colorama import Fore,Back,Style
import os,sys
#colors 
red = Fore.RED 
green = Fore.GREEN
reset = Style.RESET_ALL
#AdminPanelScan
def scan(dire):
   success = True
   url = args.url
   errors = ["404","not found","403","forbidden","access denied","error"]
   response = requests.get(f"{url}{dire}")
   if response.status_code == 200 :
      for error in errors :
          if error in response.text.lower():
             success = False
             print(f" (+){red} {url}{dire}{reset}")
             break
      if success == True :
         print(f" (+){green} {url}{dire}{reset}")
   else :
      print(f" (+){red} {url}{dire}{reset}")
#Main
def AdminPanelScan() : 
    dirs = []
    wordlist = args.wordlist
    file = open(wordlist,"r").readlines()
    for i in file :
        i = i.strip()
        dirs.append(i)
    for dire in dirs :
        process = threading.Thread(target=scan,args=(dire,))
        process.start()
#Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",help="Target Url")
parser.add_argument("-w","--wordlist",help="Wordlist File")
parser.add_argument("--scan",help="AdminPanel Scan",action="store_true")
args = parser.parse_args()
if args.url and args.wordlist and args.scan :
   AdminPanelScan()
else :
   file = os.path.basename(__file__)
   os.system(f"python {file} -h")
   
