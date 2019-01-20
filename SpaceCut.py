def URLfromlist(raw):
    for course in raw:
        for char in course:
            if char.isdigit():
                cutlocation = char
                break
        coursename = course[0:int(cutlocation)]
        newstring = course[int(cutlocation)+1:]
        
        return (coursename, newstring)

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