import requests
import json
response=requests.get("http://saral.navgurukul.org/api/courses")
print(response.json())
def jprint(obj):
    text=json.dumps(obj,indent=4)
    print(text)
    print(text)
jprint(response.json())
""" Second method """
with open("courses.json","w") as b:
    json.dump(response.json(),b,sort_keys=True,indent=4)   
with open("courses.json","r") as c:
    d=json.load(c)
a=0
id=[]
for x in d["availableCourses"]:

    print(str(a),".",x["name"])
    a+=1
    id.append(x["id"])
user=int(input("Enter your courses number :- "))
Req=requests.get(" http://saral.navgurukul.org/api/courses/"+id[user]+"/exercises").text
a=json.loads(Req)
with open("Slug.json","w") as z:
    json.dump(a,z,indent=4)
b=0
slug=[]
slug_id=[]
child1=[]
for y in a["data"]:
    print(str(b+1),".",y["name"])
    slug_id.append(y["id"])
    slug.append(y["slug"])
    child=y["childExercises"]
    c=1
    for z in child:
        child1.append(z["slug"])
        print("     ",str(b),".",str(c),z["name"])
        c+=1
    b+=1
course=input("Enter your good courses :- ")
if type(int(course))==int:
    Req_12=requests.get(" http://saral.navgurukul.org/api/courses/"+id[user]+"/exercise/getBySlug?slug="+slug[int(course)]).text
    d=json.loads(Req_12)
    for a in d:
        if a=="content":
            x=d.get(a)
    d=json.loads(x)
    for c in d:
        for d in c:
            if d=="value":
                print(c.get(d))
elif type(float(course))==float:
    Req_13=requests.get("http://saral.navgurukul.org/api/courses/"+id[user]+"/exercise/getBySlug?slug="+child1[str(course)]).text
    c=json.loads(Req_13)
    for b in c:
        if b=="content":
            x=c.get(b)
    d=json.loads(x)
    for c in d:
        for d in c:
            if d=="value":
                print(c.get(d))
    



    
 
 
 
 