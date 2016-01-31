import os
import time
from termcolor import colored

def choose():
    while(True):
        print colored('[ 1 ]','blue'),colored("Get Wifi Status :",'green')
        print colored('[ 2 ]','blue'),colored("Turn Wifi ON ",'green')
        print colored('[ 3 ]','blue'),colored("Turn Wifi OFF ",'green')
        print colored('[ 4 ]','blue'),colored("Available WiFi List : ",'green')
        print colored('[ 5 ]','blue'),colored("Connect to an Open WiFi :",'green')
        print colored('[ 6 ]','blue'),colored("Connect to a Password Protected WiFi :",'green')
        print colored('[ 7 ]','red'),colored("Exit",'red')
        #print colored('[ 9 ]','blue'),colored("Help",'green')

        print

        choice =int( raw_input("Enter Your Choice:"))

        if(choice ==1):
            os.system("nmcli radio wifi")
            print("If it Disabled then Turn it On using 2nd option")
            print("")
            
        elif(choice ==2):
            os.system("nmcli radio wifi on")
            print("Turned On")
            print("")
        elif(choice ==3):
            os.system("nmcli radio wifi off")
            print("Turned Off")
            print("")
        elif(choice == 4):
            print("Rescanning....")
            os.system("clear")
            os.system("nmcli device wifi list")
        
        elif(choice ==5):       
            Id = raw_input("Enter the SSID or BSSID :")

            os.system("nmcli device wifi connect "+ Id)
        elif(choice ==6):       
            Id = raw_input("Enter the SSID or BSSID :")
            print("")
            password = raw_input("Enter the password :")

            os.system("nmcli device wifi connect "+ Id +" password "+password)
        elif (choice == 7):
            exit(1)
        else:
            print("Wrong Input Please try again!!!")



if __name__ =="__main__":
    choose()


    

