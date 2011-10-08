<style type="text/css">
body {
	font: 0.8em/1.6em Arial, Helvetica, sans-serif;
}
fieldset {
	width: 500px;
}

#sample {
	display:table;
}
#sampleFile {
	float: left;
	display:table-cell;
	margin-right: 15px;
}
#download {
	margin-top: 15px;
	display: table;
}
.dlImage {
	display: table-cell;
	float: left;
	margin-right: 10px;
}
.dlText {
	float: left;
	display: table-cell;
}
.fileDetails {
	color: red;
}
.releaseDate{
	margin-top: -3px;
	color: gray;
}
</style>


<div id="sample">
<div id="sampleFile">
<?php include_once('uploadify-multi-single.php');
$scriptDataFile = 'downloads/Uploadify multi-single sample.zip'; ?>
</div>
<div id="download">
  <div class="dlImage">
	<a href="<?= $scriptDataFile ?>"><img src="css/images/dload.gif" alt="Download"/></a>
  </div>
  <div class="dlText">
	<div class="fileDetails">Uploadify multi-single sample.zip (<?= round(filesize($scriptDataFile)/1024, 2) ?>KB)</div>
	<div class="releaseDate">Released March 10, 2009</div>
  </div>
</div>
</div>

<div id="sample">
<div id="sampleFile">
<?php include_once('uploadify-scriptData.php');
$scriptDataFile = 'downloads/Uploadify scriptData sample.zip'; ?>
</div>
<div id="download">
  <div class="dlImage">
	<a href="<?= $scriptDataFile ?>"><img src="css/images/dload.gif" alt="Download"/></a>
  </div>
  <div class="dlText">
	<div class="fileDetails">Uploadify scriptData sample.zip (<?= round(filesize($scriptDataFile)/1024, 2) ?>KB)</div>
	<div class="releaseDate">Released March 10, 2009</div>
  </div>
</div>
</div>


<div id="sample">
<div id="sampleFile">
<?php include_once('uploadify-style.php');
$scriptDataFile = 'downloads/Uploadify style sample.zip'; ?>
</div>
<div id="download">
  <div class="dlImage">
	<a href="<?= $scriptDataFile ?>"><img src="css/images/dload.gif" alt="Download"/></a>
  </div>
  <div class="dlText">
	<div class="fileDetails">Uploadify style sample.zip (<?= round(filesize($scriptDataFile)/1024, 2) ?>KB)</div>
	<div class="releaseDate">Released March 10, 2009</div>
  </div>
</div>
</div>

<div id="sample">
<div id="sampleFile">
<?php include_once('uploadify-jgrowl.php');
$jGrowlFile = 'downloads/Uploadify jGrowl sample.zip'; ?>
</div>
<div id="download">
  <div class="dlImage">
	<a href="<?= $jGrowlFile ?>"><img src="css/images/dload.gif" alt="Download"/></a>
  </div>
  <div class="dlText">
	<div class="fileDetails">Uploadify jGrowl sample.zip (<?= round(filesize($jGrowlFile)/1024, 2) ?>KB)</div>
	<div class="releaseDate">Released March 10, 2009</div>
  </div>
</div>
</div>