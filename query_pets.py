#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 10"""
import sqlite3
import sys

#connect to database, ask for user identity, check existance, print data,
#otherwise print error message, do it until user identification is -1
conn = sqlite3.connect('pets.db')
identity = raw_input("Person ID: ")

if identity == "-1":
	sys.exit()

try:
	curs = conn.cursor()
	curs.execute("SELECT first_name,last_name,per.age,name,pet.age,breed,dead "\
				"FROM person per "\
				"INNER JOIN person_pet pp ON per.id = pp.person_id "\
				"INNER JOIN pet pet ON pet.id = pp.pet_id "\
				"WHERE per.id = ?",identity)

	fetch = curs.fetchall() # entire result set will be stored on the client side
	for row in fetch:
		if row[6]:
			tense1 = 'had'
			tense2 = 'was'
		else:
			tense1 = 'has'
			tense2 = 'is'
		print "{} {},Age {}".format(row[0],row[1],row[2])
		print "{} {} a {} named {} that {} {} years old".format(
			row[0],tense1,row[5],row[3],tense2,row[4])
	
except sqlite3.Error as err:
	raise sqlite3.Error(err)