# only links are new should be crawled for additional links
# looks for all links that begin with /wiki/ (don't restrict to article links)
# collects the title, the 1st paragraph of content and the link to edit the page if available

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("this page is missing something")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # encountered a new page
                newPage = link.attrs['href']
                print("--------------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")
