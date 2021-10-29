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
			///$("#Blockchain").text("$" + data["blockchain"]);
			///$("#Gemini").text("$" + data["gemini"]);
			if (data["Blockchain"] <= data["Gemini"]) {
				$("#recommendation").text("Recommened buy site: " + "Blockchain");
			} else {
				$("#recommendation").text("Recommened buy site: " + "Gemini");
			}

			$.each(data, function(k,v) {
				var item = "#"+k;
				console.log(item);
				$(item).text("$" + v);
			});
		});
	}, 1000);

});
