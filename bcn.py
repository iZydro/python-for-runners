#!python

from urllib2 import urlopen
from xml.dom import minidom
from BeautifulSoup import BeautifulSoup

import codecs
import locale
import sys

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

for number in range (1, 20000):

	result = ""

	feed = urlopen("http://www.zurichmaratobarcelona.es/cgi-bin/ZMB_result_res_maraton-es.py?value=" + str(number))

	soup = BeautifulSoup(''.join(feed.read()))

	tables = soup.findAll('table')
	for table in tables:
		#print "TABLE"
		rows = table.findAll('tr')
		trc = 1
		for tr in rows:
			#print "TR"
			if trc == 7:
				cols = tr.findAll('td')
				tdc = 1
				for td in cols:
					if tdc == 3:
						for tde in td:
							for tdea in tde:
								for tdeas in tdea:
									result = result + tdeas
						#print str(td)
					if tdc == 7:
						for tde in td:
							result = result + " | " + tde
						#print str(td)
					tdc = tdc + 1
			trc = trc + 1

	if result != "":
		print result
		sys.stdout.flush()
