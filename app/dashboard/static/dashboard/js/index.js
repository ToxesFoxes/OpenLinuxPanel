// parent .card-body .row.system-stats
// element system-stat

// create jquery-ui sortable

$(function () {
	var systemStats = {
		items: ['cpu', 'memory','disk'],
	}
	$(".system-stats").sortable({
		items: ".system-stat",
		placeholder: "system-stat-placeholder",
		forcePlaceholderSize: true,
		opacity: 0.5,
		helper: "clone",
		axis: 'x',
		tolerance: "pointer",
		start: function (event, ui) {
			ui.placeholder.height(ui.item.height());
		},
		update: function (event, ui) {
			// update item, post to /system-stats/update
			// $.ajax({
			// 	url: '/system-stats/update',
			// 	type: 'POST',
			// 	data: {
			// 		'classlist': item.attr('class'),
			// 		'index': item_index
			// 	},
			// 	success: function (data) {
			// 		console.log(data);
			// 	}
			// });
			// update all, not only the item
			var items = $(".system-stats .system-stat");
			var order = [];
			items.each(function (i, e) {
				// find in classlist systemStats.items
				// as name
				var item = $(e);
				var classlist = item.attr('class').split(' ');
				var name = classlist.find(function (e) {
					return systemStats.items.indexOf(e) > -1;
				});
				order.push(name);
			});
			$.ajax({
				url: '/system-stats/update',
				type: 'POST',
				contentType: "application/json; charset=utf-8",
				traditional: true,
				data: JSON.stringify({
					'order': order
				}),
				success: function (data) {
					console.log(data);
				}
			});
		},
	});
});
// $(function () {
// 	$(".system-stats").sortable({
// 		containment: "parent",
// 		placeholder: "placeholder",
// 		opacity: 0.5,
// 		helper: "clone",
// 		axis: 'x',
// 		tolerance: "pointer",
// 		start: function (e, ui) {
// 			var ind_th = ui.item.index()
// 			// $('.system-stats').each(function (ind, el) {
// 			// 	$('div', el).eq(ind_th).addClass('drg').css('color', 'red')
// 			// })
// 		},
// 		stop: function (e, ui) {
// 			var itInd = ui.item.index()
// 			console.log("Col: " + itInd)
// 			$(".system-stat").each(function (ind, el) {
// 				var cell = $(".drg", el).detach()
// 				console.log("Row Len: " + $("div", el).length)
// 				if (itInd >= $("div", el).length) {
// 					cell.appendTo($(el))
// 				} else {
// 					cell.insertBefore($("div", el).eq(itInd))
// 				}
// 				cell.removeClass("drg").css("color", "black")
// 			})
// 		}
// 	})
// 	$(".system-stats").disableSelection()
// })