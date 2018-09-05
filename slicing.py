def newSlice(strIn, sliceAt):

    lastsubstr = ""
    output = []

    for i in range(len(strIn)):
        if strIn[i:i+len(sliceAt)]==sliceAt:
            output.append(lastsubstr)
            lastsubstr = ""
        lastsubstr = lastsubstr + strIn[i]
    output.append(lastsubstr)
    return output

print(newSlice(input("string"),input("slice where?")))