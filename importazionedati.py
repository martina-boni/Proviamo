pip install python-calendarific

import calendarific

calapi = calendarific.v2('6981d02afb34fb0d7f67b5ad93491ab8283a7773')

parameters = {
	# Required
	'country': 'IT',
	'year':    2019,
}

holidays = calapi.holidays(parameters)


def __init__(self, welcome_message()):
    self.message = welcome_message
    print "Welcome to your calendar :)"
    print self.message
        
def welcome():
    print "Welcome, " + USER_FIRST_NAME + "."
    print "Calendar starting..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "Current Time: " + strftime("%H: %M : %S")
    print "What would you like to do?" 
