__author__ = 'dishantrathi'
import requests

class CheckConnection:
    def CheckConnection(self):
        try :
            internetEnable = requests.get('https://www.google.com/') #Website -- #use google.com as default
            iE = internetEnable.status_code
            if iE == 200: #Response Status Code [May Differ]
                print("Internet Enabled")
            else:
                pass
        except Exception: #if doesn't work then remove "Exception"
            print("No Internet Connection : Check Your Lan | WiFi | Modem | Router Connections For More")

#CheckConnectionObject = CheckConnection() #Calling Class
#CheckConnectionObject.CheckConnection() #Calling Method