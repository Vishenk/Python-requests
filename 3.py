#Задача 3
import requests
name1 =[]
salary1=[]
name2 =[]
salary2=[]
clean_salary1=[]
clean_salary2=[]
dict1={}
dict2={}
answer={}

for i in range(20):
    url="https://api.hh.ru/vacancies?area=2&search_field=name&per_page=100&page={}".format(str(i))
    items1=requests.get(url).json()['items']
    for item in items1:
        salary1+=[item['salary']]
        name1+=[item['name']]
        
for i in range(20):
    url="https://api.hh.ru/vacancies?area=1&search_field=name&per_page=100&page={}".format(str(i))
    items2=requests.get(url).json()['items']
    for item in items2:
        salary2+=[item['salary']]
        name2+=[item['name']]
      

i=0  
while i<2000:
    sal1=salary1[i]
    if sal1 and sal1['from']:
        if sal1['currency']=='RUR':
            coef=1
        else:
            coef=60
        if sal1['gross']:
            gross=1
        else:
            gross=0.87
        sal1['from']=sal1['from']*coef*gross
        clean_salary1+=[sal1['from']]
    else:
        clean_salary1+=[0]
    i+=1
        
i=0  
while i<2000:
    sal2=salary2[i]
    if sal2 and sal2['from']:
        if sal2['currency']=='RUR':
            coef=1
        else:
            coef=60
        if sal2['gross']:
            gross=1
        else:
            gross=0.87
        sal2['from']=sal2['from']*coef*gross
        clean_salary2+=[sal2['from']]
    else:
        clean_salary2+=[0]
    i+=1
    
i=0  
while i<2000:
    if name1[i] not in dict1:
        dict1[name1[i]]=clean_salary1[i]
    else:
        if clean_salary1[i]>dict1[name1[i]]:
            dict1[name1[i]]=clean_salary1[i]
    i+=1
i=0  
while i<2000:
    if name2[i] not in dict2:
        dict2[name2[i]]=clean_salary2[i]
    else:
        if clean_salary2[i]>dict2[name2[i]]:
            dict2[name2[i]]=clean_salary2[i]
    i+=1

for name in dict1:
    if name in dict2 and dict1[name] and dict2[name]:
        if dict1[name]>dict2[name]:
            answer[name]=dict1[name]
            
print(len(answer))

maximum=0
for name in answer:
    if answer[name]>maximum:
        maximum=answer[name]
        maximum_name=[name]
    elif answer[name]==maximum and answer[name]!=0:
        maximum_name+=[name]
print(maximum_name, maximum)
f=open("items_task3_spb.txt", "w+", encoding='utf-8')
f.write(str(items1))
f.close()
f=open("items_task3_msk.txt", "w+", encoding='utf-8')
f.write(str(items2))
f.close()


