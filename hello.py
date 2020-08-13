import requests

r = requests.get("https://google.com")
print(r.status_code)

name=input("Your name? ")
print("Hello,",name)
print(r.ok)

for i in range(10):
    list1=[]
    list1.append(i)
print(list1)
