pip install python-calendarific

import calendarific

calapi = calendarific.v2('6981d02afb34fb0d7f67b5ad93491ab8283a7773')

parameters = {
	# Required
	'country': 'US',
	'year':    2019,
}

holidays = calapi.holidays(parameters)
