# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446729264.7283456
_enable_loop = True
_template_filename = 'templates/themen.html'
_template_uri = 'themen.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,title,themen,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,themen=themen,title=title)
        __M_writer = context.writer()
        __M_writer('\r\n')
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
{"source_encoding": "ascii", "filename": "templates/themen.html", "line_map": {"16": 1, "35": 29, "21": 1, "22": 2, "23": 2, "24": 4, "25": 5, "26": 5, "27": 5, "28": 7, "29": 8}, "uri": "themen.html"}
__M_END_METADATA
"""
