# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446750552.8551326
_enable_loop = True
_template_filename = 'templates/administration.html'
_template_uri = 'administration.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,benutzer,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(benutzer=benutzer,title=title,pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n\t<li><a href="/">Startseite</a></li>\r\n    <li class="active">Administration</li>\r\n</ul>\r\n\r\n<br/>\r\n\r\n\r\n\r\n<div class="panel panel-default">\r\n    <div class="panel-heading">Benutzer</div>\r\n    <div class="panel-body">\r\n       \r\n\t\t<table class="table table-striped table-hover ">\r\n\t\t\t<thead>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>Benutzername</th>\r\n\t\t\t\t\t<th>Passwort</th>\r\n\t\t\t\t\t<th>Gruppe</th>\r\n\t\t\t\t\t<th style="width: 290px;"></th>\r\n\t\t\t\t</tr>\r\n\t\t\t</thead>\r\n\t\t\t<tbody>\r\n')
        for nutzer in benutzer:
            __M_writer('\t\t\t\t\t<form method="POST" action="/administration">\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<input type="hidden" name="originalusername" value="')
            __M_writer(filters.decode.utf8(nutzer["Benutzername"]))
            __M_writer('"/>\r\n\t\t\t\t\t\t\t<td><input class="form-control" type="text" name="username" value="')
            __M_writer(filters.decode.utf8(nutzer["Benutzername"]))
            __M_writer('"/></td>\r\n\t\t\t\t\t\t\t<td><input class="form-control" type="password" name="password" value="NO CHANGE"/></td>\r\n\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t<select class="form-control" name="role">\r\n\t\t\t\t\t\t\t\t\t<option \r\n')
            if nutzer["Rolle"]=="Administrator": 
                __M_writer('\t\t\t\t\t\t\t\t\t\tselected="selected"\r\n')
            __M_writer('\t\t\t\t\t\t\t\t\t>Administrator</option>\r\n\t\t\t\t\t\t\t\t\t<option\r\n')
            if nutzer["Rolle"]=="Bearbeiter": 
                __M_writer('\t\t\t\t\t\t\t\t\t\tselected="selected"\r\n')
            __M_writer('\t\t\t\t\t\t\t\t\t>Bearbeiter</option>\r\n\t\t\t\t\t\t\t\t\t<option \r\n')
            if nutzer["Rolle"]=="Jedermann": 
                __M_writer('\t\t\t\t\t\t\t\t\t\tselected="selected"\r\n')
            __M_writer('\t\t\t\t\t\t\t\t\t>Jedermann</option>\r\n\t\t\t\t\t\t\t\t</select>\r\n\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t<td><button name="action" value="save" class="btn btn-primary">Speichern</button>\r\n\t\t\t\t\t\t\t<button name="action" value="delete" class="btn btn-warning">Löschen</button></td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t</form>\r\n')
        __M_writer('\t\t\t</tbody>\r\n\t\t</table>\r\n\t\t\t   \r\n    </div>\r\n</div>\r\n\r\n<form style="float:right;" method="POST" action="/administration">\r\n\t<button name="action" value="add" class="btn btn-raised btn-material-green"><i class="mdi-content-add"></i></button>\r\n</form>\r\n<div style="clear:both;"></div>\r\n<br>\r\n\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/administration.html", "line_map": {"16": 2, "21": 2, "22": 3, "23": 3, "24": 28, "25": 29, "26": 31, "27": 31, "28": 32, "29": 32, "30": 37, "31": 38, "32": 40, "33": 42, "34": 43, "35": 45, "36": 47, "37": 48, "38": 50, "39": 58, "40": 71, "46": 40}, "uri": "administration.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
