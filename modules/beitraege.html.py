# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449337491.118413
_enable_loop = True
_template_filename = 'templates/beitraege.html'
_template_uri = 'beitraege.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,diskussion,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,thema=thema,title=title,diskussion=diskussion)
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
            __M_writer('\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t<input type="hidden" name="thema" value="')
            __M_writer(filters.decode.utf8(thema))
            __M_writer('"/>\r\n\t\t\t\t<input type="hidden" name="id" value="')
            __M_writer(filters.decode.utf8(diskussion["ID"]))
            __M_writer('"/>\r\n\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t</form>\r\n')
        if role=="Administrator" or diskussion["Bearbeitbar"] == True: 
            __M_writer('\r\n\t\t\t<button style="float:right;" type="button" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#editPost"><i class="mdi-content-create"></i></button>\r\n\r\n\t\t\t<div id="editPost" class="modal fade">\r\n\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t<div class="modal-dialog">\r\n\t\t\t\t\t\t<div class="modal-content">\r\n\t\t\t\t\t\t  <div class="modal-header">\r\n\t\t\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\r\n\t\t\t\t\t\t\t<h4 class="modal-title">Beitrag bearbeiten</h4>\r\n\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t  <div class="modal-body">\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t<input type="hidden" name="thema" value="')
            __M_writer(filters.decode.utf8(thema))
            __M_writer('"/>\r\n\t\t\t\t\t\t\t\t<input type="hidden" name="id" value="')
            __M_writer(filters.decode.utf8(diskussion["ID"]))
            __M_writer('"/>\r\n\t\t\t\t\t\t\t\t<input type="text" class="form-control" name="title" value="')
            __M_writer(filters.decode.utf8(diskussion["Titel"]))
            __M_writer('">\r\n\t\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t\t<textarea class="form-control"  name="text" style="height:180px">')
            __M_writer(filters.decode.utf8(diskussion["Text"]))
            __M_writer('</textarea>\r\n\t\t\t\t\r\n\t\t\t\t\r\n\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t  <div class="modal-footer">\r\n\t\t\t\t\t\t\t<button type="button" class="btn btn-default" data-dismiss="modal">Abbrechen</button>\r\n\t\t\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary">Speichern</button>\r\n\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\t\r\n\t\t\t\t</form>\r\n\t\t\t</div>\r\n\t\t\t\r\n')
        __M_writer('\t</div> \r\n\t<div class="panel-footer post-info">\r\n\t\t<table>\r\n\t\t<tr><td>Autor: ')
        __M_writer(filters.decode.utf8(diskussion["Ersteller"]))
        __M_writer('</td><td>\r\n')
        if diskussion["Bearbeiter"] != " ":
            __M_writer('\t\t Bearbeiter: ')
            __M_writer(filters.decode.utf8(diskussion["Bearbeiter"]))
            __M_writer('\r\n')
        __M_writer('\t\t </td></tr>\r\n\t\t<tr><td>Erstellt am: ')
        __M_writer(filters.decode.utf8(diskussion["Erstellt"]))
        __M_writer('</td><td>\r\n')
        if diskussion["Bearbeitet"] != " ":
            __M_writer('\t\tBearbeitet am: ')
            __M_writer(filters.decode.utf8(diskussion["Bearbeitet"]))
            __M_writer('\r\n')
        __M_writer('\t\t</td></tr>\r\n\t\t</table>\r\n\t</div>\r\n</div>\r\n\r\n\r\n')
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
                __M_writer('\t\t\t\t\r\n\t\t\t\t\t<button style="float:right;" type="button" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#editPost-')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('"><i class="mdi-content-create"></i></button>\r\n\r\n\t\t\t\t<div id="editPost-')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('" class="modal fade">\r\n\t\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t\t<div class="modal-dialog">\r\n\t\t\t\t\t\t\t<div class="modal-content">\r\n\t\t\t\t\t\t\t  <div class="modal-header">\r\n\t\t\t\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\r\n\t\t\t\t\t\t\t\t<h4 class="modal-title">Beitrag bearbeiten</h4>\r\n\t\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t\t  <div class="modal-body">\r\n\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t\t\t\t<input type="hidden" name="id" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t\t\t<input type="text" class="form-control" name="title" value="')
                __M_writer(filters.decode.utf8(beitrag["Titel"]))
                __M_writer('">\r\n\t\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t\t<textarea class="form-control"  name="text" style="height:180px">')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('</textarea>\r\n\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t\t  <div class="modal-footer">\r\n\t\t\t\t\t\t\t\t<button type="button" class="btn btn-default" data-dismiss="modal">Abbrechen</button>\r\n\t\t\t\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary">Speichern</button>\r\n\t\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\t\r\n\t\t\t\t\t</form>\r\n\t\t\t\t</div>\r\n\r\n')
            __M_writer('\t</div>\r\n\t<div class="panel-footer post-info">\r\n\t\t<table>\r\n\t\t<tr><td>Autor: ')
            __M_writer(filters.decode.utf8(beitrag["Ersteller"]))
            __M_writer('</td><td>\r\n')
            if beitrag["Bearbeiter"] != " ":
                __M_writer('\t\t Bearbeiter: ')
                __M_writer(filters.decode.utf8(beitrag["Bearbeiter"]))
                __M_writer('\r\n')
            __M_writer('\t\t </td></tr>\r\n\t\t<tr><td>Erstellt am: ')
            __M_writer(filters.decode.utf8(beitrag["Erstellt"]))
            __M_writer('</td><td>\r\n')
            if beitrag["Bearbeitet"] != " ":
                __M_writer('\t\tBearbeitet am: ')
                __M_writer(filters.decode.utf8(beitrag["Bearbeitet"]))
                __M_writer('\r\n')
            __M_writer('\t\t</td></tr>\r\n\t\t</table>\r\n\t</div>\r\n</div>\r\n\r\n')
        __M_writer('\r\n')
        if role=="Administrator" or role=="Bearbeiter":
            __M_writer('\r\n<button style="float:right;" type="button" class="btn btn-primary" data-toggle="modal" data-target="#newPost">Neuer Beitrag</button>\r\n\r\n')
        __M_writer('<div style="clear:both;"></div>\r\n \r\n \r\n \r\n \r\n \r\n<div id="newPost" class="modal fade">\r\n\t<form method="POST" action="/beitraege">\r\n\t  <div class="modal-dialog">\r\n\t\t<div class="modal-content">\r\n\t\t  <div class="modal-header">\r\n\t\t\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\r\n\t\t\t<h4 class="modal-title">Neuer Beitrag</h4>\r\n\t\t  </div>\r\n\t\t  <div class="modal-body">\r\n\t\t\t\r\n\t\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\t<input type="hidden" name="id" value="')
        __M_writer(filters.decode.utf8(diskussion["ID"]))
        __M_writer('"/>\r\n\r\n\t<input type="text" class="form-control floating-label" placeholder="Titel" name="title">\r\n\t<br/>\r\n\t<textarea class="form-control floating-label" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\r\n\t\t\t\r\n\t\t  </div>\r\n\t\t  <div class="modal-footer">\r\n\t\t\t<button type="button" class="btn btn-default" data-dismiss="modal">Abbrechen</button>\r\n\t\t\t<button type="submit" name="action" value="create" class="btn btn-primary">Erstellen</button>\r\n\t\t  </div>\r\n\t\t</div>\r\n\t  </div>\t\r\n\t  </form>\r\n\t</div>\r\n\r\n \r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "22": 2, "23": 3, "24": 3, "25": 7, "26": 7, "27": 7, "28": 7, "29": 8, "30": 8, "31": 13, "32": 13, "33": 16, "34": 16, "35": 17, "36": 18, "37": 19, "38": 19, "39": 20, "40": 20, "41": 24, "42": 25, "43": 38, "44": 38, "45": 39, "46": 39, "47": 40, "48": 40, "49": 42, "50": 42, "51": 56, "52": 59, "53": 59, "54": 60, "55": 61, "56": 61, "57": 61, "58": 63, "59": 64, "60": 64, "61": 65, "62": 66, "63": 66, "64": 66, "65": 68, "66": 74, "67": 75, "68": 77, "69": 78, "70": 80, "71": 81, "72": 81, "73": 86, "74": 87, "75": 88, "76": 89, "77": 89, "78": 89, "79": 91, "80": 92, "81": 93, "82": 94, "83": 94, "84": 95, "85": 95, "86": 96, "87": 96, "88": 97, "89": 98, "90": 99, "91": 100, "92": 102, "93": 104, "94": 105, "95": 106, "96": 106, "97": 108, "98": 108, "99": 118, "100": 118, "101": 119, "102": 119, "103": 120, "104": 120, "105": 121, "106": 121, "107": 123, "108": 123, "109": 136, "110": 139, "111": 139, "112": 140, "113": 141, "114": 141, "115": 141, "116": 143, "117": 144, "118": 144, "119": 145, "120": 146, "121": 146, "122": 146, "123": 148, "124": 154, "125": 155, "126": 156, "127": 160, "128": 176, "129": 176, "130": 177, "131": 177, "132": 200, "133": 200, "139": 133}, "uri": "beitraege.html", "filename": "templates/beitraege.html"}
__M_END_METADATA
"""
