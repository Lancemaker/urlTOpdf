import pdfkit
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import time

html_page = urllib2.urlopen("http://gineco.bayer.foster.com.br/")
soup = BeautifulSoup(html_page)
links = []
regex = re.compile('[\W_]+')
i=0
for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
    #links.append(link.get('href'))
    link=link.get('href')    
    if "http://gineco.bayer.foster.com.br/" in link:
        outName=regex.sub('', link[-20:]+str(i))+'.pdf'
        print(outName)
        try:
            pdfkit.from_url(link, outName)
            i+=1
        except:
            print("erro")
        time.sleep(4)

