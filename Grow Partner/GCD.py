def find_gcd(n1,n2):
    
    while n2 !=0:
       temp=n2
       n2=n1%n2
       n1=temp

    return n1

n1=int(input("Enter first  number:"))
n2=int(input("Enter second number:"))

gcd=find_gcd(n1,n2)
print(f"The Gcd of {n1} and {n2} is {gcd},")
