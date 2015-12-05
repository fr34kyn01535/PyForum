# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449334072.0050766
_enable_loop = True
_template_filename = 'templates/diskussionen.html'
_template_uri = 'diskussionen.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(thema=thema,title=title,pageargs=pageargs)
        diskussionen = context.get('diskussionen', UNDEFINED)
        role = context.get('role', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li> \t\r\n    <li class="active">')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('</li>   \r\n</ul>\r\n<br/>\r\n\r\n<div id="newDiscussion" class="modal fade">\r\n\t<form method="POST" action="/diskussionen">\r\n\t  <div class="modal-dialog">\r\n\t\t<div class="modal-content">\r\n\t\t  <div class="modal-header">\r\n\t\t\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\r\n\t\t\t<h4 class="modal-title">Neue Diskussion</h4>\r\n\t\t  </div>\r\n\t\t  <div class="modal-body">\r\n\t\t\t\r\n\t\t\t\r\n\t\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\t\t\t<input type="text" class="form-control floating-label" required="required" placeholder="Titel" name="title">\r\n\t<br/>\r\n\t\t\t<textarea class="form-control floating-label" required="required" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\t\r\n\t\r\n\t\t\t\r\n\t\t\t\r\n\t\t  </div>\r\n\t\t  <div class="modal-footer">\r\n\t\t\t<button type="button" class="btn btn-default" data-dismiss="modal">Abbrechen</button>\r\n\t\t\t<button type="submit" name="action" value="create" class="btn btn-primary">Erstellen</button>\r\n\t\t  </div>\r\n\t\t</div>\r\n\t  </div>\t\r\n\t  </form>\r\n\t</div>\r\n\r\n')
        if role=="Administrator" or role=="Bearbeiter": 	 
            __M_writer('\r\n<button style="float:right;" type="button" class="btn btn-primary" data-toggle="modal" data-target="#newDiscussion">Neue Diskussion</button>\r\n\r\n\r\n')
        __M_writer('\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n<div class="panel panel-default">\r\n    <div class="panel-heading">Diskussionen</div>\r\n    <div class="panel-body">\r\n       \r\n\t   <div class="list-group">\r\n')
        for diskussion in diskussionen:
            __M_writer(' \r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t<div class="row-action-primary">\r\n\t\t\t\t\t<i class="mdi-file-folder"></i>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="row-content">\r\n\t\t\t\t\t<div class="least-content"></div>\r\n\r\n')
            if diskussion["Status"] == "deleted":
                __M_writer('\t\t\t\t\t\t<h4 class="list-group-item-heading">')
                __M_writer(filters.decode.utf8(diskussion["Titel"]))
                __M_writer(' [Gelöscht]</h4>\t\r\n')
            else:
                __M_writer('\t\t\t\t\t\t<h4 class="list-group-item-heading"><a href="/beitraege?thema=')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('&amp;id=')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('">')
                __M_writer(filters.decode.utf8(diskussion["Titel"]))
                __M_writer('</a></h4>\t\r\n')
            __M_writer('\t\t\t\t\t\r\n')
            if role=="Administrator": 
                __M_writer('\t\t\t\t\t\t<form method="POST" action="/diskussionen">\r\n\t\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t\t<input type="hidden" name="id" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('"/>\r\n\t\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t\t\t\t</form>\r\n')
            __M_writer('\r\n\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t<br/>\r\n\r\n\t\t\t\t\t<p class="list-group-item-text">von ')
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
{"filename": "templates/diskussionen.html", "line_map": {"16": 2, "23": 2, "24": 3, "25": 3, "26": 7, "27": 7, "28": 22, "29": 22, "30": 40, "31": 41, "32": 46, "33": 56, "34": 57, "35": 65, "36": 66, "37": 66, "38": 66, "39": 67, "40": 68, "41": 68, "42": 68, "43": 68, "44": 68, "45": 68, "46": 68, "47": 70, "48": 71, "49": 72, "50": 73, "51": 73, "52": 74, "53": 74, "54": 78, "55": 82, "56": 82, "57": 82, "58": 82, "59": 84, "60": 85, "61": 85, "62": 85, "63": 85, "64": 85, "65": 87, "66": 95, "67": 102, "68": 102, "74": 68}, "source_encoding": "utf-8", "uri": "diskussionen.html"}
__M_END_METADATA
"""
