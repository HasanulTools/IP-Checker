import requests
import os
import pprint
import requests
import os
import pprint
logo = ("""\33[1;36m
__  __                             __   
   / / / /___ __________ _____  __  __/ /   
  / /_/ / __ `/ ___/ __ `/ __ \/ / / / /    
 / __  / /_/ (__  ) /_/ / / / / /_/ / /     
/_/ /_/\__,_/____/\__,_/_/ /_/\__,_/_/

\33[1;35m═════════════════════════════════════════════════
═══════════
\33[1;92mFACEBOOK : Hasan Gaming
GITHUB            : HasanulTools
FACEBOOK PAGE     : নেই
TOOL              :   IP ADDRESS (PYTHON)
NUMBER            :01762554481

             \33[1;31mIP ADDRESS 
\33[1;35m═══════════════════════════════════════════════════
════════

""")

print(logo)
while True:
	def ip():
		ip=str(input("\n\n\nEnter Ip Address :  "))
		url=f"https://ipapi.co/{ip}/json/"
		r=requests.get(url)
		pprint.pprint(r.json())
	ip()
while True:
	def ip():
		ip=str(input("\n\n\nEnter Ip Address :  "))
		url=f"https://ipapi.co/{ip}/json/"
		r=requests.get(url)
		pprint.pprint(r.json())
	ip()
