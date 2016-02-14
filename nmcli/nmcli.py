import os
import time
#from termcolor import colored

def choose():
    while(True):
        print ('[ 1 ] Get Wifi Status :')
        print ('[ 2 ] Turn Wifi ON :')
        print ('[ 3 ] Turn Wifi OFF :')
        print ('[ 4 ] Available WiFi List : ')
        print ('[ 5 ] Connect to an Open WiFi :')
        print ('[ 6 ] Connect to a Password Protected WiFi :')
        print ('[ 7 ] Exit ')
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


    

