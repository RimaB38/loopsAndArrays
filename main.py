# from operator import length_hint
# from random import random
#
# print("loops and arrays")
#
# print("loops and arrays")
#
# print("loops and arrays")
#
# for i in range(10):
#     print("labas")
#
# for i in range(10):
#     print(i)
#
# for i in range(10):
#     print(i)
# augalai = ["roze" , "gvazdikas" , "krapai", "slyva", "ramune", "kaktusas", "lelija", "saulegraza" ,"pusis" , "liepa"]
# print(augalai)
#
# #sukuriamas masyvas (sarasa) is 10 augalu
# augalai = [ "lelija", "saulegraza" ,"pusis" , "liepa", "roze" , "gvazdikas" , "krapai", "slyva", "ramune", "kaktusas"]
# for augalas in augalai:
#     print(augalas)
#
# for skaicius in range(10, 51, 2) :
#     print(skaicius)
#
# if skaicius  % 10 == 0:
#    "continue"
#    print(skaicius)
#
# Kiek_poriniu = 0
#
# for i in range(21) : #nuo 0 iki 20
#     if i % 2 == 0:
#         kiek_poriniu = i
# print("poriniu reiksmiu kiekis:" , kiek_poriniu)
#
#
# trumpi = 0
# ilgi = 0
# for augalas in augalai:
#     if len(augalas) >=  7:
#         trumpi += 1
#     if len(augalas) > 5 :
#         ilgi += 1
# print("trumpesni nei 5 simboliai:" , trumpi)
# print("ilgesno nei 7 simboliai", ilgi)
#
# tinkami_zodziai = 0
# #einame per visus zodzius ir tikriname ilgi
# for augalas in augalai:
#     ilgis = len(augalas)
#     if ilgis > 5 and ilgis <10:
#         tinkami_zodziai += 1
# print(tinkami_zodziai, "kuriu ilgis tarp 6 ir 9 simboliu")
#
# #sugeneruojame 300 atsitiktiniu skaiciu nuo 0 iki 300
# skaiciai = []
# import random
# for _ in range(300) :
#     skaiciai.append(random.randint(0, 300))
# #jei >275 - skliausteliuose
# for skaicius in skaiciai:
#     if skaicius > 275:
#         print("[" + str("skaicius") + "]", end= " ")
#     else:
#         print(skaicius, end=" ")
# #kiek skaiciu didesni nei 150
# didesni_nei_150 = 0
# for skaicius in skaiciai:
#     if skaicius > 150:
#         didesni_nei_150 += 1
#     print("skaicius, didesni_nei_150, kiekisend:",didesni_nei_150)
#
# skaiciai = []
# for i in range(1,3001):
#      if i % 77 == 0:
#       skaiciai.append(str(i))
#
#       print(",".join(skaiciai))
#
# #nupiesti kvadrata is zvaigzduciu
# for i in range(25):
#     print("*" * 25)
#
# for y in range(25):
#     for x in range(25):
#         if y == x or x == 24 - y:
#             print("X", end=" ")
#         else:
#             print("*", end=" ")
#     print()
# import random
# # kai iskrenta herbas
# while True:
#     metimas = random.randint (0, 1)
#     if metimas == 0:
#         print( "H")
#         break
#     else:
#         print( "S")
# #stabdom kai tris kartus iskrenta herbas
# import random
#
# herbu_kiekis = 0
#
# while herbu_kiekis < 3:
#     metimas = random.randint (0, 1)
#     if metimas == 0:
#         print( "H")
#         herbu_kiekis += 1
#     else:
#         print("S")
# #stabdom kai iskrenta 3 herbai is eiles
# import random
#
# herbu_is_eiles = 0
#
# while herbu_is_eiles < 3:
#     metimas = random.randint (0, 1)
#     if metimas == 0:
#         print( "H")
#         herbu_is_eiles +=1
#     else:
#         print("S")
#         herbu_is_eiles = 0
#
# petras_total = 0
# kazys_total = 0
# partijos_nr = 0
#
#
# while petras_total < 222 and kazys_total < 222:
#     partijos_nr += 1
#     petras_points = random.randint (10, 20)
#     kazys_points = random.randint (5, 25)
#     petras_total += petras_points
#     kazys_total += kazys_points
#
#     if petras_points > kazys_points:
#         print("Partijos nr:", partijos_nr, "laimejo Petras", petras_points)
#     elif kazys_points > petras_total:
#         print("Partijos nr:", partijos_nr, "laimejo Kazys", kazys_points)
#     else:
#         print("Partijos nr:", partijos_nr, "lygiosios " )
#
# print("Petras",petras_total,"Kazys",kazys_total)
# if petras_total > kazys_total:
#     print("laimejo Petras")
# elif petras_total < kazys_total:
#     print("laimejo Kazys")
# else:
#     print("Lygiosios")
#
# import random
# masyvas = [random.randint(5,25) for _ in range(30)]
#
# print(masyvas)
#
# masyvas = [random.randint(5,25) for _ in range(30)]
# kiek_didesniu = sum(1 for skaicius in masyvas if skaicius > 10)
#
# print("masyvas:", masyvas)
# print("reiksmiu didesniu uz 10, skaicius:", kiek_didesniu)
#
# didziausia_reiksme = max(masyvas)
# print("didziausia masyvo reiksme:", didziausia_reiksme)
#
#
# masyvas = [random.randint(5,25) for _ in range(30)]
# naujas_masyvas = [masyvas [i] - i for i in range(len(masyvas))]
# print(masyvas)
# print("naujas_masyvas(reiksme - indeksas):",naujas_masyvas)
#
# for i in range(10):
#     skaicius=random.randint(5,25)
#     masyvas.append(skaicius)
# print(masyvas)
# #pridedam dar 10  skaiciu
#
# #sukuriam du naujus masyvus
#
#
# poriniai = []
# neporiniai = []
# for i in range (40) :
#     if i % 2 == 0:
#         poriniai.append(masyvas[i])
#     else:
#         neporiniai.append(masyvas[i])
# print(poriniai, neporiniai)
#
# for i in range(10):
#     masyvas.append(random.randint(5,25))
# print(masyvas)
# for i in range(0, 10,2):
#     if masyvas[i] > 15:
#         masyvas[i] = 0
# print(masyvas)
#
# #ieskom pirmo indekso,kur reiksme > 10
# for i in range(40) :
#     if masyvas[i] > 10:
#         print("pirmas indeksas,kur reiksme >10:", i)
#
# masyvas = []
# for i in range(200) :
#     raide = random.choice(['A', 'B', 'C','D'])
#     masyvas.append(raide)
# a_kiekis = 0
# b_kiekis = 0
# c_kiekis = 0
# d_kiekis = 0
# for raide in masyvas:
#     if raide == 'A':
#         a_kiekis += 1
#     elif raide == 'B':
#         b_kiekis += 1
#     elif raide == 'C':
#         c_kiekis += 1
#     elif raide == 'D':
#         d_kiekis += 1
# print(masyvas)
# print("A kiekis:", a_kiekis)
# print("B kiekis:", b_kiekis)
# print("C kiekis:", c_kiekis)
# print("D kiekis:", d_kiekis)
#
# #sugeneruojam masyva su 200 atsitiktiniu raidziu A,B,C,D
# masyvas = []
# for i in range(200) :
#     raide = random.choice(['A', 'B', 'C','D'])
#     masyvas.append(raide)
# #rikiavimas pagal abecele
# masyvas.sort()
# print("isrikiuotas masyvas:", masyvas)
#
# masyvas1 = [random.choice(['A', 'B', 'C','D']) for i in range(200)]
# masyvas2 = [random.choice(['A', 'B', 'C','D']) for i in range(200)]
# masyvas3 = [random.choice(['A', 'B', 'C','D']) for i in range(200)]
# sujungtas_masyvas = [masyvas1, masyvas2, masyvas3]
# for i in range(200):
#     kombinacija = masyvas[i] + masyvas2[i] + masyvas3[i]
#     sujungtas_masyvas.append('sujugtas')
# #skirtingos kombinacijos
# skirtingos = []
# for i in range(200):
#     if sujungtas_masyvas[i] not in skirtingos:
#         skirtingos.append(sujungtas_masyvas[i])
# print("skirtingu kombinaciju kiekis", len(skirtingos))
# print("kombinacijos:", skirtingos)
#
# masyvas1 = random.sample(range(100, 1000), 100)
# masyvas2 = random.sample(range(100, 1000), 100)
# print("masyvas1:", masyvas1)
# print("masyvas2:", masyvas2)
#
# tik_pirmame = []
# for skaicius in masyvas1:
#     if skaicius not in masyvas2:
#      tik_pirmame.append(skaicius)
# print(masyvas1)
# print(masyvas2)
# print(tik_pirmame)
#
# kartojasi = []
# for skaicius in masyvas1:
#     if skaicius in masyvas2:
#         kartojasi.append(skaicius)
# print(masyvas1)
# print(masyvas2)
# print(kartojasi)
from operator import truediv


def susumuok(a,b) :
    suma = a + b
    print(suma)


susumuok(2,5)


reiksme = (9.8596)
def pisq() :
    return 9.8596
print(reiksme)

def sandauga(a,b):
    return a * b
rezultatas=sandauga(2,5)
print("sandauga yra:",rezultatas)


skaiciai = [2, 5, 3, 4, 5]


def spausdinti_masyva(masyvas):
    for skaicius in masyvas:
        print(skaicius)

spausdinti_masyva(skaiciai)

import random
def sugeneruoti_skaiciu (min_reiksme,max_reiksme):
    return random.randint(min_reiksme,max_reiksme)
skaicius = sugeneruoti_skaiciu(20,30)
print(skaicius)

def generuoti_masyva (min_reiksme,max_reiksme,length):
    masyvas = []
    for i in range(length):
        skaicius=random.randint(min_reiksme,max_reiksme)
        masyvas.append(skaicius)
        return masyvas
rezultatas = generuoti_masyva(20,30,10)
print(rezultatas)


def susumuoti_masyva(masyvas) :
    suma = sum(masyvas)
    return suma
skaiciai = [20,30,10]
rezultatas = susumuoti_masyva(skaiciai)
print("suma yra", rezultatas)

#Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.

def skaiciuoti_vidurki(masyvas):
    if len(masyvas) == 0:
        return 0
    vidurkis = sum(masyvas)/ len(masyvas)
    return vidurkis
skaiciuoti_vidurki(skaiciai)
print("vidurkis yra", skaiciuoti_vidurki(skaiciai) )

#Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
#Pirmas skaičius- išoriniam ciklui, antras vidiniam.



def spausdinti_staciakampi( eiluciu_skaicius, zvaigzduciu_skaicius):
    for i in range(eiluciu_skaicius):
        for a in range(zvaigzduciu_skaicius):
            print("*", end=" ")
        print()
spausdinti_staciakampi(4,6)


def nagrineti_sakini (sakinys):
    simboliai = 0
    tarpai = 0
    for simbolis in sakinys:
        if simbolis == " ":
           tarpai += 1
    else:
        simboliai += 23
    print("simboliu (be tarpu):", simboliai)
    print ("tarpu:", tarpai)
nagrineti_sakini("siandiena labai grazi diena")

def kodavimas_sakinys(sakinys):
    return sakinys[::-1]

def kodavimas_sakinys_v2(sakinys):
    kodavimas = ""
    for letter in sakinys:
        kodavimas = letter + kodavimas
    return  kodavimas
rezultatas = kodavimas_sakinys("Rima")
print(rezultatas)
print(kodavimas_sakinys_v2("Rima"))

def apsukti_zodzius(sakinys):
    zodziai = sakinys.split()
    apsukti = []
    for zodis in zodziai:
        apsukti.append(zodis[::-1])
    rezultatas = (apsukti)
    print(rezultatas)
apsukti_zodzius("Labas rytas")


def spausdinti_skaicius(sarasas):
    for skaicius in sarasas:
        if type(skaicius) == int:
            print(skaicius)
duomenys = (2,10,15,6, "labas")
spausdinti_skaicius(duomenys)

def spausdinti_sveikus_skaicius(sarasas):
    for zodis in sarasas:
        if type(zodis) == int:
            print(zodis)
duomenys = (2,10,15,6,100, 8 )
spausdinti_sveikus_skaicius(duomenys)


def word_count(tekstas):
    zodziai = tekstas.split()
    return len(zodziai)

sakinys = "siandien sekasi labai gerai"
rezultatas = word_count(sakinys)
print("zodziu skaicius:", rezultatas)


def boolean_skaicius(masyvas,filtruoti_porinius):
    rezultatas = []
    for skaicius in masyvas:
        if filtruoti_porinius == True and skaicius %2 ==0:
            rezultatas.append(skaicius)
        elif filtruoti_porinius == False and skaicius %2 !=0:
            rezultatas.append(skaicius)
    return rezultatas
skaiciai = [2,5,4,6,8]
print(boolean_skaicius(skaiciai,True))
print(boolean_skaicius(skaiciai,False))


def number_is_prime(skaicius):
    if skaicius <2:
        return False
    for k  in range(2,skaicius):
        if skaicius % k == 0:
          return False
    return True
skaiciai = [2,3,5,7,11,12]
for skaicius in skaiciai:
    if number_is_prime(skaicius):
        print(skaicius)

def pakelti_laipsniu(skaicius,laipsnis):
    return skaicius ** laipsnis

rezultatas = pakelti_laipsniu(2,4)
print(rezultatas)

def nepasikartojantys_skaiciai(masyvas):
    return[skaicius for skaicius in masyvas if masyvas.count(skaicius) == 1]
skaiciai = [1,2,2,3,4,4,5,6,6,7,8]
rezultatas = nepasikartojantys_skaiciai(skaiciai)
print(rezultatas)


def daugiausia_simboliu(tekstas) :
    daznis ={}
    print(tekstas)
    for simbolis in tekstas:
        if simbolis in daznis:
            daznis[simbolis] += 1
        else:
            daznis[simbolis] = 1
    daugiausia = 0
    symb = ""
    for simbolis in daznis:
         if daznis[simbolis] > daugiausia:
            daugiausia = daznis[simbolis]
            symb = simbolis
    print(daznis)
    print(daugiausia, symb)
print("simbolis, kuris pasikartoja daugiausia:")
daugiausia_simboliu("as mokausi phyton programavimo")

def spausdink_ilgiausia_zodi(tekstas):
        zodziai = tekstas.replace(", ", "").split()
        ilgiausias = ""
        for zodis in zodziai:
            if len(zodis) > len(ilgiausias):
                ilgiausias = zodis
        print("ilgiausias zodis:",ilgiausias)
spausdink_ilgiausia_zodi("Labas siandien produktyvi diena")

def spausdinti_su_bruksniais(tekstas):
    print (f"---{tekstas}---")
    print(rezultatas)
spausdinti_su_bruksniais("labas")

def dalijasi_be_liekanos(skaicius):
    kiekis=0
    for i in range(2,skaicius):
        if skaicius % i == 0:
            kiekis += 1
    return kiekis
print(dalijasi_be_liekanos(10))
print(dalijasi_be_liekanos(20))

import random
def dalikliai_be_liekanos(skaicius):
    kiekis=0
    for i in range(2,skaicius):
        if skaicius % i == 0:
            kiekis += 1
    return kiekis
masyvas = [random.randint(33,77) for i in range(100)]
rusiuotas = sorted(masyvas, key=dalikliai_be_liekanos, reverse=True)
print("pradinis masyvas:", masyvas)
print(masyvas)
print(" isrikiuotas masyvas pagal dalikliu kieki(mazejancia tvarka):")
print(rusiuotas)

import random
def dalikliai_be_liekanos(skaicius):
    kiekis=0
    for i in range(2,skaicius):
        if skaicius % i == 0:
            kiekis += 1
    return kiekis

masyvas = [random.randint(333,777) for i in range(100)]
pirminiu_kiekis = 0
for skaicius in masyvas:
    if dalikliai_be_liekanos(skaicius) == 0:
        pirminiu_kiekis += 1

print("sugeneruotas masyvas:")
print(masyvas)
print("pirminiu skaiciu kiekis masyve:", pirminiu_kiekis)

























# Dictionary = {"Forename":"Paul", "Surname":"Dinh"}
# KeyList = ["Forename", "Surname"]
# for Key in KeyList:
#     print(Key, "=", Dictionary[Key])
#
# print(Dictionary['Forename'])






























