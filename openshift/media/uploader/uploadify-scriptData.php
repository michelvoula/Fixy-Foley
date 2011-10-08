<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Uploadify scriptData Sample</title>

<link rel="stylesheet" href="uploadify/uploadify.css" type="text/css" />

<script type="text/javascript" src="js/jquery-1.3.2.min.js"></script>
<script type="text/javascript" src="js/jquery.uploadify.js"></script>

<script type="text/javascript">
function startUpload(id, conditional)
{
	if(conditional.value.length != 0) {
		$('#'+id).fileUploadStart();
	} else
		alert("You must enter your name. Before uploading");
}
</script>
<script type="text/javascript">


$(document).ready(function() {
	$("#fileUploadname").fileUpload({
		'uploader': 'uploadify/uploader.swf',
		'cancelImg': 'uploadify/cancel.png',
		'script': 'uploadify/upload_name.php',
		'folder': 'files',
		'multi': false,
		'displayData': 'percentage',
		onComplete: function (evt, queueID, fileObj, response, data) {
			alert("Successfully uploaded: "+response);
		}
	});

	$("#fileUploadname2").fileUpload({
		'uploader': 'uploadify/uploader.swf',
		'cancelImg': 'uploadify/cancel.png',
		'script': 'uploadify/upload_name.php',
		'folder': 'files',
		'multi': true,
		'displayData': 'percentage',
		'scriptData': {'name':'JohnDoe'}, // If the value is known to php you can also enter it here ie < ?= $value ?> or < ?= $_RESULT['value'] ?>
		onComplete: function (evt, queueID, fileObj, response, data) {
			alert("Successfully uploaded: "+response);
		}
	});

	$("#fileUploadname3").fileUpload({
		'uploader': 'uploadify/uploader.swf',
		'cancelImg': 'uploadify/cancel.png',
		'script': 'uploadify/upload_name.php',
		'folder': 'files',
		'multi': true,
		'displayData': 'percentage',
		'scriptData': {'name':'JohnDoe', 'location':'Australia'}, 
		onComplete: function (evt, queueID, fileObj, response, data) {
			alert("Successfully uploaded: "+response);
		}
	});

	$('#name').bind('change', function(){
		$('#fileUploadname').fileUploadSettings('scriptData','&name='+$(this).val());
	});
	$('#name2').bind('change', function(){
		$('#fileUploadname2').fileUploadSettings('scriptData','&name='+$(this).val());
	});

	// When setting scriptData you must enter the full parameter string. More checks need to be done in this case
	// because what you will experience is if you enter a name it will wipe location:Australia unless Australia is
	// written in the location field. The same applies visa versa, the only difference is there is an "isEmpty" check
	// on the name field.
	$('#name3').bind('change', function(){
		$('#fileUploadname3').fileUploadSettings('scriptData','&name='+$(this).val()+'&location='+$('#location').val());
	});
	$('#location').bind('change', function(){
		$('#fileUploadname3').fileUploadSettings('scriptData','&name='+$('#name3').val()+'&location='+$(this).val());
	});

});

</script>
</head>

<body>
      <fieldset style="border: 1px solid #CDCDCD; padding: 8px; padding-bottom:0px; margin: 8px 0">
		<legend><strong>Upload Files - scriptData Sample with Response</strong></legend>
				<p>Name is not known at execution of this file.</p>
				<strong>Name:  </strong>
                <input name="name" id="name" type="text" maxlength="255" size="50" />
                <br /><br />
		<div id="fileUploadname">You have a problem with your javascript</div>
		<a href="javascript:startUpload('fileUploadname', document.getElementById('name'))">Start Upload</a> |  <a href="javascript:$('#fileUploadname').fileUploadClearQueue()">Clear Queue</a>
    	<p></p>
<hr width=100% size="1" color="" align="center">
				<p>Name is known at execution of this file, but can be overridden.</p>
				<strong>Name:  </strong>
				<!-- Adding the value="John Doe" does not update the scriptData. It purley gives startUpload() something to pass in the conditional,
				and if the user deletes the name it will still trigger the alert -->
                <input name="name2" id="name2" type="text" maxlength="255" size="50" value="John Doe"/>
                <br /><br />
		<div id="fileUploadname2">You have a problem with your javascript</div>
		<a href="javascript:startUpload('fileUploadname2', document.getElementById('name2'))">Start Upload</a> |  <a href="javascript:$('#fileUploadname2').fileUploadClearQueue()">Clear Queue</a>
    	<p></p>
<hr width=100% size="1" color="" align="center">
				<p>Multiple scriptData Inputs</p>
				<strong>Name:  </strong>
				<!-- Adding the value="John Doe" does not update the scriptData. It purley gives startUpload() something to pass in the conditional,
				and if the user deletes the name it will still trigger the alert -->
                <input name="name3" id="name3" type="text" maxlength="255" size="50" value="John Doe"/>
                <br /><br/>
                <!-- You can see how not using value="Australia" here that scriptData with a predefined value still works. Enter something in the
                field and it'll update the location -->
				Try leaving this blank first. Then try just changing the name, Now enter a location. Read the comments on the file to find out what's happening<br>
                <strong>Location:  </strong>
                <input name="location" id="location" type="text" maxlength="255" size="50" /> 
                <br /><br />
		<div id="fileUploadname3">You have a problem with your javascript</div>
		<a href="javascript:startUpload('fileUploadname3', document.getElementById('name3'))">Start Upload</a> |  <a href="javascript:$('#fileUploadname3').fileUploadClearQueue()">Clear Queue</a>
    	<p></p>
    </fieldset>
</body>
</html>