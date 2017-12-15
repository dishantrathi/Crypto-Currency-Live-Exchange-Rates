__author__ = 'dishantrathi'
from SICCipy.SICCipy import CheckConnection
from CurrencySelection.CurrencySelection import CurrencySelection
from Help.Help import Help
from Credits.Credits import Credits                                                                                                                                       
print()
print("Welcome to Live Exchange Rates of Crypto-Currencies , To Begin")
while True:
    print("Menu :")
    print("Enter 1 : To Check Internet Connection")#SICCipy.py Used @Author : Dishant Rathi
    print("Enter 2 : To Start Getting Live Exchange Rates")
    print("Enter 3 : To Display Help")
    print("Enter 4 : For Credits")
    print("Enter 5 : Exit Use CTRL + C To Break and Exit The Program Anytime")
    print()
    
    userChoice = int(input())
    if userChoice is 1:
        print()
        checkconnection = CheckConnection()
        checkconnection.CheckConnection()
        print()
    elif userChoice is 2:
        print()
        CurrencySelectionObject = CurrencySelection()
        CurrencySelectionObject.CurrencySelection()
        print()
    elif userChoice is 3:
        Help = Help()
        Help.Help()
        Help.Prerequirements()
    elif userChoice is 4:
        Credits = Credits()
        Credits.Credits()
    elif userChoice is 5:
        quit()
    else:
        print()
        print("Wrong Choice")
        print()