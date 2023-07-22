#!/usr/bin/python

import requests,bs4,json

import modules.module2 as mod2


def mod1():
    url = 'https://www.douglascollege.ca/current-students/important-dates-information/exam-schedule'

    list1 = []
    list2 = []
    response=requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    gg = soup.select(".xl73")
    st = ''
    for i in gg:
        teacherName = i.getText().lower().split()[0]
        if teacherName == 'sarif':
           list1.append(i.find_parent())
    for j in range(len(list1)):
        list2.append(list1[j].getText().split("\n"))
    #for x in range(len(list2)):
       # print(" ".join(list2[x]))
    mod2.mod2(list2)
