openurl = function(url, w, h){


    /*$('#popup').dialog({
     autoOpen :false,
     bgiframe :true,
     modal :true,
     resizable :false,
     width :w,
     height :h,
     minHeight:100,
     position : [ 'center', 'center' ],
     draggable :true
     });
     //        alert(url);*/
    $.ajax({
        type: "GET",
        url: url,
        data: "",
        success: function(msg){
            //alert(msg);
            $('#popup').removeClass("invisible");
            $('#popup').html(msg);
            
            //$('#popup').dialog('open');
        
        }
    });
}

insertPhoto = function(spanId){
    val1 = $('#pop').html() + $('#' + spanId).html(msg);
    $('#pop').html(val1);
}
function updateContent(win, newId, newRepr){
    // newId and newRepr are expected to have previously been escaped by
    // django.utils.html.escape.
    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    
    var name = windowname_to_id(win.name);
    alert(newRepr);
    var elem = document.getElementById('id_str_post_content');
    if (elem) {
    
	    tinyMCE.triggerSave();
       
		var content=$('#id_str_post_content').val()+newRepr;
		tinyMCE.getInstanceById('id_str_post_content').setContent(content);
       // tinyMCE.activeEditor.setContent(newRepr);
		 tinyMCE.get('id_str_post_content').focus();
        // elem.value +=newRepr;      
    }
    win.close();
}
