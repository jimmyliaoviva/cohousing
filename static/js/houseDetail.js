$(document).ready(function(){
	$("#likeBtn").hide();
	
	$("#unlikeBtn").click(function() { $("#likeBtn").show(); $("#unlikeBtn").hide(); });
	$("#likeBtn").click(function() { $("#unlikeBtn").show(); $("#likeBtn").hide(); });
	
	$("#topBtn").click(function() {	topFunction(); });
});
function topFunction() {
	$(".detailPage").scrollTop(0);
}