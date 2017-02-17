class bcolors:
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'

def get_green_print(message):
	return bcolors.OKGREEN + message + bcolors.ENDC

def get_yellow_print(message):
	return bcolors.YELLOW + message + bcolors.ENDC

def get_blue_print(message):
	return bcolors.OKBLUE + message + bcolors.ENDC

def get_red_print(message):
	return bcolors.FAIL + message + bcolors.ENDC

def print_error(message):
	print get_red_print("ERROR: ") + message

def arguments_quantity_check(arguments):
	if len(arguments) < 2:
		print "To litte arguments"
		sys.exit(1)
