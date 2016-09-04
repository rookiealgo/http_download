import urllib
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

def downloadAllImg(page):
    imgs = page.findAll('img')

    for img in imgs:
        url = img.get('src')
        # url.rsplit('-', 1)[-1]
        fileName =  url.rsplit('/', 1)[-1]
        print fileName
        urllib.urlretrieve(url, fileName)

page = BeautifulSoup(urllib.urlopen('http://taviqinvesting.com/'))
downloadAllImg(page)
