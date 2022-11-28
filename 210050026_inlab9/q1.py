import requests
from bs4 import BeautifulSoup
import sys
from collections import OrderedDict

query = sys.argv[1]

if len(query) > 5 or not (query[:2] == 'CS' and query[2:].isnumeric()):     # checking valid input
    print("NOT FOUND")
    exit(1)

r = requests.get('https://www.cse.iitb.ac.in/academics/courses.php')        # getting request from url

soup = BeautifulSoup(r.content, 'html5lib')        

univ_div = soup.find_all('div', attrs={"class":"collapsible-body", "align":"justify"})  # wanted division

univs = univ_div[4].find_all('table')       # all tables of Universities data

Univ_data = {}              # dict with keys as univ name and values as its courses
for univ in univs:          # storing univ data into list & dict
    course_data = []
    name = (univ.find('th')).getText()
    words = name.split(' ')
    univ_name = words[len(words)-1]
    for row in univ.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 2:
            values = cols[1].getText().replace('+',',').replace(' & ',',').replace('(m)',',').replace('M',',').split(',')
            for val in values:
                course_data.append(val)
                course_data.append(cols[0].getText().strip())
    Univ_data[univ_name] = course_data

course = []         # list to store course founded
univData = OrderedDict(sorted(Univ_data.items()))
for k in univData.keys():
    for i in range(len(univData[k])):
        if univData[k][i] == query and not i%2:
            courseFound = (k+":"+univData[k][i+1]).strip(" ")
            course.append(courseFound)

if len(course) == 0:          
        print("NOT FOUND")
else:
    for i in course[0:-1]:
        print(i,end=";")
    print(course[-1])