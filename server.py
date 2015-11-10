# coding:utf-8

import os.path
import cherrypy
import sys

if sys.version[0] == '2':
	reload(sys)
	sys.setdefaultencoding("utf-8")

from app import themen,diskussionen,beitraege,login,logout,administration,templates



def error_page(status, message, traceback, version):
    return templates.RenderTemplate("error.html",title="Error",status=status,message=message,traceback=traceback,version=version);
cherrypy.config.update({'error_page.default': error_page})
cherrypy.config.update({'error_page.401': error_page})
cherrypy.config.update({'error_page.402': error_page})
cherrypy.config.update({'error_page.403': error_page})
cherrypy.config.update({'error_page.404': error_page})
cherrypy.config.update({'error_page.500': error_page})

def main():
	cherrypy.Application.currentDir_s = os.path.dirname(os.path.abspath(__file__))
   
	cherrypy.config.update({
		'server.socket_host': '0.0.0.0', 
		'server.socket_port': 8082, 
	}) 
   
	cherrypy.engine.autoreload.unsubscribe()
	cherrypy.engine.timeout_monitor.unsubscribe()
	
	dynamic = {'/': {
		'tools.sessions.on': True, 
		'request.dispatch': cherrypy.dispatch.MethodDispatcher()
	}};
	
	
	cherrypy.tree.mount(themen.Request(), '/', dynamic)
	cherrypy.tree.mount(diskussionen.Request(), '/diskussionen', dynamic)
	cherrypy.tree.mount(beitraege.Request(), '/beitraege', dynamic)
	cherrypy.tree.mount(login.Request(), '/login', dynamic)
	cherrypy.tree.mount(logout.Request(), '/logout', dynamic)
	cherrypy.tree.mount(administration.Request(), '/administration', dynamic)
	
	cherrypy.tree.mount(None, '/js', {'/': {  
		'tools.gzip.on'       : True,
		'tools.staticdir.on'  : True,
		'tools.staticdir.dir' : os.path.join(cherrypy.Application.currentDir_s, 'js'),
		'tools.expires.on'    : True,
		'tools.expires.secs'  : 0
	}})
	
	cherrypy.tree.mount(None, '/css', {'/': {  
		'tools.gzip.on'       : True,
		'tools.staticdir.on'  : True,
		'tools.staticdir.dir' : os.path.join(cherrypy.Application.currentDir_s, 'css'),
		'tools.expires.on'    : True,
		'tools.expires.secs'  : 0
	}})
	
	cherrypy.tree.mount(None, '/fonts', {'/': {  
		'tools.gzip.on'       : True,
		'tools.staticdir.on'  : True,
		'tools.staticdir.dir' : os.path.join(cherrypy.Application.currentDir_s, 'fonts'),
		'tools.expires.on'    : True,
		'tools.expires.secs'  : 0
	}})

	cherrypy.engine.start()
	cherrypy.engine.block() 

if __name__ == '__main__':
	main()
