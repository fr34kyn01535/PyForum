# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446736613.7590773
_enable_loop = True
_template_filename = 'templates/themen.html'
_template_uri = 'themen.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,themen,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(themen=themen,pageargs=pageargs,title=title)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li class="active"><a href="/">Startseite</a></li>\r\n</ul>\r\n\r\n<br/>\r\n\r\n<div class="jumbotron">\r\n    <h1>Dies ist PyForum</h1>\r\n    <p>Ein quelloffenes Forum welches für die Praktika WEB BI3 erstellt wurde. Es ist in Python geschrieben und mit CherryPy gehostet.</p>\r\n    <p><a href="https://github.com/fr34kyn01535/PyForum" class="btn btn-primary btn-lg">Zum Quelltext</a></p>\r\n</div>\r\n\r\n<br/>\r\n\r\n<div class="panel panel-default">\r\n    <div class="panel-heading">Themen</div>\r\n    <div class="panel-body">\r\n       \r\n\t   \r\n\t   <div class="list-group">\r\n')
        for thema in themen:
            __M_writer('    \r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<div class="row-action-primary">\r\n\t\t\t\t\t<i class="mdi-file-folder"></i>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="row-content">\r\n\t\t\t\t\t<div class="least-content"></div>\r\n\t\t\t\t\t<h4 class="list-group-item-heading">')
            __M_writer(str(thema))
            __M_writer('</h4>\r\n\t\t\t\t\t<p class="list-group-item-text"></p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<div class="list-group-separator"></div>\r\n\t\t\t\r\n')
        __M_writer('</div>\r\n\t   \r\n\t   \r\n\t   \r\n    </div>\r\n</div>\r\n\r\n\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "themen.html", "filename": "templates/themen.html", "line_map": {"16": 2, "35": 29, "21": 2, "22": 3, "23": 3, "24": 25, "25": 26, "26": 33, "27": 33, "28": 40, "29": 49}}
__M_END_METADATA
"""
