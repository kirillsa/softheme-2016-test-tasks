#Prime function
def prime (n):
    import math
    for i in range (2,int(math.sqrt(n))+1):
        if n%i is 0:
            return False
    return True
#---------------main----------------
def main():
    sum = 0
    maxValue = 1000000
    for i in range (2,maxValue+1):
        if prime(i):
            stri = str(i)
            for j in range (len(stri)):
                ch = stri[0]
                stri = stri[1:len(stri)]+ch
                if not prime(int(stri)):
                    break
                elif j is len(stri)-1:
                    sum += 1
                    print (i)
    print (sum, 'circular prime numbers from 1 to', maxValue)
if __name__ == "__main__": main()
