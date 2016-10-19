# retrieve arbitrary "article links" until there are no article links found on the new page
# links that point to article pages have three things in common:
# 1. reside within the div with the id set to bodyContent
# 2. URLs do not contain colons
# 3. URLs begin with /wiki/

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
# takes in a Wiki article URL of the form /wiki/<Article_Name> and
# returns a list of all linked article URLs in the same form
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
# calls getLinks with some starting article, choose a random article link
# until there are no article links found
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
