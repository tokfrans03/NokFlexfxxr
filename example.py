import NokFlexfxxr

course = NokFlexfxxr.getCourseid()
auth = NokFlexfxxr.getAuth()

state = "continue"
while state == "continue":
    print("\n\nEnter 1 to enter a assignment id\nEnter 2 to exit")
    a = input("> ")
    if a == "1":
        assignment = NokFlexfxxr.getAssignmentId()
        NokFlexfxxr.getAnswer(auth, course, assignment)
    else:
        exit()
