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
		outputsorted = []
		
		for discussion in discussions:			
			current = dict()
			
			with open("./data/themen/"+ thema +"/" + discussion) as discussionfile:
				discussionfilecontent = json.load(discussionfile)
			current["Titel"] = discussionfilecontent["Titel"]
			current["Ersteller"] = discussionfilecontent["Ersteller"]
			current["Bearbeiter"] = discussionfilecontent["Bearbeiter"]
			current["Text"] = discussionfilecontent["Text"]
			current["Erstellt"] = discussionfilecontent["Erstellt"]
			current["Bearbeitet"] = discussionfilecontent["Bearbeitet"]
			current["Beitraege"] = discussionfilecontent["Beitraege"]
			current["Status"] = discussionfilecontent["Status"]
			current["BeitragID"] = discussionfilecontent["BeitragID"]
			output.append(current)
		outputsorted = sorted(output, key=itemgetter('Erstellt'), reverse=True) 
		return outputsorted
		
	def createDiskussion(self,thema,discussionname,text):
		
		discussion = dict()
		discussion["Ersteller"] = cherrypy.session["Benutzername"]
		discussion["Titel"] = discussionname
		discussion["Bearbeiter"] = " "
		discussion["Text"] = text
		discussion["Erstellt"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		discussion["Bearbeitet"] = " "
		discussion["Beitraege"] = [ ]
		discussion["Status"] = " "
		discussion["BeitragID"] = str(uuid.uuid4())

		outdiscussionfile = "./data/themen/" + thema +"/" + discussionname + ".json"
		with open(outdiscussionfile, 'w') as outdiscussion:
			json.dump(discussion, outdiscussion,indent=4)
	
	def deleteDiskussion(self, thema, discussionname):
		discussion = "./data/themen/"+ thema +"/" + discussionname + ".json"

		with open("./data/themen/"+ thema +"/" + discussionname + ".json") as discussionfile:
			discussionfilecontent = json.load(discussionfile)
		discussionfilecontent["Titel"]  = discussionname + " [gelöscht!]"		
		discussionfilecontent["Bearbeiter"] = cherrypy.session["Benutzername"]
		discussionfilecontent["Bearbeitet"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		discussionfilecontent["Status"] = "gelöscht"

		
		outdiscussionfile = "./data/themen/" + thema +"/" + discussionfilecontent["Titel"] + ".json"
		with open(outdiscussionfile, 'w') as outdiscussion:
			json.dump(discussionfilecontent, outdiscussion,indent=4)
		
		os.remove(discussion)

		

	def edit(self, thema,discussionname,beitragID,newtitle,newtext):
		#
		discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		

		with open(discussionfile, 'r') as currentfile:
			discussionfilecontent = json.load(currentfile)

		for key in discussionfilecontent:
			if discussionfilecontent["BeitragID"] == beitragID:
				discussionfilecontent["Titel"] = newtitle
				discussionfilecontent["Text"]  = newtext
				discussionfilecontent["Bearbeiter"] = cherrypy.session["Benutzername"]
				discussionfilecontent["Bearbeitet"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
				
		outfile = "./data/themen/" + thema +"/" + newtitle + ".json";
		with open(outfile, 'w') as out:
			json.dump(discussionfilecontent, out,indent=4)

		if os.path.isfile(discussionfile):
			os.remove(discussionfile)
			pass
		

	def getBeitraege(self,thema,discussionname):
		discussion = "./data/themen/" + thema +"/" + discussionname + ".json";
		output = []
		outputsorted = []
		current = dict()
		with open(discussion, "r") as discussionfile:
			discussionfilecontent = json.load(discussionfile)

	#erste Beitrag(=diskussion) gesondert
		current["Titel"] = discussionfilecontent["Titel"];
		current["Ersteller"] = discussionfilecontent["Ersteller"]
		current["Bearbeiter"] = discussionfilecontent["Bearbeiter"]
		current["Text"] = discussionfilecontent["Text"]
		current["Erstellt"] = discussionfilecontent["Erstellt"]
		current["Bearbeitet"] = discussionfilecontent["Bearbeitet"]
		current["BeitragID"] = discussionfilecontent["BeitragID"]
		output.append(current)


	#restlichen beiträge
		if discussionfilecontent["Beitraege"] != " ":
			for posts in discussionfilecontent["Beitraege"]:
				current = dict()
				current["Titel"] = posts["Titel"];
				current["Ersteller"] = posts["Ersteller"]
				current["Bearbeiter"] = posts["Bearbeiter"]
				current["Text"] = posts["Text"]
				current["Erstellt"] = posts["Erstellt"]
				current["Bearbeitet"] = posts["Bearbeitet"]
				current["BeitragID"] = posts["BeitragID"]
				output.append(current)
		
		outputsorted = sorted(output, key=itemgetter('Erstellt')) 
		return outputsorted
		

	def createBeitrag(self,thema,discussionname,title,text):
		discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		post = dict()
		with open(discussionfile) as discussionfilecontent:
			discussioncontent = json.load(discussionfilecontent)
		
		post["Titel"] = title
		post["Ersteller"] = cherrypy.session["Benutzername"];
		post["Bearbeiter"] = " ";
		post["Text"] = text;
		post["Erstellt"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime());
		post["Bearbeitet"] = " ";
		post["BeitragID"] = str(uuid.uuid4())

		discussioncontent["Beitraege"].append(post.copy())

		with open(discussionfile, 'w') as discussionfilecontent:
			json.dumps(discussioncontent,discussionfilecontent)

	def deleteBeitrag(self,thema,discussionname,beitragID):
		discussionfile = "./data/themen/" + thema +"/" + discussionname + ".json";
		with open(discussionfile, "r") as discussion:
			discussionfilecontent = json.load(discussion)

		if discussionfilecontent["BeitragID"] == beitragID:
			discussionfilecontent["Titel"] = "!"
			discussionfilecontent["Bearbeiter"] = cherrypy.session["Benutzername"]
			discussionfilecontent["Text"] = "Dieser Beitrag wurde vom Admin gelöscht"
			discussionfilecontent["Bearbeitet"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		else:
			for posts in discussionfilecontent["Beitraege"]:
				if post["BeitragID"] == beitragID:
					posts["Titel"] = "!"
					posts["Bearbeiter"] = cherrypy.session["Benutzername"]
					posts["Text"] = "Dieser Beitrag wurde vom Admin gelöscht"
					posts["Bearbeitet"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())	

		with open(discussionfile, 'w') as discussion:
			json.dumps(discussionfilecontent, discussion)
		
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