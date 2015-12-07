# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449341346.319479
_enable_loop = True
_template_filename = 'templates/beitraege.html'
_template_uri = 'beitraege.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,diskussion,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(title=title,pageargs=pageargs,thema=thema,diskussion=diskussion)
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
        __M_writer('</li>\r\n</ul>\r\n<br/>\r\n\r\n<div class="panel diskussion panel-primary">\r\n\t\r\n\t<div class="user-details">\r\n\t\t\t<table>\r\n\t\t\t<tr><td><i class="mdi-action-face-unlock"></i></td></tr>\r\n\t\t\t<tr><td><b>')
        __M_writer(filters.decode.utf8(diskussion["Ersteller"]))
        __M_writer('</b></td></tr>\r\n\t\t\t</table>\r\n\t</div>\r\n\r\n    <div class="panel-heading">')
        __M_writer(filters.decode.utf8(diskussion["Titel"]))
        __M_writer('</div>\r\n  \r\n\t<div class="panel-body" style="margin-left:100px;min-height:75px;">\r\n\t\t')
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
            __M_writer('\t<div class="panel panel-primary beitrag\r\n')
            if beitrag["Status"] == "deleted":
                __M_writer('\t\tpanel-danger\r\n')
            __M_writer('\t">\r\n\t\t<div class="panel-heading">')
            __M_writer(filters.decode.utf8(beitrag["Titel"]))
            __M_writer('</div>\r\n\t\t\r\n\t\t<div class="user-details">\r\n\t\t\t<table>\r\n\t\t\t<tr><td><i class="mdi-action-face-unlock"></i></td></tr>\r\n\t\t\t<tr><td><b>')
            __M_writer(filters.decode.utf8(beitrag["Ersteller"]))
            __M_writer('</b></td></tr>\r\n\t\t\t</table>\r\n\t\t</div>\r\n\t\t\r\n\t\t<div class="panel-body" style="margin-left:100px;min-height:75px;">\r\n\r\n')
            if beitrag["Status"] == "deleted":
                __M_writer('\t\t\t\t<b>Dieser Beitrag wurde gelöscht.</b>\r\n')
            else:
                __M_writer('\t\t\t\t\t')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('\r\n')
            __M_writer('\t\t\r\n')
            if role=="Administrator": 
                __M_writer('\t\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t\t<input type="hidden" name="id" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('"/>\r\n')
                if beitrag["Status"] == "deleted":
                    __M_writer('\t\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-material-green btn-xs"><i class="mdi-action-done"></i></button>\r\n')
                else:
                    __M_writer('\t\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n')
                __M_writer('\t\t\t\t\t</form>\r\n')
            if role=="Administrator" or beitrag["Bearbeitbar"] == True: 
                __M_writer('\t\t\t\t\t\r\n\t\t\t\t\t\t<button style="float:right;" type="button" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#editPost-')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('"><i class="mdi-content-create"></i></button>\r\n\r\n\t\t\t\t\t<div id="editPost-')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('" class="modal fade">\r\n\t\t\t\t\t\t<form method="POST" action="/beitraege">\r\n\t\t\t\t\t\t\t<div class="modal-dialog">\r\n\t\t\t\t\t\t\t\t<div class="modal-content">\r\n\t\t\t\t\t\t\t\t  <div class="modal-header">\r\n\t\t\t\t\t\t\t\t\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\r\n\t\t\t\t\t\t\t\t\t<h4 class="modal-title">Beitrag bearbeiten</h4>\r\n\t\t\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t\t\t  <div class="modal-body">\r\n\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t\t\t\t\t<input type="hidden" name="id" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                __M_writer(filters.decode.utf8(beitrag["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t\t\t\t<input type="text" class="form-control" name="title" value="')
                __M_writer(filters.decode.utf8(beitrag["Titel"]))
                __M_writer('">\r\n\t\t\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t\t\t<textarea class="form-control"  name="text" style="height:180px">')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('</textarea>\r\n\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t\t\t  <div class="modal-footer">\r\n\t\t\t\t\t\t\t\t\t<button type="button" class="btn btn-default" data-dismiss="modal">Abbrechen</button>\r\n\t\t\t\t\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary">Speichern</button>\r\n\t\t\t\t\t\t\t\t  </div>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\t\r\n\t\t\t\t\t\t</form>\r\n\t\t\t\t\t</div>\r\n\r\n')
            __M_writer('\t\t</div>\r\n\t\t<div class="panel-footer post-info">\r\n\t\t\t<table>\r\n\t\t\t<tr><td>Erstellt am: ')
            __M_writer(filters.decode.utf8(beitrag["Erstellt"]))
            __M_writer('</td></tr><tr><td>\r\n')
            if beitrag["Bearbeitet"] != " ":
                __M_writer('\t\t\tBearbeitet am ')
                __M_writer(filters.decode.utf8(beitrag["Bearbeitet"]))
                __M_writer(' von  ')
                __M_writer(filters.decode.utf8(beitrag["Bearbeiter"]))
                __M_writer('\r\n')
            __M_writer('\t\t\t</td></tr>\r\n\t\t\t</table>\r\n\t\t</div>\r\n\t</div>\r\n')
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
{"uri": "beitraege.html", "line_map": {"16": 2, "22": 2, "23": 3, "24": 3, "25": 7, "26": 7, "27": 7, "28": 7, "29": 8, "30": 8, "31": 17, "32": 17, "33": 21, "34": 21, "35": 24, "36": 24, "37": 25, "38": 26, "39": 27, "40": 27, "41": 28, "42": 28, "43": 32, "44": 33, "45": 46, "46": 46, "47": 47, "48": 47, "49": 48, "50": 48, "51": 50, "52": 50, "53": 64, "54": 67, "55": 67, "56": 68, "57": 69, "58": 69, "59": 69, "60": 71, "61": 72, "62": 72, "63": 73, "64": 74, "65": 74, "66": 74, "67": 76, "68": 82, "69": 83, "70": 84, "71": 85, "72": 87, "73": 88, "74": 88, "75": 93, "76": 93, "77": 99, "78": 100, "79": 101, "80": 102, "81": 102, "82": 102, "83": 104, "84": 105, "85": 106, "86": 107, "87": 107, "88": 108, "89": 108, "90": 109, "91": 109, "92": 110, "93": 111, "94": 112, "95": 113, "96": 115, "97": 117, "98": 118, "99": 119, "100": 119, "101": 121, "102": 121, "103": 131, "104": 131, "105": 132, "106": 132, "107": 133, "108": 133, "109": 134, "110": 134, "111": 136, "112": 136, "113": 149, "114": 152, "115": 152, "116": 153, "117": 154, "118": 154, "119": 154, "120": 154, "121": 154, "122": 156, "123": 161, "124": 162, "125": 163, "126": 167, "127": 183, "128": 183, "129": 184, "130": 184, "131": 207, "132": 207, "138": 132}, "filename": "templates/beitraege.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
