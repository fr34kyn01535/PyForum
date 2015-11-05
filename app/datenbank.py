# coding: utf-8
import json
import os
from os import path

class Datenbank(object):
	exposed = True 
	
	def __init__(self):
		pass
			
	def getThemen(self):
		return os.listdir("./data/themen/")   
	
	def getDiskussionen(self, thema):
		return os.listdir("./data/themen/" + thema)
		
	def createDiskussion(self, thema, discussionname):
		pass

	def deleteDiskussion(self, thema, discussionname):
		pass

	def editDiskussion(self, thema, discussionname):
		pass

	
			

	def loginBenutzer(self,username,password):
		benutzer = self.getBenutzer(username)
		if benutzer == None:
			return None
		if benutzer["Passwort"] != password:
			return None
		return benutzer
	
	def getBenutzer(self,username):
		userfile = "./data/benutzer/" + username + ".json";
		if os.path.isfile(userfile):
			with open(userfile) as userfilecontent:
				user = json.load(userfilecontent)
			return user
		else:
			return None
			
	def deleteBenutzer(self,username):
		userfile = "./data/benutzer/" + username + ".json";
		if os.path.isfile(userfile):
			os.remove(userfile)
	
	def getAllBenutzer(self):
		users = os.listdir("./data/benutzer/")
		output = []
		for user in users:
			current = dict()
			current["Benutzername"] = user.replace(".json","")
			with open("./data/benutzer/"+user) as userfile:
				userfilecontent = json.load(userfile)
			current["Rolle"] = userfilecontent["Rolle"]
			output.append(current)
		return output
	
	
	def editBenutzer(self,username,newusername,password,role):
		if username is not None:
			userfile = "./data/benutzer/" + username + ".json";
			if os.path.isfile(userfile):
				os.remove(userfile)
		user = dict()
		user["Passwort"] = password;
		user["Rolle"] = role;
		outuserfile = "./data/benutzer/" + newusername + ".json";
		with open(outuserfile, 'w') as outuser:
			json.dump(user, outuser)


# EOF