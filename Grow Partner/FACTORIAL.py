def factorial(N):
    fact=1
    ans=1
    while ans<=N:
        fact=fact*ans
        ans=ans+1
    print("factoral of an number:",fact)

def main():
    N=int(input("Enter number whose factorial is to be calculated: "))
    factorial(N)

if __name__=="__main__":
    main()
