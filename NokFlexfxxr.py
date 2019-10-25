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

def striphtmltags(input):
    input = html.unescape(input)
    input = input.replace("<div>", "").replace("</div>", "")
    input = input.replace("<em>", "").replace("</em>", "")
    input = input.replace("<mo>", "").replace("</mo>", "")
    input = input.replace("<mtr>", "").replace("</mtr>", "")
    input = input.replace("<mi>", "").replace("</mi>", "")
    input = input.replace("<mtd>", "").replace("</mtd>", "")
    input = input.replace("<mn>", "").replace("</mn>", "")
    input = input.replace("<msup>", "").replace("</msup>", "")
    input = input.replace("<mrow>", "").replace("</mrow>", "")
    input = input.replace("<mtext>", "").replace("</mtext>", "")
    input = input.replace("<mtable>", "").replace("</mtable>", "")
    input = input.replace("<math>", "").replace("</math>", "")
    input = input.replace("<section>", "").replace("</section>", "")
    input = input.replace("<p>", "").replace("</p>", "")
    input = input.replace("<br>", " ")
    input = input.replace("\n", "")
   
    return input

def getAnswer(auth, course, assignment):
    
    headers = {
    "Authorization": "Bearer " + auth
    }
    print("\nGetting: " + baseurl + assignment + '?courseId=' + course)

    answer = json.loads(requests.get(url = baseurl + assignment + '?courseId=' + course,  headers=headers).text)



    for x in answer["solution"]:
        print("\nsolution", x["subTask"], "\n")
        
        print("Hints", striphtmltags(x["hints"]))
        print("\nSolutions", striphtmltags(x["solutions"]))
        print("\nAnswers", striphtmltags(x["answers"]))