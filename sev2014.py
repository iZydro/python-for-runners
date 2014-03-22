#!python

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

import codecs
import locale
import sys

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

for number in range (1, 10000):

	result = ""

	#feed = urlopen("file:///Users/isidro/code/python-for-runners/isidro.sev")
	feed = urlopen("http://sportmaniacs.com/events/athletes/my_ranking/53072209-9240-4455-9f22-0e7fbc5ffd2c/" + str(number))
	soup = BeautifulSoup(''.join(feed.read()))

	tables = soup.findAll('table')
	for table in tables:
		rows = table.findAll('tr')
		trc = 1
		for tr in rows:
			if trc == 1:
				cols = tr.findAll('td')
				tdc = 1
				for td in cols:
					if tdc == 4:
						for tde in td:
							for tdea in tde:
								result = result + tdea
					if tdc == 7:
						for tde in td:
							result = result + " | " + tde
					tdc = tdc + 1
			trc = trc + 1

	if result != "":
		print result
		sys.stdout.flush()
