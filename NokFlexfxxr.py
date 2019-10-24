import json
import requests
import html

baseurl = "https://nokflex-api.nok.se/api/v2/assignment/solution/"

def getAuth():
    return input("Enter your Authorization code (very long)\n> ")

def getCourseid():
    return input("Enter your course id (ex 960) \n> ")

def getAssignmentId():
    return input("Enter your assignmentId id (ex 10461) \n> ")

def striphtmltags(input, first, second):
    return input.replace(first, "").replace(second, "")

def getAwnser(auth, course, assignment):
    
    headers = {
    "Authorization": "Bearer " + auth
    }
    print("\nGetting: " + baseurl + assignment + '?courseId=' + course)

    awnser = json.loads(requests.get(url = baseurl + assignment + '?courseId=' + course,  headers=headers).text)

    if awnser["hasSolution"] == True:
        for x in awnser["solution"]:
            print(x["subTask"])
            
            a = x["answers"]
            a = html.unescape(a)
            a = striphtmltags(a, "<div>", "</div>")
            a = striphtmltags(a, "<em>", "</em>")
            a = striphtmltags(a, "<section>", "</section>")
            a = striphtmltags(a, "<p>", "</p>")
            a = a.replace("\n", "")

            print(a, "\n")

