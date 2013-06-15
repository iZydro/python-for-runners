#!python

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

mad = []
bcn = [] 
read_results("mad-her.txt", mad)
read_results("bcn.txt", bcn)

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
			result2 = "BCN: " + barcelona[1]
			result3 = "MAD: " + madrid[1]

			time_mad = datetime.strptime(madrid[1], "%H:%M:%S")
			time_bcn = datetime.strptime(barcelona[1], "%H:%M:%S")

			total_mad = total_mad + timedelta(0, time_mad.hour * 3600 + time_mad.minute * 60 + time_mad.second)
			total_bcn = total_bcn + timedelta(0, time_bcn.hour * 3600 + time_bcn.minute * 60 + time_bcn.second)

			if (time_mad > time_bcn):
				diff = " BCN faster by " + str(time_mad - time_bcn)
				bcn_faster = bcn_faster + 1
				total_diff += (time_mad - time_bcn)
			else:
				diff = " MAD faster by " + str(time_bcn - time_mad)
				mad_faster = mad_faster + 1
				total_diff -= (time_bcn - time_mad)

			print result1 + (" " * (60 - len(result1))) + result2 + (" " * (16 - len(result2))) + result3 + "  " + diff

			cnt_tot = cnt_tot + 1

print
print "Ran MAD faster: " + str(mad_faster) + ", ran BCN faster: " + str(bcn_faster)

result = divide_time(total_mad, cnt_tot)
print "Average MAD time " + result["hours"] + ":" + result["minutes"] + ":" + result["seconds"]
result = divide_time(total_bcn, cnt_tot)
print "Average BCN time " + result["hours"] + ":" + result["minutes"] + ":" + result["seconds"]

seconds = total_diff.second + total_diff.minute * 60 + total_diff.hour * 3600
div = seconds / cnt_tot
hours = int(div/3600)
minutes = int(((div - hours*3600)/60))
seconds = div - hours*3600 - minutes * 60
#print "Total difference: BCN faster by " + str(total_diff - init_diff)
print "Average difference: BCN faster by " + str(minutes) + " minutes, " + str(seconds) + " seconds"
