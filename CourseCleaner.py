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






for myUrl in finalurllist:

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

    #we're just looking at the first container
    try:
        container = str(containers[0].em)
    except IndexError:
        continue

    if str(containers[0].h3).split()[4] != '2019':
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
    # print(MasterDictionary)
print(MasterDictionary)

f = open('master_dict.txt', 'w')
f.write(str(MasterDictionary))
f.close()