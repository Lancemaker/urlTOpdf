from selenium import webdriver
import Util
import asyncio
import datetime
import re
path="/home/lancemaker/Documents/Github/PageToPDF/img/"
url='google.com'
q=0

f = open('sitemap.xml','r')

#prints shit with selenium 
async def printPages(u,o):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_position(0,0)
    driver.set_window_size(1600,900)
    print(u)
    driver.get(u)
    Util.fullpage_screenshot(driver, o)
    driver.close()

res = f.readlines()
data = []
loop = asyncio.get_event_loop()
for d in res:
    if d != None:
        data.append(re.findall('<loc>(http:\/\/.+)<\/loc>',d))

#print(data,str(len(data)))
loop = asyncio.get_event_loop()
for i in data:    
    if i:
        url=i[0]
        out=path+("%04d" % (q,))+".png"    
        print(datetime.datetime.now(),url,out)        
        loop.run_until_complete(printPages(url,out))        
        print(datetime.datetime.now())
        q+=1
loop.close()

