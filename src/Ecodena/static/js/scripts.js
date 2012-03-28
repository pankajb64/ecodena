$(document).ready(function(){
	$(".arrow").click(function(){
		$(".dropdown").toggle();
	});
	
	$(".searchbar").focus(function(){
		$(".searchicon").hide();
		$(".searchiconhover").show();
	},function(){
		$(".searchiconhover").hide();
		$(".searchicon").show();
	});
});
