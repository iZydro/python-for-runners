#!python

import sys
from unidecode import unidecode
from datetime import datetime, timedelta

def read_results(file_name, vector_name):
	for line in open(file_name, "r"):
		line = line.strip()
		runner_time = line.split(" | ")

		runner_time[0] = runner_time[0].replace(chr(0xa0), " ")
		runner_time[0] = runner_time[0].replace(chr(0xc2), "")
		runner_time[0] = unidecode(runner_time[0].decode("unicode-escape").lower())

		if runner_time[1][0] == "0":
			runner_time[1] = runner_time[1][1:]

		vector_name.append(runner_time)

def divide_time(my_time, total):
	result = {}
	seconds = my_time.second + my_time.minute * 60 + my_time.hour * 3600 + (my_time.day - 1) * 3600 * 24
	div = seconds / total
	hours = int(div/3600)
	minutes = int((div - hours*3600) / 60)
	seconds = div - hours*3600 - minutes*60
	result["hours"] = str(hours)
	if minutes < 10:
		result["minutes"] = "0" + str(minutes)
	else:
		result["minutes"] = str(minutes)
	if seconds < 10:
		result["seconds"] = "0" + str(seconds)
	else:
		result["seconds"] = str(seconds)
	return result

# Code starts here!

if len(sys.argv) < 3:
	print "Please enter the races to compare!"
	sys.exit()

race1 = sys.argv[1]
race2 = sys.argv[2]

# BCN = 1, MAD = 2

mad = []
bcn = [] 
read_results(race1 + ".txt", bcn)
read_results(race2 + ".txt", mad)

race1name = race1.upper()
race2name = race2.upper()

num_mad = len(mad)
num_bcn = len(bcn)

cnt_tot = 0
bcn_faster = 0
mad_faster = 0
init_diff = datetime.strptime("0:00:00", "%H:%M:%S")
total_diff = init_diff
total_mad = init_diff
total_bcn = init_diff

for madrid in mad:
	runner_mad = str(madrid[0])
	for barcelona in bcn:
		runner_bcn = barcelona[0]
		if runner_mad == runner_bcn:
			result1 = str(cnt_tot + 1) + ": " + runner_bcn;
			result2 = race1name + "=>" + barcelona[1]
			result3 = race2name + "=>" + madrid[1]

			time_mad = datetime.strptime(madrid[1], "%H:%M:%S")
			time_bcn = datetime.strptime(barcelona[1], "%H:%M:%S")

			total_mad = total_mad + timedelta(0, time_mad.hour * 3600 + time_mad.minute * 60 + time_mad.second)
			total_bcn = total_bcn + timedelta(0, time_bcn.hour * 3600 + time_bcn.minute * 60 + time_bcn.second)

			if (time_mad > time_bcn):
				diff = " " + race1name + " faster by " + str(time_mad - time_bcn)
				bcn_faster = bcn_faster + 1
				#total_diff += (time_mad - time_bcn)
			else:
				diff = " " + race2name + " faster by " + str(time_bcn - time_mad)
				mad_faster = mad_faster + 1
				#total_diff -= (time_bcn - time_mad)

			print result1 + (" " * (60 - len(result1))) + result2 + (" " * (18 - len(result2))) + result3 + "  " + diff

			cnt_tot = cnt_tot + 1

print
print "Ran " + race1name + " faster: " + str(bcn_faster) + ", ran " + race2name + " faster: " + str(mad_faster)

result = divide_time(total_bcn, cnt_tot)
print "Average " + race1name + " time " + result["hours"] + ":" + result["minutes"] + ":" + result["seconds"]
result = divide_time(total_mad, cnt_tot)
print "Average " + race2name + " time " + result["hours"] + ":" + result["minutes"] + ":" + result["seconds"]

if (total_bcn > total_mad):
	# MAD faster
	result = divide_time(datetime.strptime("0:0:0", "%H:%M:%S") + (total_bcn - total_mad), cnt_tot)
	faster = race2name
else:
	# BCN faster
	result = divide_time(datetime.strptime("0:0:0", "%H:%M:%S") + (total_mad - total_bcn), cnt_tot)
	faster = race1name

print "Average difference: " + faster + " faster by " + result["minutes"] + " minutes, " + result["seconds"] + " seconds"

'''
seconds = total_diff.second + total_diff.minute * 60 + total_diff.hour * 3600
div = seconds / cnt_tot
hours = int(div/3600)
minutes = int(((div - hours*3600)/60))
seconds = div - hours*3600 - minutes * 60
print "Average difference: " + race1name + " faster by " + str(minutes) + " minutes, " + str(seconds) + " seconds"
'''
