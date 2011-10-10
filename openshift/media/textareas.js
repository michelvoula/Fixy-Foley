tinyMCE.init({
    mode: "textareas",
    
    editor_selector: "mceEditor",
    theme: "advanced",
	plugins:"preview,autolink,lists,pagebreak,style,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,inlinepopups,autosave",
    skin: "cirkuit",
	extended_valid_elements : "script[type|src],iframe[src|style|width|height|scrolling|marginwidth|marginheight|frameborder],",
    
    theme_advanced_buttons1: "preview,autosave,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
    theme_advanced_buttons2: "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,cleanup,help,code,|,insertdate,inserttime,|,forecolor,backcolor",
    theme_advanced_buttons3: "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,advhr,|,fullscreen",
    theme_advanced_toolbar_location: "top",
    theme_advanced_toolbar_align: "left",
    theme_advanced_statusbar_location: "bottom",
    theme_advanced_resizing: true,
    
    // Example content CSS (should be your site CSS)
    content_css: "css/content.css",
    
    // Drop lists for link/image/media/template dialogs
    template_external_list_url: "lists/template_list.js",
    external_link_list_url: "lists/link_list.js",
    external_image_list_url: "lists/image_list.js",
    media_external_list_url: "lists/media_list.js",

});
