#Changes Decimal to binary
def dec_to_bin(x):
    #Changes the string input to a integer input
    x = int(x)
    #creates an empty list 
    List=[]
    #A loop to iterate through the number until it is less than 0
    while (x>0):
        #the next few lines are the conversions of the decimal number to the binary number
        a=int(float(x%2))
        List.append(a)
        x=(x-a)/2
    List.append(0)
    string=""
    #loop that adds the strings together
    for j in List[::-1]:
        string=string+str(j)
    #Print statment for the binary number
    print(string)

#changes hex to decimal 
def dec_to_hex(n):
    #converts the string value to a decimal
    n = int(n)
    #checks if the n value is less than or equal to 0 if so it prints 0
    if (n <= 0):
        print(0)
    #Checks if the value is greater than 0 if so it prints it
    elif (n <= 1):
        print ,
    #If neither case works it then prints out the letter value for the corresponding number
    else:
        t = int(n/16)
        print(t, end="")
        x =(n % 16)

        if (x == 10):
            print("A"),

        if (x == 11):
            print("B"),

        if (x == 12):
            print("C"),

        if (x == 13):
            print("D"),

        if (x == 14):
            print("E"),

        if (x == 15):
            print ("F"),

#Changes binary to decimal
def bin_to_dec(x):
    #Converts a string to an int
   x = int(x)
   #creates a variable string that stores the vstring x
   string = str(x)
   #gets the length of string x
   length = len(string)-1
   #sets the index and the decimal value to 0
   index = 0
   decVal = 0
   #iterates through changing the binary number to the decimal value
   while length >= 0:
       num = int(string[index])
       decVal += (num * 2**length)
       length -= 1
       index += 1
   print(decVal)
   return decVal

#changes hex numbers to decimal numbers
def hex_to_dec(x):
    #cretaes a string variable and stors x into it
    string = x

    #gets the length of the string
    count = len(string) - 1

    #storage variables used for index and decVal
    index = 0
    decVal = 0

    #loops through and changes hexadecimal to decimal
    while count >= 0:    
        num = string[index]
        if num == 'A' or num == 'a':
            decVal += (10 * 16**count)
        elif num == 'B' or num =='b':
            decVal += (11 * 16**count) 
        elif num == 'C' or num == 'c':
            decVal += (12 * 16**count)
        elif num == 'D' or num =='d':
            decVal += (13 * 16**count)
        elif num == 'E' or num =='e':
            decVal += (14 * 16**count)
        elif num == 'F' or num =='f':
            decVal += (15 * 16**count)
        elif num == 'G' or num =='g':
            decVal += (16 * 16**count)
        else:
            num = int(string[index])
            decVal += (num * 16**count)
        count -= 1
        index += 1
    print(decVal)
    return decVal

   

    #Canges a twoc complement to a 
def two_to_dec(binarySequence):
    convertedSequence = [0] * len(binarySequence)
    carryBit = 1
    #check to see if the binary is a positive or negative
    if binarySequence[0] != '0':            
        # INVERT THE BITS
        for i in range(0, len(binarySequence)):
             i binarySequence[i] == '0':
                convertedSequence[i] = 1
            else:
                convertedSequence[i] = 0
                
        # ADD BINARY DIGIT 1
        #if last digit is 0, just add the 1 then there's no carry bit so return
        if convertedSequence[-1] == 0: 
                convertedSequence[-1] = 1
                st = ''.join(str(e) for e in convertedSequence)
                bin_to_dec(st)
        for bit in range(0, len(binarySequence)):
            if carryBit == 0:
                break
            index = len(binarySequence) - bit - 1
            if convertedSequence[index] == 1:
                convertedSequence[index] = 0
                carryBit = 1
            else:
                convertedSequence[index] = 1
                carryBit = 0
                
    if binarySequence[0] != '0':        #if negative binary then use a different list
        st = ''.join(str(e) for e in convertedSequence)
    elif binarySequence[0] == '0':      #elif positive binary then use orginal list
        st = binarySequence
    #converts st into a int number
    x = int(st)
    #sets the variable equal to a string x
    string = str(x)
    #gets the length of the string
    length = len(string)-1
    #variables for storing data
    index = 0
    dec = 0
       #loops through binary to change to decimals
    while length >= 0:            
       num = int(string[index])
       dec = dec + (num * 2**length)
       length -= 1
       index += 1
    if binarySequence[0] == "1":
        print("-"+ str(dec))
    else:
        print(dec)

def menu():
    print("1. Decimal to binary")
    print("2. Decimal to hexadecimal")
    print("3. Binary to decimal")
    print("4. Hexadecimal to decimal")
    print("5. Twos complement to Decimal")
    print("6. Run Test cases")
    print("7. Exit")

def test():
     dec_to_bin("5")
     dec_to_bin("0")
     dec_to_hex("31")
     dec_to_hex("0") 
     bin_to_dec("101")
     bin_to_dec("000") 
     hex_to_dec("1F")
     hex_to_dec("000") 
     two_to_dec("00101100")
     two_to_dec("11110000")

def main():
    while(True):
        print()
        menu()
        choice = int(input())    
        if choice == 1:
            n=input("please enter the number in decimal format: ")
            dec_to_bin(n)    
        elif choice == 2:
             n=input("please enter the number in decimal format: ")
             dec_to_hex(n)
        elif choice == 3:
             n = input("please enter the number in binary format: ")
             bin_to_dec(n)
        elif choice == 4:
             n = input("please enter the number in hexadecimal format: ")
             hex_to_dec(n)
        elif choice == 5:
             n=input("please enter the two's comeplement of a: ")
             two_to_dec(n)
        elif choice == 6:
            test()  
        elif choice == 7:
            break

if __name__ == "__main__":
    main()
