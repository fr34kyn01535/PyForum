# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449333663.50059
_enable_loop = True
_template_filename = 'templates/footer.html'
_template_uri = 'footer.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n\t</section>\r\n\t\r\n\t<section id="footer">\r\n\t\t<div class="panel panel-default">\r\n\t\t\t<div class="panel-footer">© 2015 <a href="https://github.com/minolyx">Michael</a> und <a href="https://github.com/fr34kyn01535">Sven</a></div>\r\n\t\t</div>\r\n\t</section>\r\n\t\r\n   </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/footer.html", "line_map": {"16": 2, "27": 21, "21": 2}, "source_encoding": "utf-8", "uri": "footer.html"}
__M_END_METADATA
"""
