import bs4

from stringCut import stringCut
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


MasterDictionary = {'(CAB 335)': [['test', 'ing'], ['day', 'starttime', 'endtime']]}
#we're just looking at the first container
container = str(containers[12].em)

#calls the Function that return day of week, start time, end time, and room number and splits the list
temp = stringCut(container)
templocation = str(temp.pop())

if templocation not in MasterDictionary:
    MasterDictionary[templocation] = [temp]
else:
    MasterDictionary[templocation].append(temp)



print(MasterDictionary)

