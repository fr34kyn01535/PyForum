# coding: utf-8
import json
import os

class Datenbank(object):
	exposed = True 
	
	def __init__(self):
		pass
			
	def getThemen(self):
		return os.listdir("./data/themen/")   
# EOF