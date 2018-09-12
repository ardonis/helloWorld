def newSlice(strIn, sliceAt):

    lastsubstr = ""

    output = []

    for i in range(len(strIn)):

        lastsubstr = lastsubstr + strIn[i]
        if strIn[i:i+len(sliceAt)] == sliceAt:
            output.append(lastsubstr)
            lastsubstr = ""

    output.append(lastsubstr)

    return output


print(newSlice(input("string"), input("slice where?")))
