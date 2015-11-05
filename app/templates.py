# coding: utf-8
import cherrypy
from app import datenbank,templates
from mako.template import Template
from mako.runtime import Context
from mako.lookup import TemplateLookup

def RenderTemplate(file, **kwargs):
	templates = TemplateLookup(directories=["./templates/"], module_directory="./modules/")
	template = templates.get_template(file)
	return template.render(**kwargs)
	
# EOF