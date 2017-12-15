__author__ = 'dishantrathi'
class Help:
    def Help(self):
        print()
        print()
        print("Voila : You are in the help section")
        print()
        print("This App gives live Exchange Rates of Crypto Currencies Like BTC, ETH, LTC etc. in respect to your desired required currency.")
        print()
        print("From The Main App select 'Option 2' and type CryptoCurrency with required Currency")
        print("For Example")
        print("")
        print("'BTCINR' : Will Get current exchange rates of Crypto Currency Bitcoin 'BTC' in Indian National Rupee")
        print("'LTCUSD' : Will Get current exchange rates of Crypto Currency Bitcoin 'LTC' in US Dollar")
        print()
        print("To Exit : Press CTRL + C Keys to Break and press 5 to Exit")
        print()
        print()
        return self
    def Prerequirements(self):
        print("Pre Requirements Are")
        print()
        print("1. Request Framework")
        print("Run this Command : 'pip install requests' in CMD")
        print("Refer For More : http://docs.python-requests.org/en/master/user/install/")
        print()
        print("2. SICCipy")
        print("To check whether the app has Internet Connection or Not")
        print("Refer for More : https://github.com/dishantrathi/SICCiPy")
        print()
        print()
        return self

#Help = Help()
#Help.Help()
#Help.Prerequirements()