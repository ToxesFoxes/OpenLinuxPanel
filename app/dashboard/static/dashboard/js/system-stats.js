$(function () {
	var systemStats = {
		items: ['cpu', 'memory', 'disk'],
		edit: false,
		refresh: 5000,
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
			ui.placeholder.height(ui.item.height())
		},
		update: function (event, ui) {
			var items = $(".system-stats .system-stat")
			var data = []
			items.each(function (i, e) {
				var item = $(e)
				var classlist = item.attr('class').split(' ')
				var name = classlist.find(function (e) {
					return systemStats.items.indexOf(e) > -1
				})
				data.push({ name, order: i + 1, active: item.is(':visible') })
			})
			$.ajax({
				url: '/api/system-stats/order/',
				type: 'POST',
				contentType: "application/json; charset=utf-8",
				traditional: true,
				data: JSON.stringify(data),
				success: function (data) {
					console.log(data)
				}
			})
		},
	}).sortable("disable")
	$.ajax({
		url: '/api/system-stats/order/',
		type: 'GET',
		beforeSend: function (xhr) {
			xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
		},
		success: function (data) {
			console.log(data)
			data.forEach(function (e) {
				var item = $('<div class="system-stat ' + e.name + ' col-6 col-sm-3 col-md-3 col-lg-2 text-center" id="system-stat-' + e.name + '"></div>')
				var knob = $('<input type="text" class="knob" readonly data-linecap="round" data-thickness=".15" data-min="0"data-max="100" value="0" data-width="90" data-height="90" data-angleOffset="180" data-fgColor="#29D67A">')
				var label = $('<div class="knob-label">' + e.name + '</div>')
				item.append(knob)
				item.append(label)
				$(".system-stats").append(item)
				if (!e.active) {
					item.hide()
				}
				knob.knob({
					readOnly: true,
					format: function (value) {
						return value + '%'
					}
				})
			})
		}
	})

	const editSysStatsCardBtn = $(".card.system-stats-card button[data-card-widget='edit']")
	editSysStatsCardBtn.click(function () {
		systemStats.edit = !systemStats.edit
		if (systemStats.edit) {
			editSysStatsCardBtn.find('i').removeClass('fa-pen-to-square').addClass('fa-save')
			$(".card.system-stats-card").addClass('card-primary')
		} else {
			$(".card.system-stats-card").addClass('card-success')
			setTimeout(function () {
				editSysStatsCardBtn.find('i').addClass('fa-pen-to-square').removeClass('fa-save')
				$(".card.system-stats-card").removeClass('card-success card-primary')
			}, 1000)
		}
		$(".system-stats").sortable(systemStats.edit ? "enable" : "disable")
	})
})