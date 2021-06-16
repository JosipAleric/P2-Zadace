imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

from random import *


d = {}

for ime in imena:
  d[ime] = randint(1,5)

print(d)

print("\n" + "\n")

brojac = 0
pet = 0
cetiri = 0
tri = 0
dva = 0
jedan = 0

for ocjena in d.values():
  brojac += 1
  if ocjena == 5:
    pet += 1
  elif ocjena == 4:
    cetiri += 1
  elif ocjena == 3:
    tri += 1
  elif ocjena == 2:
    dva += 1
  else:
    jedan += 1
  
postotak = ((pet + cetiri + tri + dva) / brojac) * 100
postotak1 ="{:.2f}".format(postotak)


print("Petice: ", pet)
print("Cetvorke: ", cetiri) 
print("Trojke: ", tri) 
print("Dvice: ", dva) 
print("Jedinice: ", jedan)   
print("Postotak prolaznosti: ", postotak1, "%")
    
