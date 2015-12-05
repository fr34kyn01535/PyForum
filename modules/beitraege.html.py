# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449331480.000925
_enable_loop = True
_template_filename = 'templates/beitraege.html'
_template_uri = 'beitraege.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,diskussion,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(diskussion=diskussion,pageargs=pageargs,thema=thema,title=title)
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
        __M_writer('</li>\r\n</ul>\r\n<br/>\r\n\r\n<div class="panel diskussion panel-primary">\r\n    <div class="panel-heading">')
        __M_writer(filters.decode.utf8(diskussion["Titel"]))
        __M_writer('</div>\r\n  \r\n\t<div class="panel-body">\r\n\t\t')
        __M_writer(filters.decode.utf8(diskussion["Text"]))
        __M_writer('\r\n')
        if role=="Administrator": 
            __M_writer('\t\t\t<form method="POST" action="/diskussionen">\r\n\t\t\t\t<input type="hidden" name="thema" value="')
            __M_writer(filters.decode.utf8(thema))
            __M_writer('"/>\r\n\t\t\t\t<input type="hidden" name="id" value="')
            __M_writer(filters.decode.utf8(diskussion["ID"]))
            __M_writer('"/>\r\n\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t</form>\r\n')
        if role=="Administrator" or diskussion["Bearbeitbar"] == True: 
            __M_writer('\r\n\t\t\t<button onclick="ShowHide(\'BearbeitenFormular-)" style="float:right;" class="btn btn-primary btn-xs"><i class="mdi-content-create"></i></button>\r\n\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t<div id="BearbeitenFormular" style="DISPLAY: none">\r\n\t\t\r\n\t\t\t\t<input type="hidden" name="thema" value="')
            __M_writer(filters.decode.utf8(thema))
            __M_writer('"/>\r\n\t\t\t\t<input type="hidden" name="id" value="')
            __M_writer(filters.decode.utf8(diskussion["ID"]))
            __M_writer('"/>\r\n\t\t\r\n\t\t\t\t<input type="text" class="form-control" name="title" value="')
            __M_writer(filters.decode.utf8(diskussion["Titel"]))
            __M_writer('">\r\n\t\r\n\t\t\t\t<textarea input type="text" class="form-control"  name="text" style="height:180px">')
            __M_writer(filters.decode.utf8(diskussion["Text"]))
            __M_writer('</textarea>\r\n\t\r\n\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary btn-material-green btn-sm">Speichern</button>\r\n\t\t\t\r\n\t\t\t\t</div>\r\n\t\t\t</form>\r\n')
        __M_writer('\t</div>  \r\n\t<div class="panel-footer">\r\n\t\t<ul class="post-info">\r\n\t\t\t<li>Autor: ')
        __M_writer(filters.decode.utf8(diskussion["Ersteller"]))
        __M_writer('</li>\r\n\t\t\t<li>Geschrieben: ')
        __M_writer(filters.decode.utf8(diskussion["Erstellt"]))
        __M_writer('</li>\r\n\t\t</ul>\r\n\t</div>\r\n</div>\r\n\r\n\r\n')
        for beitrag in diskussion["Beitraege"]:
            __M_writer('\r\n<div class="panel panel-default beitrag\r\n')
            if beitrag["Status"] == "deleted":
                __M_writer('\tpanel-danger\r\n')
            __M_writer('">\r\n    <div class="panel-heading">')
            __M_writer(filters.decode.utf8(beitrag["Titel"]))
            __M_writer('</div>\r\n    \r\n\r\n\t<div class="panel-body">\r\n\r\n')
            if beitrag["Status"] == "deleted":
                __M_writer('\t\t\t<b>Dieser Beitrag wurde gelöscht.</b>\r\n')
            else:
                __M_writer('\t\t\t\t')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('\r\n')
            __M_writer('\t\r\n')
            if role=="Administrator": 
                __M_writer('\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="id" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('"/>\r\n')
                if beitrag["Status"] == "deleted":
                    __M_writer('\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-material-green btn-xs"><i class="mdi-action-done"></i></button>\r\n')
                else:
                    __M_writer('\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n')
                __M_writer('\t\t\t\t</form>\r\n')
            if role=="Administrator" or beitrag["Bearbeitbar"] == True: 
                __M_writer('\t\t\t\t<button data-toggle="BearbeitenFormular-')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('" style="float:right;" class="btn btn-primary btn-xs toggleButton"><i class="mdi-content-create"></i></button>\r\n\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t<div id="BearbeitenFormular-')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('" style="DISPLAY: none">\r\n\t\t\t\t\t\r\n\t\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t\t<input type="hidden" name="id" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t<input type="text" class="form-control" name="title" value="')
                __M_writer(filters.decode.utf8(beitrag["Titel"]))
                __M_writer('">\r\n\t\t\t\t\t\t<textarea input type="text" class="form-control"  name="text" style="height:180px">')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('</textarea>\r\n\t\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary btn-material-green btn-sm">Bearbeiten</button>\r\n\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</form>\r\n')
            __M_writer('\t</div>\r\n\t<div class="panel-footer">\r\n\t\t<ul class="post-info">\r\n\t\t\t<li>Autor: ')
            __M_writer(filters.decode.utf8(diskussion["Ersteller"]))
            __M_writer('</li>\r\n\t\t\t<li>Geschrieben: ')
            __M_writer(filters.decode.utf8(diskussion["Erstellt"]))
            __M_writer('</li>\r\n\t\t</ul>\r\n\t</div>\r\n</div>\r\n\r\n')
        __M_writer('\r\n')
        if role=="Administrator" or role=="Bearbeiter":
            __M_writer('<button data-toggle="ErstellenFormular" style="float:right;" class="btn btn-raised btn-material-green toggleButton"><i class="mdi-content-add"></i></button>\r\n')
        __M_writer('<div style="clear:both;"></div>\r\n \r\n<form method="POST" action="/beitraege">\r\n<div id="ErstellenFormular" style="DISPLAY: none">\r\n\r\n\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\t<input type="hidden" name="id" value="')
        __M_writer(filters.decode.utf8(diskussion["ID"]))
        __M_writer('"/>\r\n\r\n\t<input type="text" class="form-control floating-label" placeholder="Titel" name="title">\r\n\r\n\r\n\t<textarea input type="text" class="form-control floating-label" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\r\n\t<button type="submit" name="action" value="create" class="btn btn-primary btn-material-green btn-sm">Erstellen</button>\r\n\r\n</div>\r\n</form>\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "templates/beitraege.html", "line_map": {"16": 2, "22": 2, "23": 3, "24": 3, "25": 7, "26": 7, "27": 7, "28": 7, "29": 8, "30": 8, "31": 13, "32": 13, "33": 16, "34": 16, "35": 17, "36": 18, "37": 19, "38": 19, "39": 20, "40": 20, "41": 24, "42": 25, "43": 30, "44": 30, "45": 31, "46": 31, "47": 33, "48": 33, "49": 35, "50": 35, "51": 42, "52": 45, "53": 45, "54": 46, "55": 46, "56": 52, "57": 53, "58": 55, "59": 56, "60": 58, "61": 59, "62": 59, "63": 64, "64": 65, "65": 66, "66": 67, "67": 67, "68": 67, "69": 69, "70": 70, "71": 71, "72": 72, "73": 72, "74": 73, "75": 73, "76": 74, "77": 74, "78": 75, "79": 76, "80": 77, "81": 78, "82": 80, "83": 82, "84": 83, "85": 83, "86": 83, "87": 85, "88": 85, "89": 87, "90": 87, "91": 88, "92": 88, "93": 89, "94": 89, "95": 91, "96": 91, "97": 92, "98": 92, "99": 98, "100": 101, "101": 101, "102": 102, "103": 102, "104": 108, "105": 109, "106": 110, "107": 112, "108": 117, "109": 117, "110": 118, "111": 118, "112": 134, "113": 134, "119": 113}, "uri": "beitraege.html"}
__M_END_METADATA
"""
