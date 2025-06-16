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









