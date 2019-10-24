import NokFlexfxxr

course = NokFlexfxxr.getCourseid()
auth = NokFlexfxxr.getAuth()

print("\n\nEnter 1 to enter a assignment id\nEnter 2 to exit")

state = "continue"
while state == "continue":
    a = input("> ")
    if a == "1":
        assignment = NokFlexfxxr.getAssignmentId()
        NokFlexfxxr.getAwnser(auth, course, assignment)
    else:
        exit()