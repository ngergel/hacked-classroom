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


#we're just looking at the first container
container = str(containers[0].em)

#looking for the first space in the container
def findSpace(containername):
    for i in range(len(container)):
        if containername[i] == " ":
            return i

#stores the day of week the class occurs in
index = findSpace(container)
dayOfWeek = container[4:index]

#make the new string (should be shorter)
container2 = container[index+1:]

#isolating starttime
index2 = findSpace(container2)
startTime = container2[0:index2]
container3 = container2[index2:]

print("Day of week is: " + dayOfWeek)
print("start time is: " + startTime)

#isolating endtime
endtime = container3[2:11]
print("end time is: " + endtime)

room = container3[12:-5]
print("room is located: " + room)





