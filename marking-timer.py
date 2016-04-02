#!/usr/bin/env python3
import sys
import time
import signal
from datetime import datetime

filename = "hours-marking.txt"
date_format = "%a %b %d %H:%M:%S %Z %Y"

start_time = 0

def sighandler(signum, frame):
    write_end_time()
    quit()

def write_start_time():
    global start_time
    sys.stderr.write("Writing start time to {0}...\n".format(filename))
    start_time = datetime.now()

    sys.stdout.write("Start time: ")
    sys.stdout.write(time.strftime(date_format))
    sys.stdout.write('\n')

def write_end_time():
    sys.stderr.write("Writing end time to {0}...\n".format(filename))
    end_time = datetime.now()
    time_marked = end_time - start_time

    sys.stdout.write("End time: ")
    sys.stdout.write(time.strftime(date_format))
    sys.stdout.write('\n')
    sys.stdout.write("Total time marked: ")
    sys.stdout.write(str(time_marked).split('.')[0])
    sys.stdout.write("\n\n")
    sys.stderr.write("Total time marked: {}\n".format(str(time_marked).split('.')[0]))

if __name__ == "__main__":
    sys.stdout = open(filename, "a")
    write_start_time()
    # Set up SIGHUP handler
    signal.signal(signal.SIGHUP, sighandler)
    signal.signal(signal.SIGTERM, sighandler)
    signal.signal(signal.SIGINT, sighandler)
    signal.signal(signal.SIGABRT, sighandler)
    signal.signal(signal.SIGQUIT, sighandler)

    sys.stderr.write("Waiting until you finish your marking session.\n")
    sys.stderr.write("When you are done, press Ctrl-C.\n")
    #sys.stderr.write("When you are done, either press Ctrl-C, or simply end the SSH connection.\n")
    # hang until user quits
    counter = 0
    spinner = ('-', '\\', '|', '/')
    while True:
        counter += 1
        end_time = datetime.now()
        time_marked = end_time - start_time
        sys.stderr.write("                                                  \r")
        sys.stderr.write("Time marked so far: {} {}\r".format(str(time_marked).split('.')[0], spinner[counter % len(spinner)]))
        #time.sleep(1000000)
        #time.sleep(300)
        #time.sleep(1)
        time.sleep(0.5)
