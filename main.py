#!/usr/bin/python3
#author: @kodarak / kodraco#6816 (discord) / kodarakK (github)


import os
import math
from time import sleep
from programs import *
import shutil
import sys

#"edit" tot "insl" is voor de text editor te gerbruiken

# edit --> maak file en typ eerste lijntjes
# lose --> dislpay contents file
# cl --> 'change line' --> geef file + lijn nummer (index--> begint bij 0) 
# insl --> "insert line" geef index en insert lijntjes zoveel je wilt en eruit gaan met ctrl - C zoals in edit 

# het heeft een leer curve maar is zeker te doen c:

# de rest is mogelijk om via de code in 'programs.py' te bekijken. 

prgs = ["rekenmachine\n", "comeet\n", "huis hoogte meter (hhm)\n", "konijn\n", "random\n", "edit\n", "lose\n", "cl\n", "insl\n", "mkdir\n", "remf\n", "remdir\n"]

def main():
	# to check for multiple cli arguments this needs to be added
	action = input("\n\n\n> ")  + " extra"
	action = action.split()
	if action[0] == "prg":
		if len(prgs) == 0:
			print("no programs")
			main()
		else:
			[print(i) for i in prgs]
			main()
	elif action[0] == "rekenmachine":
		calc()
		main()
	elif action[0] == "comeet":
		comeet()
		main()
	elif action[0] == "clear":
		os.system("cls")
		main()
	elif action[0] == "hhm":
		huis_hoogte_meter()
		main()
	elif action[0] == "konijn":
		konijnen()
		main() 
	elif action[0] == "random":
		rand()
		main()
	elif action[0] == "edit":
		editor(action[1])
		main()
	elif action[0] == "lose":
		lose(action[1])
		main()
	elif action[0] == "cl":
		if action[1] != "extra" or action[2] != "extra":
			cl(action[1], action[2])
			main()
		else:
			print("no file or line given")
			main()
	elif action[0] == "insl":
		if action[1] != "extra":
			insl(action[1])
			main()
		else:
			print("no file or line given")
			main()
	elif action[0] == "remf":
		if action[1] != "extra":
			remf(action[1])
			main()
		else:
			print("no such file")
			main()
	elif action[0] == "remdir":
		if action[1] != "extra":
			remdir(action[1])
			main()
		else:
			print("no such file")
			main()
	elif action[0] == "mkdir":
		if action[1] != "extra":
			mkdir(action[1])
			main()
		else:
			print("geen dir gegeven")
			main()
	elif action[0] == "exit":
		return
	else:
		main()


if __name__ == "__main__":
	header("mini-os")
	print("om te weten wat te kunnen doen run 'prg'")
	main()
