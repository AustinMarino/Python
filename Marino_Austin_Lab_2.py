# Name: Austin Marino
# Date: 10/24/2019
# Subject: CYB 107
# Description: This program using multiple access and mutator methods to manipulate a user's account information.
# The program also uses three different imported modules, math, random, and logging. These modules allowed the author to create
# a randomly generated debit card for the user (if requested) and also allowed the user to round their annual
# interest earnings to two decimal places. When a new debit card is requested by the user, the logging module
# takes the randomly generated card number and logs it to a file located on the user's Desktop.
# The overall use of this program is for a user to enter an account number,
# enter a savings account amount, and enter a desired annual interest rate. Upon completion, the student is given,
# the total earnings per month while holding their money in a savings account. From a bankers perspective, this code
# also provides logging timestamps for when new debit cards were distributed. 

import math
import random
import logging

class Account:

    def __init__(self, idNum = 0, bal = 0, annualInterest = 0.0):
        self.__id = idNum
        self.__balance = bal
        self.__annualInterestRate = annualInterest

    def getID(self):
        return self.__id

    def setID(self, idNum):
        self.__id = idNum

    def getBalance(self):
        return self.__balance

    def setBalance(self, total):
        self.__balance = bal

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, rate):
        self.__annualInterestRate = annualInterest

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate /100 /12

    def getMonthlyInterest(self):
        monthlyInterest = self.__balance * self.getMonthlyInterestRate()
        return round(monthlyInterest, 2)

LOG_FORMAT = '%(levelname)s:%(asctime)s:%(message)s'
logging.basicConfig(filename='C:\\Users\\austy\\Desktop\\DebitCards.log', level=logging.DEBUG , format=LOG_FORMAT)
logger = logging.getLogger

account = 3
while account == 3:
    account = input("Enter account number: ")
    try:
        account = int(account)
    except ValueError:
        print("")
        print("Invalid input")
        print("User ID is integers only")
        print("Example: 12345612312")
        print("")
        account = 3

balance = 3
while balance == 3:
    balance = input("Enter savings account balance: ")
    try:
        balance = float(balance)
    except ValueError:
        print("")
        print("Invalid input")
        print("User balance can be integers or decimals only.")
        print("Example: 2000.25")
        print("")
        balance = 3

interest = 3
while interest == 3:
    interest = input("Enter your annual interest rate: ")
    try:
        interest = float(interest)
    except ValueError:
        print("")
        print("Invalid input")
        print("Interest rates can be integers or decimals only.")
        print("Example: 4.5")
        print("")
        interest = 3

austinAccount = (Account(account, balance, interest))

print("")
print("Account ID: $", austinAccount.getID())
print("Savings account balance: $", austinAccount.getBalance())
print("Annual interest Rate:", austinAccount.getAnnualInterestRate())
print("Interest earned (Monthly): $", austinAccount.getMonthlyInterest())
print("")


newCard = 3
while newCard == 3:
    newCard = input("Would you like a new debit card? (1 = Yes, 2 = No): ")
    try:
        newCard = int(newCard)
        if newCard == 1:
            debitCard = random.randint(1000000000000000, 9999999999999999)
            print("New Debit Card:", debitCard)
            logger = logging.getLogger()
            logger.info("DebitCardNumber: " + str(debitCard))
        elif newCard == 2:
            print("Have a nice day!")
        else:
            print("Invalid input")
            newCard = 3
    except ValueError:
        print("")
        print("Invalid input")
        print("1 = Yes, 2 = No")
        print("")
        newCard = 3

