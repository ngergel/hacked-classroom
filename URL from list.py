def SpaceCut(string):
    for i in range(len(string)):
        if string[i] == " ":
            cutlocation = i
            print(cutlocation)
            break
    coursename = string[0:cutlocation]
    newstring = string[cutlocation+1:]
    return (coursename, newstring)




file = open('Rawlist.txt', 'r')
text_list = file.read().split('”')
text_list = '"'.join(text_list)
text_list = text_list.split('“')

for i in range(len(text_list)):
    text_list[i] = text_list[i].strip()

raw_list = '"'.join(text_list)


for course in raw_list:
    coursetuple = SpaceCut(str(raw_list[0]))
    coursename = coursetuple[0]
    coursetuple2 = SpaceCut(coursetuple[1])
    coursenum = coursetuple2[0]
    url = str("https://catalogue.ualberta.ca/Course/Details?subjectCode=" + coursename + "&catalog=" + coursenum)
    print(url)
