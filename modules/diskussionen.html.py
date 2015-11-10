# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1447152539.9181325
_enable_loop = True
_template_filename = 'templates/diskussionen.html'
_template_uri = 'diskussionen.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,thema=thema,title=title)
        diskussionen = context.get('diskussionen', UNDEFINED)
        role = context.get('role', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li> \t\r\n    <li class="active">')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('</li>   \r\n</ul>\r\n<br/>\r\n\r\n<div id="hiddenDiv" style="display: none">\r\n\t<form method="POST" action="/diskussionen">\r\n\t<ul class="wmfg_questions">\r\n\t\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\t\t<li class="wmfg_q">\r\n\t\t\t<input type="text" class="form-control floating-label" required="required" placeholder="Titel" name="title">\r\n\t\t</li>\r\n\t\t<li class="wmfg_q">\r\n\t\t\t\r\n\t\t\t<textarea input type="text" class="form-control floating-label" required="required" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\t\t</li>\r\n\t\t<li class="wmfg_q">\r\n\t\t\t<button type="submit" name="action" value="create" class="btn btn-primary btn-material-green btn-sm">Erstellen</button>\r\n\t\t</li>\r\n\t</ul>\r\n</form>\r\n</div>\r\n\r\n')
        if role=="Administrator" or role=="Bearbeiter": 	 	
            __M_writer('<button style="float:right;" class="btn btn-raised btn-material-green toggleButton" data-toggle="hiddenDiv"><i class="mdi-content-add"></i></button>\r\n\r\n\r\n')
        __M_writer('\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n<div class="panel panel-default">\r\n    <div class="panel-heading">Diskussionen</div>\r\n    <div class="panel-body">\r\n       \r\n\t   <div class="list-group">\r\n')
        for diskussion in diskussionen:
            __M_writer(' \r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<div class="row-action-primary">\r\n\t\t\t\t\t<i class="mdi-file-folder"></i>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="row-content">\r\n\t\t\t\t\t<div class="least-content"></div>\r\n\r\n')
            if diskussion["Status"] == "deleted":
                __M_writer('\t\t\t\t\t\t<h4 class="list-group-item-heading">')
                __M_writer(filters.decode.utf8(diskussion["Titel"]))
                __M_writer(' [Gelöscht]</a>\r\n')
            else:
                __M_writer('\t\t\t\t\t\t<h4 class="list-group-item-heading"><a href="/beitraege?thema=')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('&id=')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('">')
                __M_writer(filters.decode.utf8(diskussion["Titel"]))
                __M_writer('</a>\r\n')
            __M_writer('\t\t\t\t\t\r\n')
            if role=="Administrator": 
                __M_writer('\t\t\t\t\t\t<form method="POST" action="/diskussionen">\r\n\t\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t\t<input type="hidden" name="id" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t\t\t\t</form>\r\n')
            __M_writer('\r\n\t\t\t\t\t</h4>\t\t\t\t\t\r\n\t\t\t\t\t<br/>\r\n\r\n\t\t\t\t\t<p class="list-group-item-text">von ')
            __M_writer(filters.decode.utf8(diskussion["Ersteller"]))
            __M_writer(' (')
            __M_writer(filters.decode.utf8(diskussion["Erstellt"]))
            __M_writer(')</p>\r\n\r\n')
            if diskussion["Bearbeiter"] != " ": 
                __M_writer('\t\t\t\t\t\t<p class="list-group-item-text">zuletzt bearbeitet von ')
                __M_writer(filters.decode.utf8(diskussion["Bearbeiter"]))
                __M_writer(' (')
                __M_writer(filters.decode.utf8(diskussion["Bearbeitet"]))
                __M_writer(')</p>\r\n')
            __M_writer('\r\n\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t\r\n\t\t\t<div class="list-group-separator"></div>\r\n\t\t\t\r\n')
        __M_writer('</div>\r\n\t   \r\n \r\n\t   \r\n    </div>\r\n</div> \r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/diskussionen.html", "uri": "diskussionen.html", "line_map": {"16": 2, "23": 2, "24": 3, "25": 3, "26": 7, "27": 7, "28": 14, "29": 14, "30": 29, "31": 30, "32": 34, "33": 44, "34": 45, "35": 53, "36": 54, "37": 54, "38": 54, "39": 55, "40": 56, "41": 56, "42": 56, "43": 56, "44": 56, "45": 56, "46": 56, "47": 58, "48": 59, "49": 60, "50": 61, "51": 61, "52": 62, "53": 62, "54": 66, "55": 70, "56": 70, "57": 70, "58": 70, "59": 72, "60": 73, "61": 73, "62": 73, "63": 73, "64": 73, "65": 75, "66": 83, "67": 90, "68": 90, "74": 68}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
