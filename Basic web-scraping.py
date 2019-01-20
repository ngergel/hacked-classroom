import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

#sets the url
myUrl = "https://catalogue.ualberta.ca/Course/Details?subjectCode=MATH&catalog=102"


#opens the url and stores in into page_html
uClient = urlopen(myUrl)
page_html = uClient.read()
uClient.close()

#parses the html file (page_html)
page_soup = soup(page_html, "html.parser")


#grabs each part
containers = page_soup.findAll("div", {"class": "claptrap-class"})


for container in containers:
    print(container.em)
