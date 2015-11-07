# coding: utf-8
import json
import os
import time
import cherrypy
from os import path
from app import authentifizierung

class Datenbank(object):
	exposed = True 
	
	def __init__(self):
		pass
			
	def getThemen(self):
		return os.listdir("./data/themen/")   
	
	def getDiskussionen(self, thema):
		discussions = os.listdir("./data/themen/" + thema)
		output = []
		for discussion in discussions:
			current = dict()
			current["Titel"] = discussion.replace(".json","")
			with open("./data/themen/"+ thema +"/" + discussion) as discussionfile:
				discussionfilecontent = json.load(discussionfile)
			current["Ersteller"] = discussionfilecontent["Ersteller"]
			current["Bearbeiter"] = discussionfilecontent["Bearbeiter"]
			current["Text"] = discussionfilecontent["Text"]
			current["Erstellt"] = discussionfilecontent["Erstellt"]
			current["Bearbeitet"] = discussionfilecontent["Bearbeitet"]
			current["Beitraege"] = discussionfilecontent["Beitraege"]
			output.append(current)
		return output
		
	def createDiskussion(self,thema,discussionname,text):
		discussion = dict()
		discussion["Ersteller"] = cherrypy.session["Benutzername"];
		discussion["Bearbeiter"] = 0;
		discussion["Text"] = text;
		discussion["Erstellt"] = time.asctime()
		discussion["Bearbeitet"] = 0;
		discussion["Beitraege"] = 0;

		outdiscussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		with open(outdiscussionfile, 'w') as outdiscussion:
			json.dump(discussion, outdiscussion)
	
	def deleteDiskussion(self, thema, discussionname):
		discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		current = dict()
		current["Ersteller"] = discussionfile["Ersteller"]
		current["Erstellt"] = discussionfile["Erstellt"]
		if os.path.isfile(discussionfile):
			os.remove(discussionfile)

		

	def editDiskussion(self, thema, discussionname, newdiscussionname):
		if discussionname is not None:
			discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		if os.path.isfile(discussionfile):
			pass
		

	def getBeitraege(self,thema,discussionname):
		output = []
		current = dict()
		with open("./data/themen/" + thema +"/" + discussionname, "r") as discussioncontent:
			discussionfilecontent = json.load(discussioncontent)
		current["Beitraege"]["Ersteller"] = discussionfilecontent["Beitraege"]["Ersteller"]
		current["Beitraege"]["Bearbeiter"] = discussionfilecontent["Beitraege"]["Bearbeiter"]
		current["Beitraege"]["Text"] = discussionfilecontent["Beitraege"]["Text"]
		current["Beitraege"]["Erstellt"] = discussionfilecontent["Beitraege"]["Erstellt"]
		current["Beitraege"]["Bearbeitet"] = discussionfilecontent["Beitraege"]["Bearbeitet"]
		output.append(current)
		return output

	def createBeitrag(self,thema,discussionname,texttitle,text):
		Beitrag = dict()
		Beitrag["Beitraege"]["Ersteller"] = cherrypy.session["Benutzername"];
		Beitrag["Beitraege"]["Bearbeiter"] = 0;
		Beitrag["Beitraege"]["Text"] = text;
		Beitrag["Beitraege"]["Erstellt"] = time.asctime()
		Beitrag["Beitraege"]["Bearbeitet"] = 0;

		pass
	def deleteBeitrag(self,thema,discussionname,beitragID):
		pass
	def editBeitrag(self,thema,discussionname,beitragID):
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