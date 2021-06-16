#Prva funkcija
def dobrodosao(ime):
    print ("Dobrodosao " + ime)
    
#Druga funkcija
pozdrav = (lambda ime: ("Pozdrav " + ime))

#Treca funkcija
def dobrodoslica(funkcija):
    return funkcija("Josip")

print(dobrodoslica(dobrodosao))
print(dobrodoslica(pozdrav))
