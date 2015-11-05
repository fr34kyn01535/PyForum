# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446718586.0419335
_enable_loop = True
_template_filename = 'templates/footer.html'
_template_uri = 'footer.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('       </section>\r\n   </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "templates/footer.html", "uri": "footer.html", "line_map": {"16": 0, "27": 21, "21": 1}}
__M_END_METADATA
"""
