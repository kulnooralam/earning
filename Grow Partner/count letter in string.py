def count(string,letter):
    count=0
    for char in string:
        if char==letter:
            count+=1
    return count

def main():
    string=input("Enter a string:")
    letter=input("Enter a letter:")

    occurence=count(string,letter)
    print(f"The letter '{letter}'occurs {occurence} times in the string.")

if __name__=="__main__":
    main()
    












