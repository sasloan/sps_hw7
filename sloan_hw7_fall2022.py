# Problem 1

header1 = """Welcome the Multiples Program! In this program you will input \n
              two numbers. Your first number will be what you want the second \n
              number to be divided by. Then we will output all the numbers that \n
              you can divide your first number by in order for it to equal your \n
              number. Please note that the numbers must be below 500 and if they \n
              are not perfectly divisable thenwe will only show numbers that \n
              are divisable up to the first number with NO REMAINDERS! Thank you \n
              and enjoy!"""
              
print(header1)
print(" ")
print(" ")

firstnum = input("Please enter an INTEGER that is between 1 and 500: ")
secondnum = input("Please enter a INTEGER number you want to divide by: ")

wordCheck = 1

while(wordCheck <= int(firstnum)):
    
    if(wordCheck % int(secondnum) == 0):
        
        print(wordCheck)
        
    wordCheck = wordCheck + 1
    

# Problem 2.a

header2a = """Welcome to the number calculators. This program will take two numbers \n
That you input and create a range between them and then give you the total of \n
those numbers and the count of the numbers in the range!"""

print(header2a)
print("")
print("")
print("")

upperAlimit = input("Please Input your first number between 0 and 100: ")
lowerAlimit = input("Please Input your second number between 0 and 100: ")

while(int(upperAlimit) and int(lowerAlimit) < 100):

    inputRange = range(int(upperAlimit),int(lowerAlimit))

    userInputList = list(inputRange)

    totalOfList = sum(userInputList)

    amountOfVariables = len(userInputList)
    
    print("")
    print("")
    print(f"The Numbers between your selections are: {userInputList}")
    print("These numbers are your Range.")
    print("")
    print(f"The Total amount of the Range you inputted is: {totalOfList}")
    print("")
    print(f"The Total count of variables in the Range you inputted is: {amountOfVariables}")
    
    print("")
    print("")
    
    upperAlimit = int(input("Please Input your first number between 0 and 100: "))
    lowerAlimit = int(input("Please Input your second number between 0 and 100: "))

else:
    print("")
    print("")
    print("Please re-read the directions and try again. ")

        
# Problem 2.b


header2b = """Welcome to the Range analyser! the program that takes your input \n
and tells you the middle number of your range, the count of your Range and the \n
sum of your range!! Please start by entering two numbers between 0 and 100."""

print(header2b)
print("")
print("")
print("")

upperBLimit = input("Please enter in your first number between 0 and 100: ")
lowerBLimit = input("Please enter in your second number between 0 and 100: ")

upperAndLowerRange = range(int(upperBLimit), int(lowerBLimit))

userList = list(upperAndLowerRange)

for userNum in userList:
    
    print("")
    print(f"The number in the middle of your range is: {((len(userList))/2)+1}")
    print("")
    print(f"The count of the range you entered is: {len(userList)}")
    print("")
    print(f"The sum of the range you entered is: {sum(userList)}")
    break

# Problem 3


header3 = """Welcome to the sentance analyser program. We start by inputing a \n
sentance and then the analyser will read your sentance and output if if it \n
is a letter, and if so then it will output the lower and capital versions of \n
the letter, if it is a digit then it will output the digit and the squar of the \n
digit and finally if it is a space then it will out put the space and if it is \n
a special character then it will output the special character!"""

print(header3)

print("")
print("")
print("")

userSentance = input("Please input your Sentance here: ")

for character in userSentance:
    
    if(character.isalpha()):
        
        print(character.lower())
        print("")
        print(character.upper())
        print("")
    
    elif(character.isnumeric()):
        
        print(float(character))
        print("")
        print(pow(float(character),2))
        print("")
        
    elif(character == ' '):
        
        print("SPACE")
        print("")
        
    else:
        
        print(f"{character} is a special character.")
        
# Problem 4

header4 = """Welcome to the input number Analyser, you can put in several numbers \n
and when you say "done" then the system will take all that you inputed and give \n
you the count of numbers you inputted, the sum of the numbers that you input \n
and the average of the numbers that you inputted. Enjoy!

Enter "done" when finished inputing numbers"""

print(header4)
print("")

userList = input("Please input your first number here: ")
count = 0
total = 0

while(userList != "done"):
    
    count = count + 1
    total = total + float(userList)

    userList = input("Please input your next number here: ")
    print("")
    
average = total / count
    
print(f"You have inputted {count} numbers.")
print("")
print(f"The total amount of all the numbers you inputted is: {total}")
print("")
print(f"The average amount of the numbers you inputted is: {average:.2f} ")
    


    
        
    
    
        
  

