import re
import urllib2
import webbrowser
import time
from bs4 import BeautifulSoup
from appscript import *

downloadLinks = 0


for num in range(1500,2000):
    u = "http://download.cnet.com/windows/3150-20_4-0-" + str(num) + ".html?sort=reviewDate%20asc&tag=page" # from download.com
    page = urllib2.urlopen(u)
    soup = BeautifulSoup(page)
    
    for link in soup.findAll(href=re.compile("26dlm")):
        downloadLinks = downloadLinks + 1
        print "Number of download links: ", downloadLinks
        url = link.get('href')
        print(url)               
        webbrowser.open(url)
        time.sleep(10)
        safari = app("Safari")
        safari.windows.first.current_tab.close()
