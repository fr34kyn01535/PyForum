# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446748161.6988945
_enable_loop = True
_template_filename = 'templates/diskussionen.html'
_template_uri = 'diskussionen.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(title=title,thema=thema,pageargs=pageargs)
        diskussionen = context.get('diskussionen', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li>\r\n    <li class="active">')
        __M_writer(str(thema))
        __M_writer('</li>\r\n    \r\n</ul>\r\n\r\n\r\n<div class="panel panel-default">\r\n    <div class="panel-heading">Diskussionen</div>\r\n    <div class="panel-body">\r\n       \r\n\t   \r\n\t   <div class="list-group">\r\n')
        for diskussion in diskussionen:
            __M_writer('    \r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<div class="row-action-primary">\r\n\t\t\t\t\t<i class="mdi-file-folder"></i>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="row-content">\r\n\t\t\t\t\t<div class="least-content"></div>\r\n\t\t\t\t\t<h4 class="list-group-item-heading">')
            __M_writer(str(diskussion))
            __M_writer('</h4>\r\n\t\t\t\t\t<p class="list-group-item-text"></p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<div class="list-group-separator"></div>\r\n\t\t\t\r\n')
        __M_writer('</div>\r\n\t   \r\n\t   \r\n\t   \r\n    </div>\r\n</div>\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/diskussionen.html", "uri": "diskussionen.html", "source_encoding": "utf-8", "line_map": {"32": 40, "38": 32, "16": 2, "22": 2, "23": 3, "24": 3, "25": 7, "26": 7, "27": 18, "28": 19, "29": 26, "30": 26, "31": 33}}
__M_END_METADATA
"""
