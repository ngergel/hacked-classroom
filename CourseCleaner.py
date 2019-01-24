import bs4
from SpaceCut import URLfromlist
from string import ascii_letters, digits
from stringCut import stringCut
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from time import sleep
MasterDictionary = dict()


valid_chars=ascii_letters+digits+' -"[],'

file = open('Rawlist.txt', 'r')
text_list = file.read().split('”')
text_list = '"'.join(text_list)
text_list = text_list.split('“')

for i in range(len(text_list)):
    text_list[i] = text_list[i].strip()

text_list = str('"'.join(text_list))


# f = open('actual_list.txt', 'w')
# f.write(text_list)
# f.close()
# file.close()

proper_list = ''

for i in text_list:
    if i in valid_chars:
        proper_list += i

# empty
# for i in range(len(proper_list)):
#     element = proper_list[i].split()
#     proper_list[i] = "".join(element)
# print(proper_list)





exec('actual_list = '+proper_list)
# print(actual_list)

#final_url_list = URLfromlist(actual_list)
#print(final_url_list)

finalurllist = URLfromlist(actual_list)
# print(finalurllist)
#finalurllist = ['https://catalogue.ualberta.ca/Course/Details?subjectCode=EN%20PH&catalog=131']

totalcourses = len(finalurllist)



coursenum = 0
for myUrl in finalurllist[0:totalcourses]:

    #opens the url and stores in into page_html
    try:
        uClient = urlopen(myUrl)
        page_html = uClient.read()
        uClient.close()
    except:
        continue

    #parses the html file (page_html)
    page_soup = soup(page_html, "html.parser")

    #grabs each part
    containers = page_soup.findAll("div", {"class": "claptrap-class"})
    containerslength = len(containers)

#iterates through all the containers for data
    for i in range(0,containerslength):
        try:
            container = str(containers[i].em)
        except IndexError:
            continue

        if str(containers[i].h3).split()[4] != '2019' and str(containers[i].h3).split()[2] != 'Winter':
            continue

        #calls the Function that return day of week, start time, end time, and room number and splits the list
        temp = stringCut(container)

        if temp == None:
            continue

        templocation = str(temp.pop())

        if templocation not in MasterDictionary:
            MasterDictionary[templocation] = [temp]
        else:
            MasterDictionary[templocation].append(temp)
    print(myUrl)
    coursenum = coursenum   +1
    print(str(coursenum) + '/' + str(totalcourses))


f = open('newmaster_dict.txt', 'w')
f.write(str(MasterDictionary))
f.close()