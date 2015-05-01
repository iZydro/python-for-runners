#!python

from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

import codecs
import locale
import sys

#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

for number in range (11461, 14000):

    sys.stderr.write(str(number) + "\n")
    sys.stderr.flush()

    result = str(number) + " | "

    # feed = urlopen("http://www.maratonmadrid.org/resultados/clasificacion.asp?carrera=10&parcial=10&clasificacion=1&dorsal=" + str(number))
    #feed = urlopen("http://www.resultadoscarreras.es/index.php?pag=res&idi=ES&car=6&eve=1&par=11&cla=1&nom=&ape=&pai=&nup=0&dor=" + str(number))

    #soup = BeautifulSoup(''.join(feed.read()))

    try:
        req = urllib.request.Request("http://www.resultadoscarreras.es/index.php?pag=res&idi=ES&car=6&eve=1&par=11&cla=1&nom=&ape=&pai=&nup=0&dor=" + str(number))
        feed = urllib.request.urlopen(req)
        results = feed.read()

        soup = BeautifulSoup(results)

        t = soup.find("table")
        r = t.findAll("tr")
        if len(r) > 1:
            d = r[1].findAll("td")

            for tde in d[2]:
                for tdea in tde:
                    for tdeas in tdea:
                        result = result + str(tdeas)

            for tde in d[3]:
                result = result + " " + str(tde)

            for tde in d[6]:
                result = result + " | " + str(tde)

        if result != str(number) + " | ":
            print(result)
            sys.stdout.flush()

    except:
        number -= 1

