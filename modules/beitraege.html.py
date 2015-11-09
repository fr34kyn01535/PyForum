# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1447086843.6711905
_enable_loop = True
_template_filename = 'templates/beitraege.html'
_template_uri = 'beitraege.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,discussionname,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(title=title,discussionname=discussionname,pageargs=pageargs,thema=thema)
        beitraege = context.get('beitraege', UNDEFINED)
        role = context.get('role', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li>\r\n    <li><a href="/thema?thema=')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('">')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('</a></li>\r\n    <li class="active">')
        __M_writer(filters.decode.utf8(discussionname))
        __M_writer('</li>\r\n</ul>\r\n<br/>\r\n\r\n')
        for beitrag in beitraege:
            __M_writer('<div class="panel panel-default beitrag">\r\n    <div class="panel-heading">')
            __M_writer(filters.decode.utf8(beitrag["Titel"]))
            __M_writer('</div>\r\n    <div class="panel-body">\r\n       \r\n\t   \r\n\t   <div class="list-group">\r\n\t   \r\n   \t\t\t<p class="list-group-item-text datum">(')
            __M_writer(filters.decode.utf8(beitrag["Erstellt"]))
            __M_writer(')</p>\r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t\r\n\t\t\t\t<table class="table">\r\n\t\t\t\t\t<td style="width:100px;">\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
            __M_writer(filters.decode.utf8(beitrag["Ersteller"]))
            __M_writer('</p></i>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<div class="least-content"></div>\t\t\t\t\t\t\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
            __M_writer(filters.decode.utf8(beitrag["Text"]))
            __M_writer('</p>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</table>\r\n\t\t\t</div>\r\n\t\t\t<div class="list-group-separator"></div>\r\n\r\n')
            if role=="Administrator": 
                __M_writer('\t\t\t\t<form method="POST" action="/diskussion">\r\n\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="discussionname" value="')
                __M_writer(filters.decode.utf8(discussionname))
                __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="title" value="')
                __M_writer(filters.decode.utf8(beitrag["Titel"]))
                __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="text" value="')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('"/>\r\n\t\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t\t</form>\r\n\r\n\t\t\t\t<button onclick="ShowHide(\'BearbeitenFormular\')" style="float:right;" class="btn btn-primary btn-xs"><i class="mdi-content-create"></i></button>\r\n\t\t\t\t<form method="POST" action="/diskussion">\r\n\t\t\t\t\t<div id="BearbeitenFormular" style="DISPLAY: none">\r\n\t\t\t\t\t<ul class="wmfg_questions">\r\n\t\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="discussionname" value="')
                __M_writer(filters.decode.utf8(discussionname))
                __M_writer('"/>\r\n\t\t\t\t\t<input type="hidden" name="beitragID" value="')
                __M_writer(filters.decode.utf8(beitrag["BeitragID"]))
                __M_writer('"/>\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t<input type="text" class="form-control" name="newtitle" value="')
                __M_writer(filters.decode.utf8(beitrag["Titel"]))
                __M_writer('">\r\n\t\t\t\t\t</li>\r\n\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t<textarea input type="text" class="form-control"  name="newtext" style="height:180px">')
                __M_writer(filters.decode.utf8(beitrag["Text"]))
                __M_writer('</textarea>\r\n\t\t\t\t\t</li>\r\n\r\n\t\t\t\t\t<li class="wmfg_q">\r\n\t\t\t\t\t\t<button type="submit" name="action" value="edit" class="btn btn-primary btn-material-green btn-sm">Bearbeiten</button>\r\n\t\t\t\t\t</li>\r\n\t\t\t\t\t</ul>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</form>\r\n\r\n')
            __M_writer('</div>\r\n\t   \r\n\t   \r\n\t   \r\n    </div>\r\n</div>\r\n')
        __M_writer('\r\n')
        if role=="Administrator" or role=="Bearbeiter":
            __M_writer('<button onclick="ShowHide(\'ErstellenFormular\')" style="float:right;" class="btn btn-fab btn-raised btn-material-green btn-xs"><i class="mdi-content-add"></i></button>\r\n')
        __M_writer('<div style="clear:both;"></div>\r\n\r\n<form method="POST" action="/diskussion">\r\n<div id="ErstellenFormular" style="DISPLAY: none">\r\n<ul class="wmfg_questions">\r\n\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\t<input type="hidden" name="discussionname" value="')
        __M_writer(filters.decode.utf8(discussionname))
        __M_writer('"/>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t<input type="text" class="form-control floating-label" placeholder="Titel" name="title">\r\n\t</li>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t\r\n\t\t<textarea input type="text" class="form-control floating-label" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\t</li>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t<button type="submit" name="action" value="create" class="btn btn-primary btn-material-green btn-sm">Erstellen</button>\r\n\r\n\t</li>\r\n\r\n</ul>\r\n</div>\r\n</form>\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n<script>\r\nfunction ShowHide(id){\r\n\tif(document.getElementById(id).style.display == \'none\'){\r\n\t\tdocument.getElementById(id).style.display=\'block\';\r\n\t}else{\r\n\t\tdocument.getElementById(id).style.display = \'none\';\r\n\t}\r\n}\r\n\r\n</script>\t\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 2, "23": 2, "24": 3, "25": 3, "26": 7, "27": 7, "28": 7, "29": 7, "30": 8, "31": 8, "32": 12, "33": 13, "34": 14, "35": 14, "36": 20, "37": 20, "38": 25, "39": 25, "40": 29, "41": 29, "42": 35, "43": 36, "44": 37, "45": 37, "46": 38, "47": 38, "48": 39, "49": 39, "50": 40, "51": 40, "52": 48, "53": 48, "54": 49, "55": 49, "56": 50, "57": 50, "58": 52, "59": 52, "60": 57, "61": 57, "62": 68, "63": 75, "64": 76, "65": 77, "66": 79, "67": 84, "68": 84, "69": 85, "70": 85, "71": 119, "72": 119, "78": 72}, "filename": "templates/beitraege.html", "uri": "beitraege.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
