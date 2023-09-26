print("Program to check the number is odd or even")
def check_even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

def main():    
    num=int(input("Enter a number:")) 
    result=check_even_odd(num)
    print(f"The number {num} is {result}.")
if __name__=="__main__":
    main()
