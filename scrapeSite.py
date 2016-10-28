#! python3
#----------------------------------------------------------
# scrapeSite.py opens and scrapes a site of your choosing
#----------------------------------------------------------
# execute in the command line:
#
#   python3 scrapeSite.py <site_to_scrape>
#----------------------------------------------------------

import sys, requests, webbrowser
siteToScrape = ''.join(sys.argv[1:])
webbrowser.open(siteToScrape)
res = requests.get(siteToScrape)
res.raise_for_status()
# we can also save the scraped web page
# onto our hard drive, using the open()
# and write() methods.
playFile = open('scrapeMent.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
