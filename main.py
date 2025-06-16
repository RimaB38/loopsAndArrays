from random import random

print("loops and arrays")

print("loops and arrays")

print("loops and arrays")

for i in range(10):
    print("labas")

for i in range(10):
    print(i)

for i in range(10):
    print(i)
augalai = ["roze" , "gvazdikas" , "krapai", "slyva", "ramune", "kaktusas", "lelija", "saulegraza" ,"pusis" , "liepa"]
print(augalai)

#sukuriamas masyvas (sarasa) is 10 augalu
augalai = [ "lelija", "saulegraza" ,"pusis" , "liepa", "roze" , "gvazdikas" , "krapai", "slyva", "ramune", "kaktusas"]
for augalas in augalai:
    print(augalas)

for skaicius in range(10, 51, 2) :
    print(skaicius)

if skaicius  % 10 == 0:
   "continue"
   print(skaicius)

Kiek_poriniu = 0

for i in range(21) : #nuo 0 iki 20
    if i % 2 == 0:
        kiek_poriniu = i
print("poriniu reiksmiu kiekis:" , kiek_poriniu)


trumpi = 0
ilgi = 0
for augalas in augalai:
    if len(augalas) >=  7:
        trumpi += 1
    if len(augalas) > 5 :
        ilgi += 1
print("trumpesni nei 5 simboliai:" , trumpi)
print("ilgesno nei 7 simboliai", ilgi)

tinkami_zodziai = 0
#einame per visus zodzius ir tikriname ilgi
for augalas in augalai:
    ilgis = len(augalas)
    if ilgis > 5 and ilgis <10:
        tinkami_zodziai += 1
print(tinkami_zodziai, "kuriu ilgis tarp 6 ir 9 simboliu")

#sugeneruojame 300 atsitiktiniu skaiciu nuo 0 iki 300
skaiciai = []
for _ in range(300) :
    skaiciai.append(random.randint(0, 300 ))
#jei >275 - skliaustelliuose
for skaicius in skaiciai:
    if skaicius > 275:
        print( str["skaicius"], end= " ")
    else:
        print(skaicius, end=" ")
#kiek skaiciu didesni nei 150
didesni_nei_150 = 0
for skaicius in skaiciai:







