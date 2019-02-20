import random

numlst = random.sample(range(10), 4)
num = ""
for x in numlst:
    num = num + str(x)

def ispartof(_num, lst):
    for x in lst:
        if _num == x:
            return True
    return False

tries = 1

while True:
    ans = input("szám:\t")
    if len(ans) != len(num):
        print("please give a valid answer")
    else:
        if ans == num:
            print("nice! It took you {} tries.".format(tries))
            break
        tries +=1
        cows = 0
        bulls = 0
        for x in range(len(ans)):
            if ans[x] == num[x]:
                bulls += 1
            elif ispartof(ans[x], num):
                cows += 1
        print("cows:{}\tbulls:{}\n".format(str(cows), str(bulls)))
