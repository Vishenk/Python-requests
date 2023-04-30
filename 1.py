#Задание 1
import requests
name =[]
salary=[]
salary_clean=[]

for i in range(10):
    url="https://api.hh.ru/vacancies?text=Анаоитикк&area=1&search_field=name&per_page=100&page={}".format(str(i))
    items=requests.get(url).json()['items']
    for item in items:
        salary+=[item['salary']]
        name+=[item['name']]
        
for sal in salary:
    if sal:
        if sal['currency']=='RUR':
            coef=1
        else:
            coef=60
        if sal['gross']:
            gross=1
        else:
            gross=0.87
        if (sal['from'] and sal["to"]):
            salary_clean+=[(sal['from']+sal['to'])/2*coef*gross]
        elif sal['from']:
            salary_clean+=[sal['from']]
        elif sal['from']:
            salary_clean+=[sal['to']]
        else:
            salary_clean+=[None]
    else:
        salary_clean+=[None]
            
print(name)
print(salary_clean)
f=open("items_task1.txt", "w+", encoding='utf-8')
f.write(str(items))
f.close()