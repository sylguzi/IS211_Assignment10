#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 10"""
import sqlite3
conn = sqlite3.connect('pets.db')
person = (
	(1,'James','Smith',41)
	,(2,'Diana','Greene',23)
	,(3,'Sara','White',27)
	,(4,'William','Gibson',23)
	)
pet = (
	(1,'Rusty','Dalmation',4,1)
	,(2,'Bella','Alaskan Malamute',3,0)
	,(3,'Max','CockerSpaniel',1,0)
	,(4,'Rocky','Beagle',7,0)
	,(5,'Rufus','CockerSpaniel',1,0)
	,(6,'Spot','Bloodhound',2,1)
	)
per_pet = (
	(1,1)
	,(1,2)
	,(2,3)
	,(2,4)
	,(3,5)
	,(4,6)
	)
#execute "Executes an SQL statement. The SQL statement may be parameterized 
#(i. e. placeholders instead of SQL literals). The sqlite3 module 
#supports two kinds of placeholders: question marks (qmark style) 
#and named placeholders"

#make sure to add "\ at the end of each
with conn:
	cur = conn.cursor()
	cur.execute("CREATE TABLE person("\
				"id INTEGERPRIMARYKEY,"\
				"first_name TEXT,"\
				"last_name TEXT,"\
				"age INTEGER)")
	cur.execute("CREATE TABLE pet("\
				"id INTEGER PRIMARY KEY,"\
				"name TEXT,"\
				"breed TEXT,"\
				"age INTEGER,"\
				"dead INTEGER)")
	cur.execute("CREATE TABLE person_pet("\
				"person_id INTEGER,"\
				"pet_id INTEGER)")

#executemany: "Execute a database operation (query or command) 
#against all parameter tuples or mappings found in the sequence" 
	cur.executemany("INSERT INTO person VALUES(?,?,?,?)",person)
	cur.executemany("INSERT INTO pet VALUES(?,?,?,?,?)",pet)
	cur.executemany("INSERT INTO person_pet VALUES(?,?)",per_pet)