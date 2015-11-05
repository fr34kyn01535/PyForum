# coding: utf-8
import json
import os

class Datenbank(object):
	exposed = True 
	
	def __init__(self):
		pass
			
	def getThemen(self):
		return os.listdir("./data/themen/")   
	
	def getDiskussionen(self):
		return os.listdir("./data/diskussionen/")

	def check(self, param):
		if param is None:
			return "None"
		else:
			return str(param)
	
	def test(self):
		print("Testing database...")
		print("loginBenutzer(\"fr34kyn01535\",\"test\"): " + self.check(self.loginBenutzer("fr34kyn01535","test")));
		print("loginBenutzer(\"fr34kyn01535\",\"asdasd\"): " + self.check(self.loginBenutzer("fr34kyn01535","asdasd")));
		print("getBenutzer(\"fr34kyn01535\"): " + self.check(self.getBenutzer("fr34kyn01535")));
		print("deleteBenutzer(\"fr34kyn01535\"): " + self.check(self.getBenutzer("fr34kyn01535")));
		print("getBenutzer(\"fr34kyn01535\"): " + self.check(self.getBenutzer("fr34kyn01535")));
		print("editBenutzer(None,\"fr34kyn01535\",\"test\",\"Administrator\"): " + self.check(self.editBenutzer(None,"fr34kyn01535","test","Administrator")));
		print("getBenutzer(\"fr34kyn01535\"): " + self.check(self.getBenutzer("fr34kyn01535")));
		print("editBenutzer(\"fr34kyn01535\",\"fr34kyn01535Test\",\"bla\",\"Benutzer\"): " + self.check(self.editBenutzer("fr34kyn01535","fr34kyn01535Test","bla","Benutzer")));
		print("getBenutzer(\"fr34kyn01535\"): " + self.check(self.getBenutzer("fr34kyn01535")));
		print("getBenutzer(\"fr34kyn01535Test\"): " + self.check(self.getBenutzer("fr34kyn01535Test")));
		print("editBenutzer(\"fr34kyn01535Test\",\"fr34kyn01535\",\"test\",\"Administrator\"): " + self.check(self.editBenutzer("fr34kyn01535Test","fr34kyn01535","test","Administrator")));
		print("getBenutzer(\"fr34kyn01535\"): " + self.check(self.getBenutzer("fr34kyn01535")));
		print("getBenutzer(\"fr34kyn01535Test\"): " + self.check(self.getBenutzer("fr34kyn01535Test")));
	
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