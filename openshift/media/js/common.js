openurl=function(url)
{


$('#pop').dialog({
                                autoOpen :false,
                                bgiframe :true,
                                modal :true,
                                resizable :false,
                                width :800,
                                height :400,
                                minHeight:100,
                                position : [ 'center', 'center' ],
                                draggable :true

                            });

                            alert(url);

    $.ajax
    (
    {
        type: "GET",
        url: url,
        data:"",
        success: function(msg)
        {
          alert(msg);
            $('#pop').removeClass("invisible");
            $('#pop').html(msg);

            $('#pop').dialog('open');

        }
    }
    );
}



function setContent(url,method)
{
      $.ajax
        (
        {
            type: method,
            url:url,
            data:'',
            success: function(msg)
            {
                $('#content').html(msg);
            }
            });
}


/**
 * function to show a confirmation message box
 * @param textMessage : the content to display in the box
 * @param yesFunction : the function to execute when click on yes
 * notice that you should have a div with ID=ConfirmDialog in the page and include jquery,jquery ui javascript
 * and ixedit sample css file
 */
showConfirm=function(textMessage,yesFunction)
{
	
	//alert(yesFunction);
	
	$('#divConfirmDialog').removeClass("invisible");
	$('#divConfirmDialog').html(textMessage);
	var target = jQuery('div#divConfirmDialog');
	
	if (!target.dialog('isOpen')) {
		target.dialog( {
			autoOpen :false,
			bgiframe :true,
			modal :true,
			resizable :false,
			width :200,
			height :100,
			minHeight:100,
			position : [ 'center', 'center' ],
			draggable :true,
			buttons:
			{
			"yes" :yesFunction,
			"no" :function()
				 {
				$(this).dialog("close");
				 }
			}

		})
	}
	;
	target.show();
	target.dialog('open');
}


/**
 * function to show a waiting message when a lenghty operation is laucnhed
 */


function initialiseWaiting()
{
   	var target = jQuery('div#waiting_message');
	//target.show();
	
		target.dialog
	  (
	  {
			autoOpen :false,
			bgiframe :true,
			modal :true,
			resizable :false,
			width :200,
			height :200,
			position : [ 'center', 'center' ],
			draggable :true

	 })
   
}
showWaiting=function(event, ui) 
{
	$('#waiting_message').removeClass("invisible");
	var target = jQuery('div#waiting_message');
	target.show();
	
	target.dialog('open');
};

//close the waiting message
closeWaiting=function(event, ui) 
{
	    	var target = jQuery('div#waiting_message');
                $('#waiting_message').addClass("invisible");
	    	target.dialog('close');
			
}

/**
 * function to show a message box
 * @param widthP : width of the box
 * @param heightP:height of the box
 * @param message : message to display in the box
 */
showPopup=function(withdP,heightP,delay,message)
		{
			$('#popMessage').removeClass("invisible");
			$('#popMessage').html(message);
			var target = jQuery('div#popMessage');
			target.show();
			if (!target.dialog('isOpen')) 
			{
				target.dialog(
				{
					autoOpen :false,
					bgiframe :true,
					modal :true,
					resizable :false,
					width :withdP,
					height :heightP,
					minHeight:heightP,
					position : [ 'center', 'center' ],
					draggable :true

				})
			}
			;
			target.dialog('open');
			
		}

//close a popup
closePopUp=function(delay)
{
			
	$("#popMessage").fadeOut
	(delay,
	    function()
		{
		  var target = jQuery('div#popMessage');
		  target.dialog('close');
		}
	);
			
}

 function datemmDDyyyy(strDate,separateur)
 {

	        day = strDate.substring(0,2);
		month = strDate.substring(3,5);
		year = strDate.substring(6,10);

                return month+separateur+day+year;
 }
 function getDate(strDate)
 {
   
	        day = strDate.substring(0,2);
		month = strDate.substring(3,5);
		year = strDate.substring(6,10);
		d = new Date();
		d.setDate(day);
		d.setMonth(month);
		d.setFullYear(year);
		return d;
}
 function compare(date_1, date_2){
	    diff = date_1.getTime()-date_2.getTime();
	    return (diff==0?diff:diff/Math.abs(diff));
	  }
