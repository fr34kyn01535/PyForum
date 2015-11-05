# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446731794.3611386
_enable_loop = True
_template_filename = 'templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,title,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(title=title,pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\t<form action="/login" id="login" method="POST">\r\n        <input type="text" name="username" placeholder="Benutzername" required="required" />\r\n        <input type="text" name="password" placeholder="Passwort" required="required"/>\r\n        <button type="submit">Einloggen</button>\r\n    </form>\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "login.html", "filename": "templates/login.html", "line_map": {"16": 1, "21": 1, "22": 2, "23": 2, "24": 8, "30": 24}}
__M_END_METADATA
"""
