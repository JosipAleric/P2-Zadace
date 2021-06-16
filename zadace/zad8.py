#Prva funkcija
def dobrodosao(ime):
    print ("Dobrodosao " + ime)
    
#Druga funkcija
pozdrav = (lambda ime: ("Pozdrav " + ime))

#Treca funkcija
def dobrodoslica(funkcija):
    return funkcija("Marko")

print(dobrodoslica(dobrodosao))