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
	username = "Gast";
	if hasattr(cherrypy,"session") and 'Benutzername' in cherrypy.session:
		role = cherrypy.session['Rolle']
		username = cherrypy.session['Benutzername']
	return template.render_unicode(username=username,role=role,**kwargs).encode('utf-8', 'replace')
# EOF