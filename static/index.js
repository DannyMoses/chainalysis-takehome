console.log("js loaded");

$(document).ready( function()  {
	
	var selectedCrypto = "BTC";

	$(".dropdown-menu li a").click( function()  {
		$(this).parents(".dropdown").find(".btn").html($(this).text() + ' <span class="caret"></span>');
		$(this).parents(".dropdown").find('.btn').val($(this).data('value'));
		selectedCrypto = $(this).parents(".dropdown").find('.btn').val();
	});

	
	setInterval(function() {
		$.get('/update/' + selectedCrypto, function(data, status){
			console.log(data);
			$("#blockchainData").text("$" + data["blockchain"]);
			$("#geminiData").text("$" + data["gemini"]);
			if (data["blockchain"] <= data["gemini"]) {
				$("#recommendation").text("Recommened buy site: " + "Blockchain");
			} else {
				$("#recommendation").text("Recommened buy site: " + "Gemini");
			}
		});
	}, 1000);

});
