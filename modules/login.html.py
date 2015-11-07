# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446931755.7956815
_enable_loop = True
_template_filename = 'templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(title=title,pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n<form class="form-horizontal" action="/login" id="login" method="POST">\r\n\t<fieldset>\r\n        <legend>Login</legend>\r\n        <div class="form-group">\r\n            <label for="inputUsername" class="col-lg-2 control-label">Benutzername</label>\r\n            <div class="col-lg-10">\r\n                <input type="text" class="form-control" required="required" id="username" name="username" placeholder="Benutzername"><br/>\r\n            </div>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="inputPassword" class="col-lg-2 control-label">Passwort</label>\r\n            <div class="col-lg-10">\r\n                <input type="password" class="form-control" required="required" id="password" name="password" placeholder="Passwort">\r\n            </div>\r\n        </div>\r\n        <div class="form-group">\r\n            <div class="col-lg-10 col-lg-offset-2">\r\n                <button type="submit" class="btn btn-primary">Einloggen</button>\r\n            </div>\r\n        </div>\r\n    </fieldset>\r\n</form>\r\n\t\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 2, "21": 2, "22": 3, "23": 3, "24": 27, "25": 27, "31": 25}, "source_encoding": "utf-8", "filename": "templates/login.html", "uri": "login.html"}
__M_END_METADATA
"""
