from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sys
import re

username = sys.argv[1]
passWord = sys.argv[2]
ta_name = sys.argv[3]

app_data = {
    "login": username,
    "password": passWord,
    "url": "https://moodle.iitb.ac.in/login/index.php",
    "ta": ta_name
}

def auth_moodle(data: dict) -> requests.Session():
    ann_scrap =[]
    login, password, url_domain, ta_name = data.values()
    s = requests.Session()
    r_1 = s.get(url=url_domain + "/login/index.php")
    pattern_auth = '<input type="hidden" name="logintoken" value="\w{32}">'
    token = re.findall(pattern_auth, r_1.text)
    token = re.findall("\w{32}", token[0])[0]
    payload = {'anchor': '', 'logintoken': token, 'username': login, 'password': password, 'rememberusername': 1}
    r_2 = s.post(url=url_domain + "/login/index.php", data=payload)
    soup = BeautifulSoup(r_2.content, 'html5lib')
    course_link = ""
    for i in soup.find_all('a'):
        if "CS 251-2022-1" in i.getText():
            print(i.get('href'))
            course_link += (i.get('href'))
            break
    #if len(course_link)==0:
    #    raise Exception("CS 251-2022-1 course is not present")
    r_3 = s.post(course_link, data=payload)
    soup1 = BeautifulSoup(r_3.content, 'html5lib')
    annoucement = ""
    for i in soup1.find_all('a'):
        if "Announcements" in i.getText():
            annoucement += i.get('href')
    r_4 = s.post(annoucement, data=payload)
    soup2 = BeautifulSoup(r_4.content, 'html5lib')
    #print(soup2.find('html'))
    Anntable = soup2.find_all('tr', attrs={'class':'discussion subscribed'})
    for ann in Anntable:
        col = ann.find('th')
        #for i in col:
        #    print(i)
        #    print("-------------------------------------------------------------------------------------------")

        ''' CHECKING TA NAME!
        TA_name = ""
        started_by = (col[1].getText()).split()[:len((col[1].getText()).split())-3]
        for i in started_by[:-1]:
            TA_name += i + " "
        TA_name += started_by[-1]
        if TA_name == ta_name:
            print(TA_name)
        else:
            continue'''
        ann_link = col.find('a').get('href')
        r_5 = s.post(ann_link, data=payload)
        soup3 = BeautifulSoup(r_5.content, 'html5lib')
        totalsubAnn = soup3.find_all('header', attrs={"class":"mb-2 header row d-flex"})
        for j in totalsubAnn:
            if j.find('a') != None:
                #print(i.find('a').getText())
                if j.find('a').getText() == ta_name:
                    word = j.find('time').getText() + "; " + j.find('h3').getText()
                    ann_scrap.append(word)
    return ann_scrap

    #for i in r_2.text.splitlines():
    #    if "<title>" in i:
    #        print(i[15:-8:])
    #        break
    #counter = 0
    #for i in r_2.text.splitlines():
    #    if "loginerrors" in i or (0 < counter <= 3):
    #        counter += 1
    #        print(i)
    #return s


annList = auth_moodle(data=app_data)
# Creates a new file
#for i in annList:
#    print(i)
with open('announcements.txt', 'w') as fp:
    for i in annList:
        fp.write(i)
        fp.write('\n')