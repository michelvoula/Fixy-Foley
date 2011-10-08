<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Uploadify scriptData Sample</title>

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
		'multi': false,
		'displayData': 'speed'
	});

	$("#fileUpload2").fileUpload({
		'uploader': 'uploadify/uploader.swf',
		'cancelImg': 'uploadify/cancel.png',
		'script': 'uploadify/upload.php',
		'folder': 'files',
		'multi': true,
		'buttonText': 'Select Files',
		'checkScript': 'uploadify/check.php',
		'displayData': 'speed',
		'simUploadLimit': 2
	});

	$("#fileUpload3").fileUpload({
		'uploader': 'uploadify/uploader.swf',
		'cancelImg': 'uploadify/cancel.png',
		'script': 'uploadify/upload.php',
		'folder': 'files',
		'fileDesc': 'Image Files',
		'fileExt': '*.jpg;*.jpeg;*.gif;*.png',
		'multi': true,
		'auto': true
	});
});

</script>
</head>

<body>
      <fieldset style="border: 1px solid #CDCDCD; padding: 8px; padding-bottom:0px; margin: 8px 0">
		<legend><strong>Uploadify - Single and Multiple Sample</strong></legend>
		<h2>Single File Upload</h2>
		<p>Display speed</p>
		<div id="fileUpload">You have a problem with your javascript</div>
		<a href="javascript:$('#fileUpload').fileUploadStart()">Start Upload</a> |  <a href="javascript:$('#fileUpload').fileUploadClearQueue()">Clear Queue</a>
    	<p></p>
<hr width=100% size="1" color="" align="center">
		<h2>Multiple File Upload</h2>
		<p>checkScript, buttonText, simulataneous upload limit</p>
		<div id="fileUpload2">You have a problem with your javascript</div>
		<a href="javascript:$('#fileUpload2').fileUploadStart()">Start Upload</a> |  <a href="javascript:$('#fileUpload2').fileUploadClearQueue()">Clear Queue</a>
    	<p></p>
<hr width=100% size="1" color="" align="center">
		<h2>Multiple File Auto Upload</h2>
		<p>Images Only</p>
		<div id="fileUpload3">You have a problem with your javascript</div>
		<a href="javascript:$('#fileUpload3').fileUploadStart()">Start Upload</a> |  <a href="javascript:$('#fileUpload3').fileUploadClearQueue()">Clear Queue</a>
    	<p></p>
    </fieldset>
</body>
</html>