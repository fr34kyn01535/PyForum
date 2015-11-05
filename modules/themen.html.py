# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446718610.7696025
_enable_loop = True
_template_filename = 'templates/themen.html'
_template_uri = 'themen.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        themen = context.get('themen', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n')
        for thema in themen:
            __M_writer('    ')
            __M_writer(str(thema))
            __M_writer(' | \r\n')
        __M_writer('\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "themen.html", "source_encoding": "ascii", "filename": "templates/themen.html", "line_map": {"16": 0, "36": 30, "23": 1, "24": 1, "25": 3, "26": 4, "27": 4, "28": 4, "29": 6, "30": 7}}
__M_END_METADATA
"""
