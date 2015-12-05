# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449339697.0882835
_enable_loop = True
_template_filename = 'templates/diskussionen.html'
_template_uri = 'diskussionen.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,title,thema,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,title=title,thema=thema)
        role = context.get('role', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        runtime._include_file(context, 'header.html', _template_uri, title=title)
        __M_writer('\r\n\r\n<ul class="breadcrumb" style="margin-bottom: 5px;">\r\n    <li><a href="/">Startseite</a></li> \t\r\n    <li class="active">')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('</li>   \r\n</ul>\r\n<br/>\r\n\r\n<script type="text/javascript">\r\n\r\n\t$(function(){\r\n\t\t$("#newDiscussionButton").click(function(){\r\n\t\t\t$("#discussionContainer").html("Lade...");\r\n\t\t\t\r\n\t\t\tvar title = $(\'#newDiscussion input[name="title"]\').val();\r\n\t\t\tvar text = $(\'#newDiscussion textarea[name="text"]\').val();\r\n\t\t\t\r\n\t\t\tvar data = {"thema":"')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('","title":title,"text":text,"action":"create"};\r\n\t\t\r\n\t\t\t$.ajax({\r\n\t\t\t  type: "POST",\r\n\t\t\t  url: "/diskussionen",\r\n\t\t\t  data: data,\r\n\t\t\t  success: function(response,textStatus,jqXHR){\r\n\t\t\t\t\t$("#discussionContainer").html(response);\r\n\t\t\t\t\tbindDiscussionEvents();\r\n\t\t\t  },\r\n\t\t\t  complete: function(jqXHR,textStatus){\r\n\t\t\t\t$(\'#newDiscussion\').modal(\'hide\');\r\n\t\t\t  },\r\n\t\t\t  error: function(jqXHR,textStatus,thrownError) {\t\t\r\n\t\t\t\t\t$("#discussionContainer").html("Ajax Fehler: "+thrownError);\r\n\t\t\t\t},\r\n\t\t\t  dataType: "html"\r\n\t\t\t});\r\n\t\t\r\n\t\t});\r\n\t\tbindDiscussionEvents();\r\n\t\t$(document).ajaxError(function(e, request, settings,thrownError ) {\r\n\t\t\tconsole.log("Ajax Error: "+thrownError);\r\n\t\t});\r\n\t});\r\n\r\n\tfunction bindDiscussionEvents(){\r\n\t\t$(\'.deleteDiscussion\').click(function(){\r\n\t\t\t\tvar id = $(this).val();\r\n\t\t\t\tvar data = {"thema":"')
        __M_writer(filters.decode.utf8(thema))
        __M_writer('","id":id,"action":"delete"};\r\n\t\t\t\t\t\r\n\t\t\t\t$.ajax({\r\n\t\t\t\t  type: "POST",\r\n\t\t\t\t  url: "/diskussionen",\r\n\t\t\t\t  data: data,\r\n\t\t\t\t  success: function(response,textStatus,jqXHR){\r\n\t\t\t\t\t\t$("#discussionContainer").html(response);\r\n\t\t\t\t\t\tbindDiscussionEvents();\r\n\t\t\t\t  },error: function(jqXHR,textStatus,thrownError) {\t\t\r\n\t\t\t\t\t\t$("#discussionContainer").html("Ajax Fehler: "+thrownError);\r\n\t\t\t\t\t},\r\n\t\t\t\t  dataType: "html"\r\n\t\t\t\t});\r\n\t\t\t});\r\n\t};\r\n</script>\r\n\r\n<div id="newDiscussion" class="modal fade">\r\n\t  <div class="modal-dialog">\r\n\t\t<div class="modal-content">\r\n\t\t  <div class="modal-header">\r\n\t\t\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>\r\n\t\t\t<h4 class="modal-title">Neue Diskussion</h4>\r\n\t\t  </div>\r\n\t\t  <div class="modal-body">\r\n\t\t\t\r\n\t\t\t<input type="text" class="form-control floating-label" required="required" placeholder="Titel" name="title">\r\n\t<br/>\r\n\t\t\t<textarea class="form-control floating-label" required="required" placeholder="Text" name="text" style="height:180px"></textarea>\r\n\t\t  </div>\r\n\t\t  <div class="modal-footer">\r\n\t\t\t<button type="button" class="btn btn-default" data-dismiss="modal">Abbrechen</button>\r\n\t\t\t<button id="newDiscussionButton" type="button" name="action" value="create" class="btn btn-primary">Erstellen</button>\r\n\t\t  </div>\r\n\t\t</div>\r\n\t  </div>\t\r\n\t</div>\r\n\r\n')
        if role=="Administrator" or role=="Bearbeiter": 	 
            __M_writer('\r\n<button style="float:right;" type="button" class="btn btn-primary" data-toggle="modal" data-target="#newDiscussion">Neue Diskussion</button>\r\n\r\n\r\n')
        __M_writer('\r\n<div style="clear:both;"></div>\r\n\r\n<br/>\r\n\r\n<div class="panel panel-default">\r\n    <div class="panel-heading">Diskussionen</div>\r\n    <div class="panel-body">\r\n       \r\n\t   <div id="discussionContainer" class="list-group">\r\n\t   ')
        runtime._include_file(context, 'diskussionen-liste.html', _template_uri)
        __M_writer('\r\n</div>\r\n\t   \r\n \r\n\t   \r\n    </div>\r\n</div> \r\n\r\n')
        runtime._include_file(context, 'footer.html', _template_uri)
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "diskussionen.html", "line_map": {"32": 89, "33": 94, "34": 104, "35": 104, "36": 112, "37": 112, "43": 37, "16": 2, "22": 2, "23": 3, "24": 3, "25": 7, "26": 7, "27": 20, "28": 20, "29": 49, "30": 49, "31": 88}, "source_encoding": "utf-8", "filename": "templates/diskussionen.html"}
__M_END_METADATA
"""
