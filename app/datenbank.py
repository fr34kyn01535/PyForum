# coding: utf-8
import json
import os
import time
import cherrypy
import copy
import uuid
from os import path
from app import authentifizierung
from operator import itemgetter


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
			with open("./data/themen/"+ thema +"/" + discussion) as discussionfile:
				discussion = json.load(discussionfile)
			output.append(discussion)
		return sorted(output, key=itemgetter('Erstellt'), reverse=True) 
		
		
	def createDiskussion(self,thema,title,text):
		discussion = dict()
		discussion["Ersteller"] = cherrypy.session["Benutzername"]
		discussion["Titel"] = title
		discussion["Bearbeiter"] = " "
		discussion["Text"] = text
		discussion["Erstellt"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		discussion["Bearbeitet"] = " "
		discussion["Beitraege"] = [ ]
		discussion["Status"] = " "
		discussion["ID"] = str(uuid.uuid4())

		discussionpath = "./data/themen/" + thema +"/" + discussion["ID"] + ".json"
		with open(discussionpath, 'w') as discussionfile:
			json.dump(discussion, discussionfile,indent=4)
	

	def edit(self, thema,id,title,text,beitragID=None):
		discussionpath = "./data/themen/" + thema +"/" + id + ".json";
		
		with open(discussionpath, 'r') as discussionfile:
			discussion = json.load(discussionfile)

		if beitragID == None:
			discussion["Titel"] = title
			discussion["Text"]  = text
			discussion["Bearbeiter"] = cherrypy.session["Benutzername"]
			discussion["Bearbeitet"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		else:
			for post in discussion["Beitraege"]:
				if post["ID"] == beitragID:
					post["Titel"] = title
					post["Text"]  = text
					post["Bearbeiter"] = cherrypy.session["Benutzername"]
					post["Bearbeitet"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
				
		with open(discussionpath, 'w') as discussionfile:
			json.dump(discussion, discussionfile,indent=4)


	def getDiskussion(self,thema,id):
		discussionpath = "./data/themen/" + thema +"/" + id + ".json";
		
		with open(discussionpath, "r") as discussionfile:
			discussion = json.load(discussionfile)

		discussion["Beitraege"] = sorted(discussion["Beitraege"], key=itemgetter('Erstellt')) 
		
		if authentifizierung.IsLoggedIn():
			length = len(discussion["Beitraege"] ) 
			if length == 0 and cherrypy.session["Benutzername"] == discussion["Ersteller"]:
				discussion["Bearbeitbar"]  = True
			else:
				discussion["Bearbeitbar"]  = False
				id = None
				if discussion["Beitraege"] [length-1]["Ersteller"] == cherrypy.session["Benutzername"] :
					id = discussion["Beitraege"] [length-1]["ID"]
				
				for post in discussion["Beitraege"]:
					if id != None and id ==post["ID"] :
						post["Bearbeitbar"]  = True
					else:
						post["Bearbeitbar"]  = False
		else:
			discussion["Bearbeitbar"]  = False
			for post in discussion["Beitraege"]:
					post["Bearbeitbar"]  = False
					
		return discussion
		

	def createBeitrag(self,thema,id,title,text):
		discussionpath = "./data/themen/" + thema +"/" + id + ".json";
		post = dict()
		with open(discussionpath) as discussionfile:
			discussion = json.load(discussionfile)
		
		post["Titel"] = title
		post["Ersteller"] = cherrypy.session["Benutzername"];
		post["Bearbeiter"] = " ";
		post["Text"] = text;
		post["Erstellt"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime());
		post["Bearbeitet"] = " ";
		post["Status"] = " "
		post["ID"] = str(uuid.uuid4())

		discussion["Beitraege"].append(post)#.copy()

		with open(discussionpath, 'w') as discussionfile:
			json.dump(discussion, discussionfile,indent=4)

	def delete(self,thema,id,beitragID=None):
		discussionpath = "./data/themen/" + thema +"/" + id + ".json";
		with open(discussionpath, "r") as discussionfile:
			discussion = json.load(discussionfile)

		if beitragID == None:
			if discussion["Status"] == "deleted":
				discussion["Status"] = " "
			else:
				discussion["Status"] = "deleted"
			
			discussion["Bearbeiter"] = cherrypy.session["Benutzername"]
			discussion["Bearbeitet"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		else:
			for post in discussion["Beitraege"]:
				if post["ID"] == beitragID:
					if post["Status"] == "deleted":
						post["Status"] = " "
					else:
						post["Status"] = "deleted"
					post["Bearbeiter"] = cherrypy.session["Benutzername"]
					post["Bearbeitet"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())	

		with open(discussionpath, 'w') as discussionfile:
			json.dump(discussion, discussionfile,indent=4)
		
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