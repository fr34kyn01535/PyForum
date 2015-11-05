# coding:utf-8

import os.path
import cherrypy

from app import themen,login,logout

def main():
	cherrypy.Application.currentDir_s = os.path.dirname(os.path.abspath(__file__))
   
	cherrypy.config.update({
		'server.socket_host': '127.0.0.1', 
		'server.socket_port': 80, 
	}) 
   
	cherrypy.engine.autoreload.unsubscribe()
	cherrypy.engine.timeout_monitor.unsubscribe()
	
	dynamic = {'/': {
		'tools.sessions.on': True, 
		'request.dispatch': cherrypy.dispatch.MethodDispatcher()
	}};
	
	static = {'/': {  
		'tools.gzip.on'       : True,
		'tools.staticdir.on'  : True,
		'tools.staticdir.dir' : os.path.join(cherrypy.Application.currentDir_s, 'static'),
		'tools.expires.on'    : True,
		'tools.expires.secs'  : 0
	}};
	
	cherrypy.tree.mount(themen.Request(), '/', dynamic)
	cherrypy.tree.mount(login.Request(), '/login', dynamic)
	cherrypy.tree.mount(logout.Request(), '/logout', dynamic)
	cherrypy.tree.mount(None, '/static', static)

	cherrypy.engine.start()
	cherrypy.engine.block() 

if __name__ == '__main__':
	main()