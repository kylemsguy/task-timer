#!/usr/bin/env python3
import datetime

def parse_time(timestr):
    time_split = timestr.split(":")
    timedelta = datetime.timedelta(hours=int(time_split[0]), minutes=int(time_split[1]), seconds=int(time_split[2]))
    return timedelta


def main():
    totalcount = datetime.timedelta()
    with open("hours-marking.txt", 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            if "Total time marked:" in line:
                time_raw = line.split(" ")[3]
                timedelta = parse_time(time_raw)
                totalcount += timedelta
    print(str(totalcount).split('.')[0])
if __name__ == "__main__":
    main()
