<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Uploadify Move the Queue Sample</title>

<link rel="stylesheet" href="uploadify/uploadify.css" type="text/css" />

<script type="text/javascript" src="js/jquery-1.3.2.min.js"></script>
<script type="text/javascript" src="js/jquery.uploadify.js"></script>

<script type="text/javascript">


$(document).ready(function() {
	$("#fileUpload").fileUpload({
		'uploader': 'uploadify/uploader.swf',
		'cancelImg': 'uploadify/cancel.png',
		'script': 'uploadify/upload.php',
		'folder': 'files',
		'multi': true,
		'displayData': 'percentage',

/*		onInit: function (){						
			$(this).css('display','none');
			if ($.browser.msie) {
				$(this).after('<div id="' + $(this).attr("id")  + 'Uploader"></div>');
				document.getElementById($(this).attr("id")  + 'Uploader').outerHTML = flashElement;
			} else {
				$(this).after(flashElement);
			}
			$("#customspot").after('<div id="' + $(this).attr('id') + 'Queue" class="fileUploadQueue"></div>');
			return false;
		}
*/	});
});

</script>
</head>

<body>
<div style="float:left">
     <fieldset style="border: 1px solid #CDCDCD; padding: 8px; padding-bottom:0px; margin: 8px 0; width:450px">
		<legend><strong>Upload Files - movedQueue Sample</strong></legend>
		<div id="fileUpload">You have a problem with your javascript</div>
		<a href="javascript:$('#fileUpload').fileUploadStart()">Start Upload</a> |  <a href="javascript:$('#fileUpload').fileUploadClearQueue()">Clear Queue</a>
    	<p></p>
    </fieldset>
</div> 
 <div style="float:left; margin-left:20px">
 	<div id="customspot"></div>
 </div>
</body>
</html>