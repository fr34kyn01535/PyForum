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
		userstatus="<li><a href=\"/logout\">"+cherrypy.session['Benutzername']+"</a>"
	else:
		userstatus="<li><a href=\"/login\">Einloggen</a></li>"
	return template.render_unicode(userstatus=userstatus,**kwargs).encode('utf-8', 'replace')
	
# EOF