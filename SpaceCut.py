def URLfromlist(raw):
    urllist = []
    cutlocation = -1
    cutlocation2 = -1
    #take each element from raw course list
    for course in raw:
        #finds the location of the first number and cuts everything before
        for i in range(len(course)):
            if course[i].isdigit():
                cutlocation = i
                break
        coursename = course[0:cutlocation-1]
        newstring = course[cutlocation:]
        #finds the next space of new string and cuts out the course number
        for i in range(len(newstring)):
            if newstring[i] == " ":
                cutlocation2 = i
                break
        coursenum = newstring[0:cutlocation2]

        #replaces spaces with %20 (this is how the url is organized)
        coursename = coursename.replace(" ", "%20")

        #creates a url based on course name and course number
        url = str("https://catalogue.ualberta.ca/Course/Details?subjectCode=" + coursename + "&catalog=" + coursenum)
        urllist.append(url)
    return urllist


'''
    for i in range(len(string)):
        if char in string == " ":
            cutlocation = i
            print(cutlocation)
            break
'''


# list = ["AC CTG 501 - Introduction to Financial Reporting and Analysis", 'ACCTG 503 - Introduction to Financial Reporting and Analysis', 'ACCTG 610 - Financial Reporting for Managers and Analysts','ACCTG 610 - Financial Reporting for Managers and Analysts', 'ACCTG 614 - Intermediate Financial Accounting I']
#
# firstlist = URLfromlist(list)
# print(firstlist)

'''
for course in list:
    coursetuple = SpaceCut(str(list[0]))
    coursename = coursetuple[0]
    coursetuple2 = SpaceCut(coursetuple[1])
    coursenum = coursetuple2[0]
    url = str("https://catalogue.ualberta.ca/Course/Details?subjectCode=" + coursename + "&catalog=" + coursenum)
    print(url)
'''