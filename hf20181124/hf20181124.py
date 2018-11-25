feladatszam = 0

def ujfeladat():
    global feladatszam
    feladatszam += 1
    print("\n" + str(feladatszam) + ". feladat\n")

ujfeladat()

with open("C:\\Users\\Zsolti\\Documents\\scripts\\python\\hf20181124\\szavazatok.txt", "r", encoding = "utf-8") as f:
    szoveg = f.read().rstrip()
    sorok = [x.rstrip() for x in szoveg.split("\n")]
    print(szoveg)


class jelolt:
    def __init__(self, _korzet, _szavazatok, _nev, _part):
        self.korzet = _korzet
        self.szavazatok = _szavazatok
        self.nev = _nev
        self.part = _part

jeloltek = []
_jelolt = []

for x in sorok:
    _jelolt = x.split()
    __jelolt = jelolt(_jelolt[0], int(_jelolt[1]), _jelolt[2] + " " + _jelolt[3], _jelolt[4])
    jeloltek.append(__jelolt)

ujfeladat()

print(str(len(jeloltek)) + " jelölt van")

ujfeladat()

zep = 0
for x in jeloltek:
    if x.part == "ZEP":
        zep += 1

print(str(zep) + " jelölt")

ujfeladat()

f = [0] * 8
for x in jeloltek:
    f[int(x.korzet) - 1] += 1

for x in range(len(f)):
    print("A(z) {}. körzetből {}-an vannak".format(str(x + 1), str(f[x])))


ujfeladat()


l = jeloltek[0]
for x in jeloltek:
    if x.szavazatok < l.szavazatok:
        l = x

print(l.nev)

ujfeladat()

for x in jeloltek:
    if x.part == "-":
        print(x.nev)

ujfeladat()

sz = 0
for x in jeloltek:
    if x.part == "HEP":
        sz += x.szavazatok

print(str(sz) + " szavazatot")


ujfeladat()

p = input("Adjon meg egy pártot: ")
sz = 0
for x in jeloltek:
    if x.part == p:
        sz += x.szavazatok

print("A(z) {} párt {} szavazatot kapott.".format(p, str(sz)))


ujfeladat()

for x in jeloltek:
    if x.nev[0] == "M":
        print(x.nev)

ujfeladat()

f = open("C:\\Users\\Zsolti\\Documents\\scripts\\python\\hf20181124\\nevek.txt", "w+")

for x in jeloltek:
    f.write(x.nev + "\n")