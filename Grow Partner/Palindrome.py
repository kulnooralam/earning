def is_pd(string):
    string=string.replace("","").lower()
    reversed_string=string[::-1]

    if string==reversed_string:
        return True
    else:
        return False

def main():
    string=input("enter a string")
    if is_pd(string):
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome.")

if __name__=="__main__":
    main()

