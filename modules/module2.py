#!/usr/bin/python



import json, bs4, requests
from tabulate import tabulate
strList=[]



def mod2(list1):
    for i in range(len(list1)):
        #print(" ".join(list1[i]))
        str1 = list1[i]
        str1[0] = str1[0][:4].lower() + "-" + str1[0][4:] 
        strList.append(str1[0])
    #print(strList[1])
    
    mainList = []
    courses = []
    depts = []
    for i in range(len(strList)):
        url = 'https://www.douglascollege.ca/course/' + strList[i]
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        models = soup.select('.page-title')
        labels = soup.select('.field__label')

        courses.append(models[0].getText())
        for label in labels:
            if label.getText() == 'Department':
                depts.append(label.find_next('div').getText())


    for x in range(len(list1)):
        smallList = []
        for y in range(len(list1[0])-1):
            smallList.append(list1[x][y])
        concat = smallList[4] + smallList[5] + smallList[6]
        smallList[4:7] = [concat]
        smallList.append(courses[x])
        smallList.append(depts[x])
        mainList.append(smallList)
        
    #print(mainList) 
    data = mainList
    html_value = html(data)


    with open('output_isi_938.html','w',encoding='utf-8') as file:
        file.write(html_value)
        print("Data written to html output file. Please check")
    
    
def html(data):
    table_html = "<table border='1'>\n"

    table_html += "  <tr>\n"
    headers = ['course code', 'section', 'professor', 'date', 'time', 'bdlg', 'room', 'course name', 'department']
    for header in headers:
        table_html += f"    <th>{header}</th>\n"
    table_html += "  </tr>\n"

    for row in data:
        table_html += "  <tr>\n"
        for item in row:
            table_html += f"    <td>{item}</td>\n"
        table_html += "  </tr>\n"
    table_html += "</table>"
    return table_html

