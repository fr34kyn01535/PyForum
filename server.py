# coding:utf-8

import os.path
import cherrypy

from app import themen,login,logout

def main():
	try:                                  
		currentDir_s = os.path.dirname(os.path.abspath(__file__))
	except:
		currentDir_s = os.path.dirname(os.path.abspath(sys.executable))
	  
	cherrypy.Application.currentDir_s = currentDir_s
   
	cherrypy.config.update({
		'server.socket_host': '127.0.0.1', 
		'server.socket_port': 80, 
	}) 
   
	cherrypy.engine.autoreload.unsubscribe()
	cherrypy.engine.timeout_monitor.unsubscribe()
	
	config = {'/': {'tools.sessions.on': True, 'request.dispatch': cherrypy.dispatch.MethodDispatcher()}};
	
	cherrypy.tree.mount(themen.Request(), '/', config)
	cherrypy.tree.mount(login.Request(), '/login', config)
	cherrypy.tree.mount(logout.Request(), '/logout', config)

	cherrypy.engine.start()
	cherrypy.engine.block() 

if __name__ == '__main__':
	main()