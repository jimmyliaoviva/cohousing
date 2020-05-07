$(document).ready(function(){

	$('.like').hide();
	$('.unlike').show();

	$('.unlike').each(function () {
		$('#unlike').click(function () {
		$("#like").show();
		$("#unlike").hide();
		});
	});

	$('.like').each(function () {
		$('#like').click(function () {
		$("#unlike").show();
		$("#like").hide();
		});
	});




});

