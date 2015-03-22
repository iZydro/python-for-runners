#!python

import urllib.request
from bs4 import BeautifulSoup

import codecs
import locale
import sys

#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

for number in range(1, 20000):

    result = ""
    result = str(number) + " | "

    try:
        req = urllib.request.Request("http://www.zurichmaratobarcelona.es/cgi-bin/2015/ZMB_result_res_maraton-es.py?value=" + str(number))
        feed = urllib.request.urlopen(req)
        results = feed.read()

        soup = BeautifulSoup(results)

        tables = soup.findAll('table')
        for table in tables:
            rows = table.findAll('tr')
            trc = 1
            for tr in rows:
                if trc == 7 or True:
                    cols = tr.findAll('td')
                    tdc = 1
                    for td in cols:
                        if tdc == 3:
                            for tde in td:
                                for tdea in tde:
                                    for tdeas in tdea:
                                        result = result + tdeas
                        if tdc == 8:
                            for tde in td:
                                result = result + " | " + tde.strip()
                        tdc = tdc + 1
                trc = trc + 1
    except:
        number -= 1
        #result += "error | 09:59:59"

    if result != str(number) + " | ":
        print(result)
        sys.stdout.flush()
