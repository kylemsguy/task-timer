import time
from datetime import datetime

filename = "hours-marking.txt"
date_format = "%a %b %d %H:%M:%S %Z %Y"

start_time = 0
end_time = 0

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


def main():
	print("Writing start time to {0}...").format(filename)
	start_time = datetime.now()
	with open(filename, "a") as hoursfile:
		hoursfile.write("Start time: ")
		hoursfile.write(time.strftime(date_format))
		hoursfile.write('\n')

	print("Waiting until you finish your marking session.")
	print("When you are done, either press Ctrl-C or simply log off of the SSH connection.")

	while(True): pass # hang until user quits


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Writing end time...")
		write_end_time()