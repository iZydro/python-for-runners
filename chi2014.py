#!python

from urllib.request import urlopen
from bs4 import BeautifulSoup

import codecs
import locale
import sys

#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

for number in range (54966, 99999):

    sys.stderr.write(str(number) + "\n")
    sys.stderr.flush()

    result = str(number) + " | "

    try:
        feed = urlopen(r"http://results.chicagomarathon.com/2014/?event=MAR&lang=EN_CAP&pid=search&search_sort=name&search[start_no]=" + str(number))
        results = feed.read()

        soup = BeautifulSoup(results)

        tables = soup.findAll('table')
        for table in tables:
            rows = table.findAll('tr')
            trc = 1
            for tr in rows:
                if trc == 2:
                    cols = tr.findAll('td')
                    tdc = 1
                    for td in cols:
                        if tdc == 4: # Name
                            cnt = 0
                            for tde in td:
                                if cnt == 1:
                                    for tdea in tde:
                                        name = tdea
                                        try:
                                            name = name.split(" (")[0]
                                            surname_name = name.split(",")
                                            name = surname_name[1].strip() + " " + surname_name[0].strip()
                                        except Exception as e:
                                            result += "(error)"
                                            pass
                                        result += name
                                cnt += 1
                        if tdc == 10: # Time
                            for tde in td:
                                result = result + " | " + tde.strip()
                        tdc = tdc + 1
                trc = trc + 1

        if result != str(number) + " | ":
            print(result)
            sys.stdout.flush()

    except:
        number -= 1
        continue
