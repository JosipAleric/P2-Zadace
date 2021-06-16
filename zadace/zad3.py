import re

string = str(input("Unesite neki string: "))
string = string.lower()

regex = "^j.*[0-5]\s.*a$" 

result = re.findall(regex, string)

if result:
  print("Podudaranje")
else:
  print("Nema podudaranja")   