# coding: utf-8
import json
import os
import time
import cherrypy
import copy
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
			#current["BeitragID"] = discussionfilecontent["BeitragID"]
			output.append(current)
		return output
		
	def createDiskussion(self,thema,discussionname,text):
		discussion = dict()
		discussion["Ersteller"] = cherrypy.session["Benutzername"];
		discussion["Bearbeiter"] = 0;
		discussion["Text"] = text;
		discussion["Erstellt"] = time.asctime();
		discussion["Bearbeitet"] = 0;
		discussion["Beitraege"] = 0;

		outdiscussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		with open(outdiscussionfile, 'w') as outdiscussion:
			json.dump(discussion, outdiscussion)
	
	def deleteDiskussion(self, thema, discussionname):
		discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		current = dict()

		with open(discussionfile, 'r') as discussionfilecontent:
			discussioncontent = json.load(discussionfilecontent)
		current["Ersteller"] = discussioncontent["Ersteller"];
		current["Erstellt"] = discussioncontent["Erstellt"];
		current["Titel"]  = "Diese  Diskussion Wurde vom Admin gelöscht";

		outdiscussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		with open(outdiscussionfile, 'w') as outdiscussion:
			json.dump(discussion, outdiscussion)
		
		if os.path.isfile(discussionfile):
			os.remove(discussionfile)

		

	def editDiskussion(self, thema, discussionname, newdiscussionname,text=None):
		#
		discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		outfile = "./data/themen/" + thema +"/" + newdiscussionname + ".json";

		with open(discussionfile, 'r') as currentfile:
			current = json.load(currentfile)
		current["Bearbeiter"] = cherrypy.session("Benutzername");
		current["Bearbeitet"] = time.asctime();
		current["Text"]  = text;

		with open(outfile, 'w') as out:
			json.dump(current, out)

		if os.path.isfile(currentfile):
			os.remove(currentfile)
			pass
		

	def getBeitraege(self,thema,discussionname):
		discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		output = []
		current = dict()
		with open(discussionfile, "r") as discussionfilecontent:
			discussioncontent = json.load(discussionfilecontent)

	#erste Beitrag(=diskussion) gesondert
		current["Titel"] = discussionname;
		current["Ersteller"] = discussioncontent["Ersteller"]
		current["Bearbeiter"] = discussioncontent["Bearbeiter"]
		current["Text"] = discussioncontent["Text"]
		current["Erstellt"] = discussioncontent["Erstellt"]
		current["Bearbeitet"] = discussioncontent["Bearbeitet"]
		output.append(current)
	#restlichen beiträge
		for posts in discussioncontent["Beitraege"]:
			for post in posts:
				current["Titel"] = post["Titel"];
				current["Ersteller"] = post["Ersteller"]
				current["Bearbeiter"] = post["Bearbeiter"]
				current["Text"] = post["Text"]
				current["Erstellt"] = post["Erstellt"]
				current["Bearbeitet"] = post["Bearbeitet"]
				output.append(current)
		return output
		

	def createBeitrag(self,thema,discussionname,texttitle,text):
		discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		post = dict()
		with open(discussionfile) as discussionfilecontent:
			discussioncontent = json.load(discussionfilecontent)
		
		post["Titel"] = texttitle
		post["Ersteller"] = cherrypy.session["Benutzername"];
		post["Bearbeiter"] = 0;
		post["Text"] = text;
		post["Erstellt"] = time.asctime()
		post["Bearbeitet"] = 0;

		discussioncontent["Beitraege"].append(post)

	def deleteBeitrag(self,thema,discussionname,beitragID):

		pass
	#def editBeitrag(self,thema,discussionname,beitragID):
	# glaub editDiskussion sollte reichen
		#pass
			

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