# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446991583.1417265
_enable_loop = True
_template_filename = 'templates/beitraege.html'
_template_uri = 'beitraege.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(title=title,thema=thema,pageargs=pageargs)
        beitraege = context.get('beitraege', UNDEFINED)
        role = context.get('role', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li>\r\n    <li><a href="/thema?thema=')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('">')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('</a></li>\r\n\r\n       \r\n</ul>\r\n<br/>\r\n\r\n')
        for beitrag in beitraege:
            __M_writer('<div class="panel panel-default beitrag">\r\n    <div class="panel-heading">')
            __M_writer(filters.decode.utf8(beitrag["Titel"]))
            __M_writer('</div>\r\n    <div class="panel-body">\r\n       \r\n\t   \r\n\t   <div class="list-group">\r\n\t   \r\n    \r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t\r\n\t\t\t\t<div class="row-action-primary">\r\n\t\t\t\t\t<p class="list-group-item-text">')
            __M_writer(filters.decode.utf8(beitrag["Ersteller"]))
            __M_writer('</p></i>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="row-content">\r\n\t\t\t\t\t<div class="least-content"></div>\t\t\t\t\t\t\r\n\t\t\t\t\t<p class="list-group-item-text">')
            __M_writer(filters.decode.utf8(beitrag["Text"]))
            __M_writer('</p>\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\t<p class="list-group-item-text datum">(')
            __M_writer(filters.decode.utf8(beitrag["Erstellt"]))
            __M_writer(')</p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<div class="list-group-separator"></div>\r\n\t\t\t\r\n\r\n</div>\r\n\t   \r\n\t   \r\n\t   \r\n    </div>\r\n</div>\r\n')
        __M_writer('\r\n')
        if role=="Administrator" or role=="Bearbeiter":
            __M_writer('<button onclick="ShowHide()" style="float:right;" class="btn btn-fab btn-raised btn-material-green btn-xs"><i class="mdi-content-add"></i></button>\r\n')
        __M_writer('<div style="clear:both;"></div>\r\n\r\n<form method="POST" action="/thema">\r\n\r\n\r\n<div id="HiddneDiv" style="DISPLAY: none">\r\n<ul class="wmfg_questions">\r\n\t<input type="hidden" name="thema" value="')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('"/>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t<input type="text" class="form-control floating-label" placeholder="Titel" name="discussionname">\r\n\t</li>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t\r\n\t\t<textarea input type="text" class="form-control floating-label" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\t</li>\r\n\r\n\t<li class="wmfg_q">\r\n\t\t<button type="submit" name="action" value="create" class="btn btn-primary btn-material-green btn-sm">Erstellen</button>\r\n\r\n\t</li>\r\n\r\n</ul>\r\n</div>\r\n</form>\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n<script>\r\nfunction ShowHide(){\r\n\tif(document.getElementById("HiddneDiv").style.display == \'none\'){\r\n\t\tdocument.getElementById("HiddneDiv").style.display=\'block\';\r\n\t}else{\r\n\t\tdocument.getElementById("HiddneDiv").style.display = \'none\';\r\n\t}\r\n}\r\n\r\n</script>\t\r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/beitraege.html", "line_map": {"16": 2, "23": 2, "24": 3, "25": 3, "26": 7, "27": 7, "28": 7, "29": 7, "30": 13, "31": 14, "32": 15, "33": 15, "34": 25, "35": 25, "36": 29, "37": 29, "38": 31, "39": 31, "40": 44, "41": 45, "42": 46, "43": 48, "44": 55, "45": 55, "46": 89, "47": 89, "53": 47}, "source_encoding": "utf-8", "uri": "beitraege.html"}
__M_END_METADATA
"""
