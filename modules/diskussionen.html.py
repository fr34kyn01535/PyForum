# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446865588.6682403
_enable_loop = True
_template_filename = 'templates/diskussionen.html'
_template_uri = 'diskussionen.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(thema=thema,pageargs=pageargs,title=title)
        diskussionen = context.get('diskussionen', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li>\r\n    <li class="active">')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('</li>\r\n    \r\n</ul>\r\n<br/>\r\n\r\n<form method="POST" action="/thema">\r\n\r\n<ul class="wmfg_questions">\r\n\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t<input type="text" class="form-control floating-label" placeholder="Titel" name="discussionname">\r\n\t</li>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t\r\n\t\t<textarea input type="text" class="form-control floating-label" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\t</li>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t<button type="submit" name="action" value="create" class="btn btn-primary btn-material-green btn-sm">Erstellen</button>\r\n\r\n\t</li>\r\n\r\n</ul>\r\n\r\n</form>\r\n\t\r\n<button style="float:right;" class="btn btn-fab btn-raised btn-material-green btn-xs"><i class="mdi-content-add"></i></button>\r\n</form>\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n<div class="panel panel-default">\r\n    <div class="panel-heading">Diskussionen</div>\r\n    <div class="panel-body">\r\n       \r\n\t   <div class="list-group">\r\n')
        for diskussion in diskussionen:
            __M_writer('    \t\t\r\n\r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<div class="row-action-primary">\r\n\t\t\t\t\t<i class="mdi-file-folder"></i>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="row-content">\r\n\t\t\t\t\t<div class="least-content"></div>\r\n\t\t\t\t\t<h4 class="list-group-item-heading"><a href="/diskussion?thema=')
            __M_writer(filters.decode.utf8(thema))
            __M_writer('&discussionname=')
            __M_writer(filters.decode.utf8(diskussion))
            __M_writer('">')
            __M_writer(filters.decode.utf8(diskussion["Titel"]))
            __M_writer('</a>\r\n\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t\t\t<button style="float:right;" name="action" value="edit" class="btn btn-primary btn-xs"><i class="mdi-content-create"></i></button>\r\n\t\t\t\t\t</h4>\r\n\t\t\t\t\t\r\n\t\t\t\t\t\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\t<p class="list-group-item-text">von ')
            __M_writer(filters.decode.utf8(diskussion["Ersteller"]))
            __M_writer(' (')
            __M_writer(filters.decode.utf8(diskussion["Erstellt"]))
            __M_writer(')</p>\r\n\t\t\t\t\t\r\n\t\t\t\t\t<p class="list-group-item-text"></p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t\r\n\t\t\t<div class="list-group-separator"></div>\r\n\t\t\t\r\n')
        __M_writer('</div>\r\n\t   \r\n\t   \r\n\t   \r\n    </div>\r\n</div>\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 2, "22": 2, "23": 3, "24": 3, "25": 7, "26": 7, "27": 15, "28": 15, "29": 46, "30": 47, "31": 55, "32": 55, "33": 55, "34": 55, "35": 55, "36": 55, "37": 62, "38": 62, "39": 62, "40": 62, "41": 71, "42": 78, "43": 78, "49": 43}, "source_encoding": "utf-8", "uri": "diskussionen.html", "filename": "templates/diskussionen.html"}
__M_END_METADATA
"""
