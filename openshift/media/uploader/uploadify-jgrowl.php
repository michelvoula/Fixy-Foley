<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Uploadify with jGrowl Sample</title>

<link rel="stylesheet" href="uploadify/uploadify.css" type="text/css" />
<link rel="stylesheet" href="css/uploadify.jGrowl.css" type="text/css" />

<script type="text/javascript" src="js/jquery-1.3.2.min.js"></script>
<script type="text/javascript" src="js/jquery.uploadify.js"></script>
<script type="text/javascript" src="js/jquery.jgrowl_minimized.js"></script>

<script type="text/javascript">

$(document).ready(function() {
	$('#name2').bind('change', function(){
		$('#fileUploadgrowl').fileUploadSettings('scriptData','&name='+$(this).val());
	});
	$("#fileUploadgrowl").fileUpload({
		'uploader': 'uploadify/uploader.swf',
		'cancelImg': 'uploadify/cancel.png',
		'script': 'uploadify/upload_name.php',
		'folder': 'files',
		'fileDesc': 'Image Files',
		'fileExt': '*.jpg;*.jpeg;*.png;*.gif',
		'multi': true,
		'simUploadLimit': 3,
		'sizeLimit': 1048576,
		'scriptData': {'name':'JohnDoe'}, 
		onError: function (event, queueID ,fileObj, errorObj) {
			var msg;
			if (errorObj.status == 404) {
				alert('Could not find upload script. Use a path relative to: '+'<?= getcwd() ?>');
				msg = 'Could not find upload script.';
			} else if (errorObj.type === "HTTP")
				msg = errorObj.type+": "+errorObj.status;
			else if (errorObj.type ==="File Size")
				msg = fileObj.name+'<br>'+errorObj.type+' Limit: '+Math.round(errorObj.sizeLimit/1024)+'KB';
			else
				msg = errorObj.type+": "+errorObj.text;
			$.jGrowl('<p></p>'+msg, {
				theme: 	'error',
				header: 'ERROR',
				sticky: true
			});			
			$("#fileUploadgrowl" + queueID).fadeOut(250, function() { $("#fileUploadgrowl" + queueID).remove()});
			return false;
		},
		onCancel: function (a, b, c, d) {
			var msg = "Cancelled uploading: "+c.name;
			$.jGrowl('<p></p>'+msg, {
				theme: 	'warning',
				header: 'Cancelled Upload',
				life:	4000,
				sticky: false
			});
		},
		onClearQueue: function (a, b) {
			var msg = "Cleared "+b.fileCount+" files from queue";
			$.jGrowl('<p></p>'+msg, {
				theme: 	'warning',
				header: 'Cleared Queue',
				life:	4000,
				sticky: false
			});
		},
		onComplete: function (a, b ,c, d, e) {
			var size = Math.round(c.size/1024);
			$.jGrowl('<p></p>'+c.name+' - '+size+'KB', {
				theme: 	'success',
				header: 'Upload Complete',
				life:	4000,
				sticky: false
			});
		}
	});
});

</script>
</head>

<body>
    <fieldset style="border: 1px solid #CDCDCD; padding: 8px; padding-bottom:0px; margin: 8px 0">
		<legend><strong>Upload Files - Growl Sample</strong></legend>
		<input name="name3" id="name3" type="text" maxlength="255" size="50" value="John Doe"/>
		<p>File Size Limited to 1Mb. Also try cancelling an upload.</p>
		<div id="fileUploadgrowl">You have a problem with your javascript</div>
		
		<a href="javascript:$('#fileUploadgrowl').fileUploadStart()">Start Upload</a> |  <a href="javascript:$('#fileUploadgrowl').fileUploadClearQueue()">Clear Queue</a>
    	<p></p>
    </fieldset>
</body>
</html>