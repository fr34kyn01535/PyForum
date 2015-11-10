# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1447144831.7188432
_enable_loop = True
_template_filename = 'templates/header.html'
_template_uri = 'header.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,title=title)
        role = context.get('role', UNDEFINED)
        username = context.get('username', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>')
        __M_writer('\r\n<html>\r\n   <head>\r\n      <title>PyForum | ')
        __M_writer(filters.decode.utf8(title))
        __M_writer('</title>\r\n      <meta charset="UTF-8" />    \r\n        <link href="/css/bootstrap.min.css" rel="stylesheet">\r\n        <link href="/css/roboto.min.css" rel="stylesheet">\r\n        <link href="/css/material-fullpalette.min.css" rel="stylesheet">\r\n        <link href="/css/ripples.min.css" rel="stylesheet">\r\n\t\t\r\n\t\t<script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>\r\n\t\t<script type="text/javascript" src="/js/bootstrap.min.js"></script>\r\n\t\t<script type="text/javascript" src="/js/material.min.js"></script>\r\n\t\t<script type="text/javascript" src="/js/ripples.min.js"></script>\r\n\t\t\r\n\t\t<link href="/css/custom.css" rel="stylesheet" />\r\n\t\t\r\n\t\t<script type="text/javascript">\r\n\t\t\t$(function(){\r\n\t\t\t\t$.material.init();\r\n\t\t\t});\r\n\t\t</script>\r\n\t\t\r\n   </head>\r\n   <body>\r\n      <nav id="navigation">\r\n\t  \r\n\t  <div class="navbar navbar-default">\r\n  <div class="navbar-header">\r\n    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-responsive-collapse">\r\n      <span class="icon-bar"></span>\r\n      <span class="icon-bar"></span>\r\n      <span class="icon-bar"></span>\r\n    </button>\r\n    <a class="navbar-brand" href="/">PyForum</a>\r\n  </div>\r\n  <div class="navbar-collapse collapse navbar-responsive-collapse">\r\n    <ul class="nav navbar-nav">\r\n\t\t<li><a href="/">Startseite</a></li>\r\n')
        if role=="Administrator": 
            __M_writer('\t\t\t<li><a href="/administration">Administration</a></li>\r\n')
        __M_writer('    </ul>\r\n\t<ul class="nav navbar-nav navbar-right">\r\n           \r\n')
        if username=="Gast" :	
            __M_writer('\t\t\t\t<li><a style="padding:16px !important;" href="/login" title="Einloggen"><i class="mdi-action-lock-open"></i></a></li>\r\n')
        else: 
            __M_writer('\t\t\t\t<li title="')
            __M_writer(filters.decode.utf8(role))
            __M_writer('"><a href="#">')
            __M_writer(filters.decode.utf8(username))
            __M_writer('</a></li><li><a style="padding:16px !important;" href="/logout" title="Ausloggen"><i class="mdi-action-lock-outline"></i></a></li>\r\n')
        __M_writer('\t\t\t\r\n\t\t\t\r\n\t\t\t\r\n\t\t\r\n\t\t\r\n        </ul>\r\n  </div>\r\n</div>\r\n      </nav>\r\n\t\r\n\t  \r\n      <section id="main">')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/header.html", "uri": "header.html", "source_encoding": "utf-8", "line_map": {"32": 49, "33": 50, "34": 50, "35": 50, "36": 50, "37": 50, "38": 52, "44": 38, "16": 2, "23": 2, "24": 2, "25": 5, "26": 5, "27": 41, "28": 42, "29": 44, "30": 47, "31": 48}}
__M_END_METADATA
"""
