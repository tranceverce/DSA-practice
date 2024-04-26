def pattern1(n):
    for i in range(n):
        print(str(n)*n)


def pattern2(n):
    for i in range(n+1):
        for j in range(i):
            print("*",end='')
        print()


def pattern3(n):
    for i in range(n+1):
        for j in range(i):
            print(i,end='')
        print()


def pattern4(n):
    for i in range(1,n+1):
        for j in range(i,0,-1):
            print(j,end='')
        print()


def pattern5(n):
    for i in range(1,n+1):
            print((n-i+1)*" ",end='')
            print("*"*(2*i-1),end='')
            print()


def pattern6(n):
    for i in range(1,n+2):
        print((n-i+1)*" ",end='')
        for j in range(1,i):
            print(j,end="")
        print()


def pattern7(n):
    for i in range(n+1,1,-1):
        for j in range(1,i):
            print(j,end="")

        print()


def pattern8(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end="")

        print()

def pattern9(n):
    for i in range(1,(n-(n//2)+1)):
        print((n-i+1)*" ",end='')
        print("*"*(2*i-1),end='')
        print()

    for i in range(0,(n-(n//2))):
        print("@"," "*(n-2),"@")
        



pattern1(4)
print()
pattern2(4)
print()
pattern3(4)
print()
pattern4(4)
print()
pattern5(4)
print()
pattern6(4)
print()
pattern7(4)


print("pattern9")
pattern9(5)