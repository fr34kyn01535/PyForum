# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449341405.444031
_enable_loop = True
_template_filename = 'templates/diskussionen-liste.html'
_template_uri = 'diskussionen-liste.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        role = context.get('role', UNDEFINED)
        thema = context.get('thema', UNDEFINED)
        diskussionen = context.get('diskussionen', UNDEFINED)
        __M_writer = context.writer()
        for diskussion in diskussionen:
            __M_writer('\r\n\t<div class="list-group-item">\r\n\t\t<div class="row-action-primary">\r\n\t\t\t<i class="mdi-file-folder"></i>\r\n\t\t</div>\r\n\t\t<div class="row-content">\r\n\t\t\t<div class="least-content"></div>\r\n\r\n')
            if diskussion["Status"] == "deleted":
                __M_writer('\t\t\t\t<h4 class="list-group-item-heading">')
                __M_writer(filters.decode.utf8(diskussion["Titel"]))
                __M_writer(' [Gelöscht]</h4>\t\r\n')
            else:
                __M_writer('\t\t\t\t<h4 class="list-group-item-heading"><a href="/beitraege?thema=')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('&amp;id=')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('">')
                __M_writer(filters.decode.utf8(diskussion["Titel"]))
                __M_writer('</a></h4>\t\r\n')
            __M_writer('\t\t\t\r\n\t\t\t\t\r\n')
            if role=="Administrator": 
                __M_writer('\t\t\t\t<button style="float:right;" value="')
                __M_writer(filters.decode.utf8(diskussion["ID"]))
                __M_writer('" class="deleteDiscussion btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n')
            __M_writer('\t\t\t\t\t\r\n\r\n\t\t\t<p class="list-group-item-text">von ')
            __M_writer(filters.decode.utf8(diskussion["Ersteller"]))
            __M_writer(' (')
            __M_writer(filters.decode.utf8(diskussion["Erstellt"]))
            __M_writer(')</p>\r\n\r\n')
            if diskussion["Bearbeiter"] != " ": 
                __M_writer('\t\t\t\t<p class="list-group-item-text">zuletzt bearbeitet von ')
                __M_writer(filters.decode.utf8(diskussion["Bearbeiter"]))
                __M_writer(' (')
                __M_writer(filters.decode.utf8(diskussion["Bearbeitet"]))
                __M_writer(')</p>\r\n')
            __M_writer('\r\n\r\n\t\t</div>\r\n\t</div>\r\n\t\r\n\t<div class="list-group-separator"></div>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "diskussionen-liste.html", "line_map": {"16": 0, "24": 1, "25": 2, "26": 10, "27": 11, "28": 11, "29": 11, "30": 12, "31": 13, "32": 13, "33": 13, "34": 13, "35": 13, "36": 13, "37": 13, "38": 15, "39": 17, "40": 18, "41": 18, "42": 18, "43": 20, "44": 22, "45": 22, "46": 22, "47": 22, "48": 24, "49": 25, "50": 25, "51": 25, "52": 25, "53": 25, "54": 27, "60": 54}, "filename": "templates/diskussionen-liste.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
