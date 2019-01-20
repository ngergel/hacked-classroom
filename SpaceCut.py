def SpaceCut(string):
    for i in range(len(string)):
        if string[i] == " ":
            cutlocation = i
            break
    coursename = string[0:cutlocation]
    newstring = string[cutlocation+1:]
    return (coursename, newstring)

list = ["ACCTG 501 - Introduction to Financial Reporting and Analysis", "ACCTG 503 - Introduction to Financial Reporting and Analysis"]


for course in list:
    coursetuple = SpaceCut(str(list[course]))
    coursename = coursetuple[course]
    coursetuple2 = SpaceCut(coursetuple[course+1])
    coursenum = coursetuple2[course]
    url = str("https://catalogue.ualberta.ca/Course/Details?subjectCode=" + coursename + "&catalog=" + coursenum)
    print(url)
