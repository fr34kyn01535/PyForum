# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446733159.7308502
_enable_loop = True
_template_filename = 'templates/header.html'
_template_uri = 'header.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,title,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,title=title)
        userstatus = context.get('userstatus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n   <head>\r\n      <title>WEB | Forum | ')
        __M_writer(str(title))
        __M_writer('</title>\r\n      <meta charset="UTF-8" />\r\n\t  <link href=\'https://fonts.googleapis.com/css?family=PT+Sans\' rel=\'stylesheet\' type=\'text/css\'>\r\n\t  <link rel="stylesheet" type="text/css" href="/css/main.css" />\r\n      <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>\r\n   </head>\r\n   <body>\r\n      <nav id="navigation">\r\n\t\t\r\n      </nav>\r\n\t  <section id="userbar">')
        __M_writer(str(userstatus))
        __M_writer('</section>\r\n\t  \r\n      <section id="main">')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 1, "32": 26, "22": 1, "23": 5, "24": 5, "25": 15, "26": 15}, "filename": "templates/header.html", "source_encoding": "ascii", "uri": "header.html"}
__M_END_METADATA
"""
