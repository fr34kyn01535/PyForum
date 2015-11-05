# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446735170.0163949
_enable_loop = True
_template_filename = 'templates/header.html'
_template_uri = 'header.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,title=title)
        userstatus = context.get('userstatus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>')
        __M_writer('\r\n<html>\r\n   <head>\r\n      <title>PyForum | ')
        __M_writer(str(title))
        __M_writer('</title>\r\n      <meta charset="UTF-8" />    \r\n        <link href="/css/bootstrap.min.css" rel="stylesheet">\r\n        <link href="/css/roboto.min.css" rel="stylesheet">\r\n        <link href="/css/material-fullpalette.min.css" rel="stylesheet">\r\n        <link href="/css/ripples.min.css" rel="stylesheet">\r\n\t\t\r\n\t\t<script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>\r\n\t\t<script type="text/javascript" src="/js/bootstrap.min.js"></script>\r\n\t\t<script type="text/javascript" src="/js/material.min.js"></script>\r\n\t\t<script type="text/javascript" src="/js/ripples.min.js"></script>\r\n\t\t\r\n\t\t<link href="/css/custom.css" rel="stylesheet" />\r\n\t\t\r\n\t\t<script type="text/javascript">\r\n\t\t\t$(function(){\r\n\t\t\t\t$.material.init();\r\n\t\t\t});\r\n\t\t</script>\r\n\t\t\r\n   </head>\r\n   <body>\r\n      <nav id="navigation">\r\n\t  \r\n\t  <div class="navbar navbar-default">\r\n  <div class="navbar-header">\r\n    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-responsive-collapse">\r\n      <span class="icon-bar"></span>\r\n      <span class="icon-bar"></span>\r\n      <span class="icon-bar"></span>\r\n    </button>\r\n    <a class="navbar-brand" href="javascript:void(0)">PyForum</a>\r\n  </div>\r\n  <div class="navbar-collapse collapse navbar-responsive-collapse">\r\n    <ul class="nav navbar-nav">\r\n\t\t<li><a href="/">Startseite</a></li>\r\n\t\t<li><a href="#">Impressum</a></li>\r\n\t\t<li><a href="#">Über Uns</a></li>\r\n    </ul>\r\n\t<ul class="nav navbar-nav navbar-right">\r\n            ')
        __M_writer(str(userstatus))
        __M_writer('\r\n        </ul>\r\n  </div>\r\n</div>\r\n      </nav>\r\n\t\r\n\t  \r\n      <section id="main">')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "header.html", "filename": "templates/header.html", "line_map": {"16": 2, "33": 27, "22": 2, "23": 2, "24": 5, "25": 5, "26": 45, "27": 45}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
