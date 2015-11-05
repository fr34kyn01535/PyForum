# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446718586.038915
_enable_loop = True
_template_filename = 'templates/header.html'
_template_uri = 'header.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,title,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(title=title,pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n   <head>\r\n      <title>WEB | Forum | ')
        __M_writer(str(title))
        __M_writer('</title>\r\n      <meta charset="UTF-8" />\r\n\t  <link rel="stylesheet" type="text/css" href="/css/main.css" />\r\n      <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>\r\n   </head>\r\n   <body>\r\n      <nav id="navigation">\r\n\t  \r\n      </nav>\r\n\t  \r\n      <section id="main">')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "templates/header.html", "uri": "header.html", "line_map": {"16": 1, "29": 23, "21": 1, "22": 5, "23": 5}}
__M_END_METADATA
"""
