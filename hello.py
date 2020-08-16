import requests

r = requests.get("https://google.com")
print(r.status_code)


print(r.ok)

list_of_ppl=["Wayne", "Esther"]
list_of_ppl.append("Ze Xuan")
print(list_of_ppl)

list2=[]
for i in range(10):
    list2.append(i)
print(list2)


