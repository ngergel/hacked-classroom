def URLfromlist(raw):
    #take each element from raw course list
    for course in raw:
        #finds the location of the first number and cuts everything before
        for char in course:
            if char.isdigit():
                cutlocation = char
                break
        coursename = course[0:int(cutlocation)]
        newstring = course[int(cutlocation)+1:]
        #finds the next space of new string and cuts out the course number
        for i in range(len(newstring)):
            if newstring[i] == " ":
                cutlocation2 = i
                break
        coursenum = newstring[0:cutlocation2]

        #replaces spaces with %20 (this is how the url is organized)
        coursename.replace(" ", "%20")

        #creates a url based on course name and course number
        url = str("https://catalogue.ualberta.ca/Course/Details?subjectCode=" + coursename + "&catalog=" + coursenum)
        print(url)


'''
    for i in range(len(string)):
        if char in string == " ":
            cutlocation = i
            print(cutlocation)
            break
'''


list = ["ACCTG 501 - Introduction to Financial Reporting and Analysis", "ACCTG 503 - Introduction to Financial Reporting and Analysis"]

firstlist = URLfromlist(list)
print(firstlist)

'''
for course in list:
    coursetuple = SpaceCut(str(list[0]))
    coursename = coursetuple[0]
    coursetuple2 = SpaceCut(coursetuple[1])
    coursenum = coursetuple2[0]
    url = str("https://catalogue.ualberta.ca/Course/Details?subjectCode=" + coursename + "&catalog=" + coursenum)
    print(url)
'''