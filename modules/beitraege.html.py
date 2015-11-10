# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1447152727.8971817
_enable_loop = True
_template_filename = 'templates/beitraege.html'
_template_uri = 'beitraege.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,diskussion,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(thema=thema,title=title,pageargs=pageargs,diskussion=diskussion)
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
            __M_writer('\r\n\t\t\t\t<button onclick="ShowHide(\'BearbeitenFormular\')" style="float:right;" class="btn btn-primary btn-xs"><i class="mdi-content-create"></i></button>\r\n\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t<div id="BearbeitenFormular" style="DISPLAY: none">\r\n\t\t\t\r\n\t\t\t\t\t<input type="hidden" name="thema" value="')
            __M_writer(filters.decode.utf8(thema))
            __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="id" value="')
            __M_writer(filters.decode.utf8(diskussion["ID"]))
            __M_writer('"/>\r\n\t\t\t\r\n\t\t\t\t\t<input type="text" class="form-control" name="title" value="')
            __M_writer(filters.decode.utf8(diskussion["Titel"]))
            __M_writer('">\r\n\t\t\r\n\t\t\t\t\t<textarea input type="text" class="form-control"  name="text" style="height:180px">')
            __M_writer(filters.decode.utf8(diskussion["Text"]))
            __M_writer('</textarea>\r\n\t\t\r\n\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary btn-material-green btn-sm">Bearbeiten</button>\r\n\t\t\t\t\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</form>\r\n')
        __M_writer('</div>\r\n    </div>\r\n</div>\r\n\r\n')
        for beitrag in diskussion["Beitraege"]:
            __M_writer('\r\n<div class="panel \r\n')
            if beitrag["Status"] == "deleted":
                __M_writer('panel-danger\r\n')
            else:
                __M_writer('panel-default\r\n')
            __M_writer('beitrag">\r\n    <div class="panel-heading">')
            __M_writer(filters.decode.utf8(beitrag["Titel"]))
            __M_writer('</div>\r\n    <div class="panel-body">\r\n\t   \r\n\t\r\n\t \r\n\t   \r\n\t   <div class="list-group">\r\n\t     \r\n')
            if beitrag["Status"] == "deleted":
                __M_writer('\t\t\t<div class="list-group-item">\r\n\t\t\tDieser Beitrag wurde gelöscht.\r\n\t\t\t</div>\r\n\t   \r\n')
            else:
                __M_writer('   \t\t\t<p class="list-group-item-text datum">(')
                __M_writer(filters.decode.utf8(beitrag["Erstellt"]))
                __M_writer(')</p>\r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<table class="table">\r\n\t\t\t\t\t<td style="width:100px;">\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
                __M_writer(filters.decode.utf8(beitrag["Ersteller"]))
                __M_writer('</p></i>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<div class="least-content"></div>\t\t\t\t\t\t\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('</p>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</table>\r\n\t\t\t</div>\r\n\t\t\t\r\n')
            __M_writer('\t\t\t\r\n\t\t\t<div class="list-group-separator"></div>\r\n\r\n')
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
                __M_writer('\t\t\t\t<button data-toggle="BearbeitenFormular" style="float:right;" class="btn btn-primary btn-xs toggleButton"><i class="mdi-content-create"></i></button>\r\n\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t<div id="BearbeitenFormular" style="DISPLAY: none">\r\n\t\t\t\t\t\r\n\t\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t\t<input type="hidden" name="id" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t<input type="text" class="form-control" name="title" value="')
                __M_writer(filters.decode.utf8(beitrag["Titel"]))
                __M_writer('">\r\n\t\t\t\t\t\t<textarea input type="text" class="form-control"  name="text" style="height:180px">')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('</textarea>\r\n\t\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary btn-material-green btn-sm">Bearbeiten</button>\r\n\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</form>\r\n</div>\r\n\r\n')
            __M_writer('\r\n    </div>\r\n</div>\r\n')
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
{"source_encoding": "utf-8", "filename": "templates/beitraege.html", "uri": "beitraege.html", "line_map": {"16": 2, "22": 2, "23": 3, "24": 3, "25": 7, "26": 7, "27": 7, "28": 7, "29": 8, "30": 8, "31": 13, "32": 13, "33": 16, "34": 16, "35": 20, "36": 20, "37": 24, "38": 24, "39": 30, "40": 31, "41": 32, "42": 32, "43": 33, "44": 33, "45": 37, "46": 38, "47": 43, "48": 43, "49": 44, "50": 44, "51": 46, "52": 46, "53": 48, "54": 48, "55": 55, "56": 59, "57": 60, "58": 62, "59": 63, "60": 64, "61": 65, "62": 67, "63": 68, "64": 68, "65": 76, "66": 77, "67": 81, "68": 82, "69": 82, "70": 82, "71": 86, "72": 86, "73": 90, "74": 90, "75": 96, "76": 99, "77": 100, "78": 101, "79": 101, "80": 102, "81": 102, "82": 103, "83": 103, "84": 107, "85": 108, "86": 109, "87": 113, "88": 113, "89": 114, "90": 114, "91": 115, "92": 115, "93": 117, "94": 117, "95": 118, "96": 118, "97": 126, "98": 130, "99": 131, "100": 132, "101": 134, "102": 139, "103": 139, "104": 140, "105": 140, "106": 156, "107": 156, "113": 107}}
__M_END_METADATA
"""
