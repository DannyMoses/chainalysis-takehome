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
			$.each(data, function(k,v) {
				var item = "#"+k;
				$(item).text("$" + v);
			});

			var min = _.min(Object.keys(data), function(o) { return data[o] });
			$("#recommendation").text("Recommended buy site: " + min);
		});
	}, 1000);

});
