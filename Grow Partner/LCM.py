def find_lcm(n1,n2):
    max_num=max(n1,n2)
    lcm=max_num

    while True:
        if lcm%n1==0 and lcm%n2==0:
            break
        lcm+=max_num

    return lcm

n1=int(input("Enter first  number:"))
n2=int(input("Enter second number:"))

lcm=find_lcm(n1,n2)
print(f"The Lcm of {n1} and {n2} is {lcm},")
