def printNumbers(n):
    if n == 0:
        return
    print(n)
    n -= 1
    printNumbers(n)   

printNumbers(10)