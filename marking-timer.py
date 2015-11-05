#!/usr/bin/env python3
import time
import signal
from datetime import datetime

filename = "hours-marking.txt"
date_format = "%a %b %d %H:%M:%S %Z %Y"

start_time = 0

def sighup_handler(signum, frame):
	write_end_time()

def write_start_time():
	global start_time
	print("Writing start time to {0}...").format(filename)
	start_time = datetime.now()
	with open(filename, "a") as hoursfile:
		hoursfile.write("Start time: ")
		hoursfile.write(time.strftime(date_format))
		hoursfile.write('\n')

def write_end_time():
	print("Writing end time to {0}...").format(filename)
	end_time = datetime.now()
	time_marked = end_time - start_time
	with open(filename, "a") as hoursfile:
		hoursfile.write("End time: ")
		hoursfile.write(time.strftime(date_format))
		hoursfile.write('\n')
		hoursfile.write("Total time marked: ")
		hoursfile.write(str(time_marked).split('.')[0])
		hoursfile.write("\n\n")

if __name__ == "__main__":
	write_start_time()
	# Set up SIGHUP handler
	signal.signal(signal.SIGHUP, sighup_handler)
	try:
		print("Waiting until you finish your marking session.")
		print("When you are done, either press Ctrl-C or simply log off of the SSH connection.")
		while(True): pass # hang until user quits
	except KeyboardInterrupt:
		print("Writing end time...")
		write_end_time()