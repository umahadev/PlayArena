#
#  Prime Number List program
#  
#  Copyright 2019 Ulaga Nathan Mahadevan
#  
#  
#  


def main(args):
    user_input = input ("This program will list all the prime number between 0 and the given number. Please enter the number ")
    if type(user_input) != int:
        print("Not an integer")
        return 0
    val = int(user_input)
    if val < 2:
        print ("Please try the number > 1")
    else:
        print listAllPrimeNumbers(val)
    return 0

def listAllPrimeNumbers(num):
    primeList = []
    nonPrimeList = [0,1] 
    if num == 2:
        primeList = [2]
        return primeList
    
    i = 2
    while i <= num:
        j = 2
        flag = True
        while j <= i/2:
            if i % j == 0:
                nonPrimeList.append(i)
                flag = False
                break
            j = j + 1
        if flag:
            primeList.append(i)
        i = i + 1
    return primeList        
        
        
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

