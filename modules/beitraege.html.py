# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1447148580.1488047
_enable_loop = True
_template_filename = 'templates/beitraege.html'
_template_uri = 'beitraege.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,diskussion,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,diskussion=diskussion,thema=thema,title=title)
        role = context.get('role', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li>\r\n    <li><a href="/diskussionen?thema=')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('">')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('</a></li>\r\n    <li class="active">')
        __M_writer(filters.decode.utf8(diskussion["Titel"]))
        __M_writer('</li>\r\n</ul>\r\n<br/>\r\n\r\n<div class="panel panel-default diskussion">\r\n    <div class="panel-heading">')
        __M_writer(filters.decode.utf8(diskussion["Titel"]))
        __M_writer('</div>\r\n    <div class="panel-body">\r\n\t   <div class="list-group">\r\n   \t\t\t<p class="list-group-item-text datum">(')
        __M_writer(filters.decode.utf8(diskussion["Erstellt"]))
        __M_writer(')</p>\r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<table class="table">\r\n\t\t\t\t\t<td style="width:100px;">\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
        __M_writer(filters.decode.utf8(diskussion["Ersteller"]))
        __M_writer('</p></i>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<div class="least-content"></div>\t\t\t\t\t\t\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
        __M_writer(filters.decode.utf8(diskussion["Text"]))
        __M_writer('</p>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</table>\r\n\t\t\t</div>\r\n\t\t\t<div class="list-group-separator"></div>\r\n\r\n')
        if role=="Administrator": 
            __M_writer('\t\t\t\t<form method="POST" action="/diskussionen">\r\n\t\t\t\t\t<input type="hidden" name="thema" value="')
            __M_writer(filters.decode.utf8(thema))
            __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="id" value="')
            __M_writer(filters.decode.utf8(diskussion["ID"]))
            __M_writer('"/>\r\n\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t\t</form>\r\n')
        if role=="Administrator" or diskussion["Bearbeitbar"] == True: 
            __M_writer('\r\n\t\t\t\t<button onclick="ShowHide(\'BearbeitenFormular\')" style="float:right;" class="btn btn-primary btn-xs"><i class="mdi-content-create"></i></button>\r\n\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t<div id="BearbeitenFormular" style="DISPLAY: none">\r\n\t\t\t\t\t<ul class="wmfg_questions">\r\n\t\t\t\t\t<input type="hidden" name="thema" value="')
            __M_writer(filters.decode.utf8(thema))
            __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="id" value="')
            __M_writer(filters.decode.utf8(diskussion["ID"]))
            __M_writer('"/>\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t<input type="text" class="form-control" name="title" value="')
            __M_writer(filters.decode.utf8(diskussion["Titel"]))
            __M_writer('">\r\n\t\t\t\t\t</li>\r\n\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t<textarea input type="text" class="form-control"  name="text" style="height:180px">')
            __M_writer(filters.decode.utf8(diskussion["Text"]))
            __M_writer('</textarea>\r\n\t\t\t\t\t</li>\r\n\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary btn-material-green btn-sm">Bearbeiten</button>\r\n\t\t\t\t\t</li>\r\n\t\t\t\t\t</ul>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</form>\r\n')
        __M_writer('</div>\r\n    </div>\r\n</div>\r\n\r\n')
        for beitrag in diskussion["Beitraege"]:
            __M_writer('\r\n<div class="panel panel-default beitrag">\r\n    <div class="panel-heading">')
            __M_writer(filters.decode.utf8(beitrag["Titel"]))
            __M_writer('</div>\r\n    <div class="panel-body">\r\n\t   \r\n')
            if beitrag["Status"] == "deleted":
                __M_writer('\t   \r\n\t\t\tDieser Beitrag wurde gelöscht.\r\n\t   \r\n')
            else:
                __M_writer('\t   \r\n\t   <div class="list-group">\r\n   \t\t\t<p class="list-group-item-text datum">(')
                __M_writer(filters.decode.utf8(beitrag["Erstellt"]))
                __M_writer(')</p>\r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<table class="table">\r\n\t\t\t\t\t<td style="width:100px;">\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
                __M_writer(filters.decode.utf8(beitrag["Ersteller"]))
                __M_writer('</p></i>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<div class="least-content"></div>\t\t\t\t\t\t\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('</p>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</table>\r\n\t\t\t</div>\r\n\t\t\t<div class="list-group-separator"></div>\r\n\r\n')
                if role=="Administrator": 
                    __M_writer('\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t<input type="hidden" name="thema" value="')
                    __M_writer(filters.decode.utf8(thema))
                    __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="id" value="')
                    __M_writer(filters.decode.utf8(diskussion["ID"]))
                    __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                    __M_writer(filters.decode.utf8(beitrag["ID"]))
                    __M_writer('"/>\r\n\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t\t</form>\r\n')
                __M_writer('\r\n')
                if role=="Administrator" or beitrag["Bearbeitbar"] == True: 
                    __M_writer('\t\t\t\t<button onclick="ShowHide(\'BearbeitenFormular\')" style="float:right;" class="btn btn-primary btn-xs"><i class="mdi-content-create"></i></button>\r\n\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t<div id="BearbeitenFormular" style="DISPLAY: none">\r\n\t\t\t\t\t<ul class="wmfg_questions">\r\n\t\t\t\t\t<input type="hidden" name="thema" value="')
                    __M_writer(filters.decode.utf8(thema))
                    __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="id" value="')
                    __M_writer(filters.decode.utf8(diskussion["ID"]))
                    __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                    __M_writer(filters.decode.utf8(beitrag["ID"]))
                    __M_writer('"/>\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t<input type="text" class="form-control" name="title" value="')
                    __M_writer(filters.decode.utf8(beitrag["Titel"]))
                    __M_writer('">\r\n\t\t\t\t\t</li>\r\n\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t<textarea input type="text" class="form-control"  name="text" style="height:180px">')
                    __M_writer(filters.decode.utf8(beitrag["Text"]))
                    __M_writer('</textarea>\r\n\t\t\t\t\t</li>\r\n\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary btn-material-green btn-sm">Bearbeiten</button>\r\n\t\t\t\t\t</li>\r\n\t\t\t\t\t</ul>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</form>\r\n')
                __M_writer('</div>\r\n\r\n')
            __M_writer('\r\n    </div>\r\n</div>\r\n')
        __M_writer('\r\n')
        if role=="Administrator" or role=="Bearbeiter":
            __M_writer('<button onclick="ShowHide(\'ErstellenFormular\')" style="float:right;" class="btn btn-raised btn-material-green"><i class="mdi-content-add"></i></button>\r\n')
        __M_writer('<div style="clear:both;"></div>\r\n \r\n<form method="POST" action="/beitraege">\r\n<div id="ErstellenFormular" style="DISPLAY: none">\r\n<ul class="wmfg_questions">\r\n\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\t<input type="hidden" name="id" value="')
        __M_writer(filters.decode.utf8(diskussion["ID"]))
        __M_writer('"/>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t<input type="text" class="form-control floating-label" placeholder="Titel" name="title">\r\n\t</li>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t\r\n\t\t<textarea input type="text" class="form-control floating-label" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\t</li>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t<button type="submit" name="action" value="create" class="btn btn-primary btn-material-green btn-sm">Erstellen</button>\r\n\r\n\t</li>\r\n\r\n</ul>\r\n</div>\r\n</form>\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n<script>\r\nfunction ShowHide(id){\r\n\tif(document.getElementById(id).style.display == \'none\'){\r\n\t\tdocument.getElementById(id).style.display=\'block\';\r\n\t}else{\r\n\t\tdocument.getElementById(id).style.display = \'none\';\r\n\t}\r\n}\r\n\r\n</script>\t\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 2, "22": 2, "23": 3, "24": 3, "25": 7, "26": 7, "27": 7, "28": 7, "29": 8, "30": 8, "31": 13, "32": 13, "33": 16, "34": 16, "35": 20, "36": 20, "37": 24, "38": 24, "39": 30, "40": 31, "41": 32, "42": 32, "43": 33, "44": 33, "45": 37, "46": 38, "47": 43, "48": 43, "49": 44, "50": 44, "51": 46, "52": 46, "53": 51, "54": 51, "55": 61, "56": 65, "57": 66, "58": 68, "59": 68, "60": 71, "61": 72, "62": 75, "63": 76, "64": 78, "65": 78, "66": 82, "67": 82, "68": 86, "69": 86, "70": 92, "71": 93, "72": 94, "73": 94, "74": 95, "75": 95, "76": 96, "77": 96, "78": 100, "79": 101, "80": 102, "81": 106, "82": 106, "83": 107, "84": 107, "85": 108, "86": 108, "87": 110, "88": 110, "89": 115, "90": 115, "91": 125, "92": 128, "93": 132, "94": 133, "95": 134, "96": 136, "97": 141, "98": 141, "99": 142, "100": 142, "101": 176, "102": 176, "108": 102}, "filename": "templates/beitraege.html", "uri": "beitraege.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
