#!python

from urllib2 import urlopen
from xml.dom import minidom
from BeautifulSoup import BeautifulSoup

import codecs
import locale
import sys

#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

for number in range (1, 1050):

	result = ""

	feed = urlopen("http://www.maratonmadrid.org/resultados/clasificacion.asp?carrera=10&parcial=10&clasificacion=1&dorsal=F" + str(number))

	soup = BeautifulSoup(''.join(feed.read()))

	t = soup.find("table", {"width":"98%"})
	r = t.findAll("tr")
	if len(r) > 1:
		d = r[1].findAll("td")

		for tde in d[2]:
			for tdea in tde:
				for tdeas in tdea:
					result = result + str(tdeas)

		for tde in d[3]:
			for tdea in tde:
				for tdeas in tdea:
					result = result + " " + str(tdeas)

		for tde in d[6]:
			for tdea in tde:
				for tdeas in tdea:
					result = result + " | " + str(tdeas)

		print result
		sys.stdout.flush()

