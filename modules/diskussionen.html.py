# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1447147118.9741087
_enable_loop = True
_template_filename = 'templates/diskussionen.html'
_template_uri = 'diskussionen.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,title=title,thema=thema)
        role = context.get('role', UNDEFINED)
        diskussionen = context.get('diskussionen', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li> \t\r\n    <li class="active">')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('</li>   \r\n</ul>\r\n<br/>\r\n\r\n<div id="HiddneDiv" style="DISPLAY: none">\r\n\t<form method="POST" action="/diskussionen">\r\n\t<ul class="wmfg_questions">\r\n\t\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\t\t<li class="wmfg_q">\r\n\t\t\t<input type="text" class="form-control floating-label" required="required" placeholder="Titel" name="title">\r\n\t\t</li>\r\n\t\t<li class="wmfg_q">\r\n\t\t\t\r\n\t\t\t<textarea input type="text" class="form-control floating-label" required="required" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\t\t</li>\r\n\t\t<li class="wmfg_q">\r\n\t\t\t<button type="submit" name="action" value="create" class="btn btn-primary btn-material-green btn-sm">Erstellen</button>\r\n\t\t</li>\r\n\t</ul>\r\n</form>\r\n</div>\r\n\r\n')
        if role=="Administrator" or role=="Bearbeiter": 	 	
            __M_writer('<button onclick="ShowHide()" style="float:right;" class="btn btn-raised btn-material-green"><i class="mdi-content-add"></i></button>\r\n')
        __M_writer('\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n<div class="panel panel-default">\r\n    <div class="panel-heading">Diskussionen</div>\r\n    <div class="panel-body">\r\n       \r\n\t   <div class="list-group">\r\n')
        for diskussion in diskussionen:
            __M_writer(' \r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<div class="row-action-primary">\r\n\t\t\t\t\t<i class="mdi-file-folder"></i>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="row-content">\r\n\t\t\t\t\t<div class="least-content"></div>\r\n\r\n')
            if diskussion["Status"] == "deleted":
                __M_writer('\t\t\t\t\t\t<h4 class="list-group-item-heading">')
                __M_writer(filters.decode.utf8(diskussion["Titel"]))
                __M_writer('</a>\r\n')
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
        __M_writer('</div>\r\n\t   \r\n \r\n\t   \r\n    </div>\r\n</div>\r\n\r\n<script>\r\n\r\n\r\nfunction ShowHide(){\r\n\tif(document.getElementById("HiddneDiv").style.display == \'none\'){\r\n\t\tdocument.getElementById("HiddneDiv").style.display=\'block\';\r\n\t}else{\r\n\t\tdocument.getElementById("HiddneDiv").style.display = \'none\';\r\n\t}\r\n}\r\n\r\n</script>\t  \r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/diskussionen.html", "uri": "diskussionen.html", "line_map": {"16": 2, "23": 2, "24": 3, "25": 3, "26": 7, "27": 7, "28": 14, "29": 14, "30": 29, "31": 30, "32": 32, "33": 42, "34": 43, "35": 51, "36": 52, "37": 52, "38": 52, "39": 53, "40": 54, "41": 54, "42": 54, "43": 54, "44": 54, "45": 54, "46": 54, "47": 56, "48": 57, "49": 58, "50": 59, "51": 59, "52": 60, "53": 60, "54": 64, "55": 68, "56": 68, "57": 68, "58": 68, "59": 70, "60": 71, "61": 71, "62": 71, "63": 71, "64": 71, "65": 73, "66": 81, "67": 101, "68": 101, "74": 68}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
