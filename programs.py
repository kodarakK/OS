#!/usr/bin/python3

#author: @kodarak / kodraco#6816 (discord) / kodarakK (github)


import math, os, random
from main import *
from time import sleep
import shutil
import sys

def header(app):
	#os.system("clear")
	text = f"Welkom to {app}"
	print(len(text) * '~')
	print(text)
	print(len(text) * '~')


def comeet():
	header("comeet")
	for i in range(20):
		os.system("clear")
		
		print(i*'\n' + i * ' ' + "-----------------\n" + i * ' ' + "|               |\n" +
		      i * ' ' + "|               |\n" + i * ' ' + "|               |\n" +
		      i * ' ' + "|               |\n" + i * ' ' + "|               |\n" +
		      i * ' ' + "|               |\n" + i * ' ' + "-----------------")
		sleep(0.2)

def calc():
	header("rekenmachine")
	while True:
		try:
			input_value = input("enter an expression \n/rekenmachine/> ")
			if input_value == "exit":
				return
			uitkomst = eval(input_value)
			break
		except NameError:
			print("kan niet")
	print(uitkomst)
	calc()


def huis_hoogte_meter():
	header("huis hoogte meter")
	while True:
		try:
			hoek = input("Hoek graden invoeren\n/hhm/>")
			if hoek == "exit":
				return
			afstand = input("Afstand in meters invoeren\n/hhm/>")
			if afstand == "exit":
				return
			else:
				hoek = float(hoek)
				afstand = float(afstand)
			break
		except ValueError:
			print("invoer is fout!")

	# brekeningen
	hoek = hoek * 2 * math.pi / 360
	hoogte = afstand * math.tan(hoek)
	os.system("cls")
	print(f"Het huis is {int(hoogte)} m hoog.")
	huis_hoogte_meter()


def konijnen():
	header("konijnen populatie!")
	for i in range(10):
		populatie = 2 * math.exp(math.log(15) * i)
		print(f"Na jaar {i}: {populatie} dieren. ")


def rand():
	header("willekeurig getal")
	while True:
		try:
			min = input("\nminimum:\nrand>")
			if min == "exit":
				return
			max = input("\nmax:\nrand>")
			if max == "exit":
				return
			else:
				min = float(min)
				max = float(max)
			break
		except ValueError:
			print("invoer is fout!")
	if min > max:
		print("min > max ==> klopt niet!!")
		sleep(5)
		rand()
	print(random.randrange(min, max))
	rand()


def editor(filename):
	os.system("clear")
	print("TEXT EDITOR   <ctrl> - C TO EXIT:\n")
	while True:
		try:
			input_value = input(":")
			with open(filename, 'a+') as f:
				f.write(input_value + "\n")
		except KeyboardInterrupt:
			print("  bye bye :3")
			break


def lose(filename):
	os.system("clear")
	print(f"filename: {filename}\n\n")
	if filename ==  "extra":
		print("geen bestands naam gegeven")
	else:
		with open(filename, "r") as f:
			print(f.read())


def cl(filename, line):
	with open(filename, 'r') as f:
		data = f.readlines()
	new_line = input(":")
	data[int(line)] = new_line + "\n"
	with open(filename, 'w') as f:
		f.writelines(data)


def insl(filename):
	value = ""
	index = int(input("index: "))

	while True:
		try:
			value += input(":") + "\n"
		except KeyboardInterrupt:
			print("  bye bye :3")
			break
	with open(filename, "r") as f:
		contents = f.readlines()
	contents.insert(index, value)
	with open(filename, "w") as f:
		contents = "".join(contents)
		f.write(contents)


def remf(filename):
	try:
		os.remove(filename)
		print(f"succelfully removed {filename}")
	except OSError as e:
		print(f"Error: {e.filename} - {e.strerror}")

def remdir(dir):
	try:
		shutil.rmtree(dir)
		print(f"succesfully removed {dir}")
	except OSError as e:
		print(f"Error: {e.filename} - {e.strerror}")

def mkdir(name):
	os.mkdir(name)
