import requests

r = requests.get("https://google.com")
print(r.status_code)

name=input("Your name? ")
print("Hello,",name)
print(r.ok)



list_of_ppl=["Wayne", "Esther"]
list_of_ppl.append("Ze Xuan")
print(list_of_ppl)
