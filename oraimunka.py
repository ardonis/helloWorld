import random

""" lst = [str(x) for x in range(1,11) if x%2 == 0]

print(" ".join(lst)) """


def randNums():
    rndlist = []

    for x in range(100):
        rndlist.append(random.randrange(100))
    return rndlist


""" nums = 0
for x in randNums():
    if x%2==0:
        nums = nums+1

print(str(nums))

print("az összeg: {}".format(sum(range(1, 501)))) """

print(max(randNums()))


randNums = []
for x in range(10):
    randNums.append(random.randrange(65, 91))

low = 0
med = 0
for x in randNums:
    if x >= 65 and x < 70:
        low = low+1
    if x >= 70 and x < 80:
        med = med+1

print("kis számok: {}\nközepes számok: {}".format(low, med))


"HF: 1950-ben betettem pénzt a bankba, kamat 2%"
"30 véletlen szám 50-100. páros vagy páratlan a több?"
"beadott szóban az 'e' -> '?'"
