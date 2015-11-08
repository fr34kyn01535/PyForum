# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446994350.0239832
_enable_loop = True
_template_filename = 'templates/beitraege.html'
_template_uri = 'beitraege.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(title=title,pageargs=pageargs,thema=thema)
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
            __M_writer('</div>\r\n    <div class="panel-body">\r\n       \r\n\t   \r\n\t   <div class="list-group">\r\n\t   \r\n   \t\t\t<p class="list-group-item-text datum">(')
            __M_writer(filters.decode.utf8(beitrag["Erstellt"]))
            __M_writer(')</p>\r\n\t\t\t<div class="list-group-item">\r\n\t\t\t\t\r\n\t\t\t\t<table class="table">\r\n\t\t\t\t\t<td style="width:100px;">\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
            __M_writer(filters.decode.utf8(beitrag["Ersteller"]))
            __M_writer('</p></i>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<div class="least-content"></div>\t\t\t\t\t\t\r\n\t\t\t\t\t\t<p class="list-group-item-text">')
            __M_writer(filters.decode.utf8(beitrag["Text"]))
            __M_writer('</p>\r\n\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</table>\r\n\t\t\t</div>\r\n\t\t\t<div class="list-group-separator"></div>\r\n')
            if role=="Administrator": 
                __M_writer('\t\t\t\t<form method="POST" action="/thema">\r\n\t\t\t\t<input type="hidden" name="thema" value="')
                __M_writer(filters.decode.utf8(thema))
                __M_writer('"/>\r\n\t\t\t\t<input type="hidden" name="discussionname" value="sollte der titel hin"/>\r\n\t\t\t\t<button style="float:right;" name="action" value="delete" class="btn btn-warning btn-xs"><i class="mdi-content-clear"></i></button>\r\n\t\t\t\t<button style="float:right;" name="action" value="edit" class="btn btn-primary btn-xs"><i class="mdi-content-create"></i></button>\r\n\t\t\t\t</form>\r\n')
            __M_writer('</div>\r\n\t   \r\n\t   \r\n\t   \r\n    </div>\r\n</div>\r\n')
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
{"filename": "templates/beitraege.html", "source_encoding": "utf-8", "line_map": {"16": 2, "23": 2, "24": 3, "25": 3, "26": 7, "27": 7, "28": 7, "29": 7, "30": 13, "31": 14, "32": 15, "33": 15, "34": 21, "35": 21, "36": 26, "37": 26, "38": 30, "39": 30, "40": 36, "41": 37, "42": 38, "43": 38, "44": 44, "45": 51, "46": 52, "47": 53, "48": 55, "49": 62, "50": 62, "51": 96, "52": 96, "58": 52}, "uri": "beitraege.html"}
__M_END_METADATA
"""
