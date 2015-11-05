# coding: utf-8
import cherrypy
from app import datenbank
from mako.template import Template
from mako.runtime import Context
from mako.lookup import TemplateLookup

def RenderTemplate(file, **kwargs):
	templates = TemplateLookup(directories=["./templates/"], module_directory="./modules/")
	template = templates.get_template(file)
	
	if 'Benutzername' in cherrypy.session:
		userstatus="Eingeloggt als: "+cherrypy.session['Benutzername']+" ["+cherrypy.session['Rolle']+"] (<a href=\"/logout\">Ausloggen</a>)"
	else:
		userstatus="Nicht eingeloggt. (<a href=\"/login\">Einloggen</a>)"
	return template.render(**kwargs,userstatus=userstatus)
	
# EOF