def main():
    print ("Enter:")
    print ("'1' to count small triangle")
    print ("'2' to count big triangle")
    case = 0
    while case is not 1 and case is not 2:
        case = int(input('Make your choise '))
    if case is 1:
        f = open ('Triangle.txt',encoding="utf-8")
    else:
        f = open ('BigTriangle.txt',encoding="utf-8")
    sum = 0
    i = 0
    while 1:
        line = f.readline()
        if line is '':
            break
        List = line.split(' ')
        previ = i-1
        nexti = i+1
        maxNum = int(List[i])
        if previ >= 0:
            if int(List[previ]) > maxNum:
                maxNum = int(List[previ])
                i = previ
        if nexti < len(List):
            if int(List[nexti]) > maxNum:
                maxNum = int(List[nexti])
                i = nexti
        sum += maxNum
    print (sum)
    f.close()
if __name__ == "__main__": main()
