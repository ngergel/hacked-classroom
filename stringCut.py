def stringCut(container):

    def findSpace(containername):
        for i in range(len(containername)):
            if containername[i] == " ":
                return i

    # stores the day of week the class occurs in
    index = findSpace(container)
    dayOfWeek = container[4:index]

    # make the new string (should be shorter)
    container2 = container[index + 1:]

    # isolating starttime
    index2 = findSpace(container2)
    startTime = container2[0:index2]
    container3 = container2[index2:]

    if dayOfWeek[0] not in 'MTWRF':
        return None

    # print("Day of week is: " + dayOfWeek)
    # print("start time is: " + startTime)

    # isolating endtime
    endtime = container3[2:11]
    # print("end time is: " + endtime)

    room = container3[12:-5]
    # print("room is located: " + room)

    roomtuple = [dayOfWeek, startTime, endtime, room]

    return roomtuple