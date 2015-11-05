# coding: utf-8
import cherrypy
from app import datenbank
from mako.template import Template
from mako.runtime import Context
from mako.lookup import TemplateLookup

def RenderTemplate(file, **kwargs):
	templates = TemplateLookup(directories=["./templates/"], module_directory="./modules/", default_filters=['decode.utf8'], input_encoding='utf-8', output_encoding='utf-8')
	template = templates.get_template(file)
	role = "Jedermann";
	if hasattr(cherrypy,"session") and 'Benutzername' in cherrypy.session:
		userstatus="<li><a href=\"/logout\">"+cherrypy.session['Benutzername']+" ["+cherrypy.session['Rolle']+"]</a>"
		role = cherrypy.session['Rolle']
	else:
		userstatus="<li><a href=\"/login\">Einloggen</a></li>"
	return template.render_unicode(userstatus=userstatus,role=role,**kwargs).encode('utf-8', 'replace')
	
# EOF