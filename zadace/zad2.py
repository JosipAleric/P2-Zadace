from csv import reader
# open file in read mode
with open('rezultati.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    rezultati = list(map(tuple, csv_reader))
    # display all rows of csv
    rezultati.sort()
    #print(rezultati)


#Sortiranje liste po prezimenima
novi_rezultati = []
for ime, prezime, bodovi in rezultati:
	novi_rezultati.append((prezime, ime, bodovi))

novi_rezultati.sort()
print(novi_rezultati)



d = {}

for ime, prezime, bodovi in novi_rezultati:
  bodovi = int(bodovi)
  if bodovi < 50:
    ocjena = 1
    d[ime + " " + prezime] = ocjena
  elif bodovi < 65:
    ocjena = 2
    d[ime + " " + prezime] = ocjena
  elif bodovi < 80:
    ocjena = 3
    d[ime + " " + prezime] = ocjena
  elif bodovi < 90:
    ocjena = 4
    d[ime + " " + prezime] = ocjena
  else:
     ocjena = 5
     d[ime + " " + prezime] = ocjena    
 

print("\n" + "\n")
print(d)
print("\n" + "\n")

for ime, ocjena in d.items():
  print(ime,  ":", ocjena) 

	    

