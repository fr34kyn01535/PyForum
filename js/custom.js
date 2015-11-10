$(function(){
	$(".toggleButton").click(function(){
		var toToggle=$(this).attr("data-toggle");
		$( "#" +toToggle).toggle();
	});
});
