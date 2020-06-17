from os import system
from time import sleep
from datetime import datetime
import logging

ip = "8.8.8.8" # Google DNS Server's ip address, commonly used for checking internet connection
dest_path = "D:\\PythonProjects\\NetworkCheck\\" # to maintain log
DateToday = datetime.now().date()

def check_internet(ip):
    return system("ping "+ip) # ping ip to check connection, 0 means succesful connection while 1 means failed connection

def restart_pc():
    system("shutdown /r /t 1") # cmdlet for restarting PC

def maintain_log(log_entry):
    logFile = dest_path + "Network Check Log " + str(DateToday) + ".log"
    logging.basicConfig(filename=logFile, filemode='w', format='%(asctime)s %(message)s')
    logging.warning(log_entry)

def main():
    sleep(60)
    print("Checking Network Status...")
    network_status = check_internet(ip)
    if network_status == 0:
        print("Connection Successful")

    elif network_status == 1:
        print("Connection Failed. Emergency Measures Activated!")
        maintain_log("Connection Failed. Emergency Measures Activated!")
        sleep(900)
        print("Checking Network Status One Final Time...")
        maintain_log("Checking Network Status One Final Time...")
        network_status = check_internet(ip) 
        if network_status == 0:
            print("Connection Successful, Deactivating Emergency Measures")
            maintain_log("Connection Successful, Deactivating Emergency Measures")
        elif network_status == 1:
            print("Forcing Reboot...")
            maintain_log("Forcing Reboot...")
            sleep(10)
            restart_pc()

while True:
    main()