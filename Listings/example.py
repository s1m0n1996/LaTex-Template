#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

a = {
    "Winter": {
        "temperatur": "kalt"
    },
    "Sommer": {
        "temperatur": "warm"
    }
}

def print_jahreszeiten:
	""" Gibt die jahreszeiten aus dem dict aus
	und gibt die temperatur an
	"""
	jahreszeiten = a.keys()
	for jahreszeit in jahreszeiten:
		temperatur = a[jahreszeit]["temperatur"]

		print(f"Im {jahreszeit} ist es {temperatur}")
		
def hello_world(text: str):
	print("hello world")
	print(text)
	
def teiler(zahl: int):
	""" Gibt alle teiler der Zahl aus	
	"""

	print(f"Ganzzahlige Teiler von {zahl}:")
	starttime = datetime.utcnow()

	for i in range(1, zahl):
		if zahl % i == 0:
			print(i)
		# kein ganzzahliger Teiler mehr möglich
		if i > zahl / 2:
			break

	exec_time = datetime.utcnow() - starttime
	print(f"Ausführungszeit: {exec_time}")

if __name__ == '__main__':
	teiler()