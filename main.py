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
import random
for _ in range(300) :
    skaiciai.append(random.randint(0, 300))
#jei >275 - skliausteliuose
for skaicius in skaiciai:
    if skaicius > 275:
        print("[" + str("skaicius") + "]", end= " ")
    else:
        print(skaicius, end=" ")
#kiek skaiciu didesni nei 150
didesni_nei_150 = 0
for skaicius in skaiciai:
    if skaicius > 150:
        didesni_nei_150 += 1
    print("skaicius, didesni_nei_150, kiekisend:",didesni_nei_150)

skaiciai = []
for i in range(1,3001):
     if i % 77 == 0:
      skaiciai.append(str(i))

      print(",".join(skaiciai))

#nupiesti kvadrata is zvaigzduciu
for i in range(25):
    print("*" * 25)

for y in range(25):
    for x in range(25):
        if y == x or x == 24 - y:
            print("X", end=" ")
        else:
            print("*", end=" ")
    print()
import random
# kai iskrenta herbas
while True:
    metimas = random.randint (0, 1)
    if metimas == 0:
        print( "H")
        break
    else:
        print( "S")
#stabdom kai tris kartus iskrenta herbas
import random

herbu_kiekis = 0

while herbu_kiekis < 3:
    metimas = random.randint (0, 1)
    if metimas == 0:
        print( "H")
        herbu_kiekis += 1
    else:
        print("S")
#stabdom kai iskrenta 3 herbai is eiles
import random

herbu_is_eiles = 0

while herbu_is_eiles < 3:
    metimas = random.randint (0, 1)
    if metimas == 0:
        print( "H")
        herbu_is_eiles +=1
    else:
        print("S")
        herbu_is_eiles = 0

petras_total = 0
kazys_total = 0
partijos_nr = 0


while petras_total < 222 and kazys_total < 222:
    partijos_nr += 1
    petras_points = random.randint (10, 20)
    kazys_points = random.randint (5, 25)
    petras_total += petras_points
    kazys_total += kazys_points

    if petras_points > kazys_points:
        print("Partijos nr:", partijos_nr, "laimejo Petras", petras_points)
    elif kazys_points > petras_total:
        print("Partijos nr:", partijos_nr, "laimejo Kazys", kazys_points)
    else:
        print("Partijos nr:", partijos_nr, "lygiosios " )

print("Petras",petras_total,"Kazys",kazys_total)
if petras_total > kazys_total:
    print("laimejo Petras")
elif petras_total < kazys_total:
    print("laimejo Kazys")
else:
    print("Lygiosios")











