# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446746165.5041482
_enable_loop = True
_template_filename = 'templates/error.html'
_template_uri = 'error.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        message = context.get('message', UNDEFINED)
        status = context.get('status', UNDEFINED)
        title = context.get('title', UNDEFINED)
        traceback = context.get('traceback', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title+' '+status)
        __M_writer('\r\n\r\n<div class="jumbotron">\r\n    <h1>')
        __M_writer(filters.decode.utf8(status))
        __M_writer('</h1>\r\n    <p>')
        __M_writer(filters.decode.utf8(message))
        __M_writer('</p>\r\n    <pre>')
        __M_writer(filters.decode.utf8(traceback))
        __M_writer('</pre>\r\n    <p><a href="/" class="btn btn-primary btn-lg">Zur Startseite</a></p>\r\n</div>\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "error.html", "source_encoding": "utf-8", "filename": "templates/error.html", "line_map": {"32": 8, "33": 8, "34": 12, "40": 34, "16": 2, "25": 2, "26": 3, "27": 3, "28": 6, "29": 6, "30": 7, "31": 7}}
__M_END_METADATA
"""
