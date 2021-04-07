import random
import datetime

myDatabase = {}

def init():
    isValidOptionSelected = False
    print("Welcome to Peenarz-Bank")
    
    while isValidOptionSelected == False:
        haveAccount = int(input("Do you have account with us?: 1 (Yes) 2 (No) \n"))

        if(haveAccount == 1):
            customerLogin()

        elif(haveAccount == 2):
            customerRegister()

        else:
            print("Invalid Option selected")       




def customerLogin():
    print("********** Online Login **********")
    print("Welcome Back")

    isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberInputedByUser = int(input("Enter your account number \n"))
        userPassword = input("Enter your paasword \n")
        


## looping througgh the database dictionary

        for accountNumber, userDetails in myDatabase.items():
            if(accountNumber == accountNumberInputedByUser):
                if(userDetails[3] == userPassword):
                    isLoginSuccessful = True
                    bankOperation(userDetails)
            else:
              print("Invalid account or password")

    


def customerRegister():
    print("****** Register ******")

    first_name = input("What is your First name \n")
    last_name = input("What is your Last name \n")
    email = input("What is your email \n")
    createPassword = input("Create your password \n")
    confirmPassword = input("Confirm password \n")

    if(createPassword != confirmPassword):
        print("Password does not match")
        customerRegister()

    accountNumber = generateAccountNumber()

    myDatabase[accountNumber] = [first_name, last_name, email, createPassword]

    print("Your account number: %d" % accountNumber)
    print("Stay Safe and enjoy banking with us!!")

    customerLogin()
    


def bankOperation(customer):
    currentDateAndTime = datetime.datetime.now()
    theCurrentHour = currentDateAndTime.strftime("%H")
    if(int(theCurrentHour) == 24 or int(theCurrentHour) >= 1 and int(theCurrentHour) < 12):
        print("Good Morning & Welcome %s %s" % (customer[0], customer[1]))

    elif(int(theCurrentHour) >= 12 and int(theCurrentHour) <= 17):
        print("Good Afternoon & Welcome %s %s" % (customer[0], customer[1]))
    
    else:
        print("Good Evening & Welcome %s %s" % (customer[0], customer[1]))

    

    selectedOption = int(input("what would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
       depositOperation()

    elif(selectedOption == 2):
       withdrawalOperation()  

    elif(selectedOption == 3):
       customerLogout() 

    elif(selectedOption == 4):
       print("Invalid option selected")
       bankOperation(customer)






def depositOperation():
    amountToDeposit = int(input("How much would you like to deposit? \n"))
    print("Your current balance is %d" % amountToDeposit)
    byeMessageToUser()


def withdrawalOperation():
    int(input("How much would you like to Withdraw ? \n"))
    print("Kindly take your cash")
    byeMessageToUser()
    

def customerLogout():
    customerLogin()



def generateAccountNumber():
    return random.randrange(1111111111,9999999999)


def byeMessageToUser():
    print("Thank you for using our service, Byee!!")




init()