import random
import time
import os
import requests
import string
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def start():
    
    os.system('color')
    
    with open('proxies.txt') as d:
        proxys = d.readlines()
    
    
    
    while True:
        
        code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        
        randomproxy = random.choice(proxys)
        
        print(randomproxy)
        
        proxies = {
            "http": "http://" + randomproxy
        }
        
        r = requests.get(url, proxies=proxies)
        
        if r.status_code == 200:
            print(" ")
            print(f"{bcolors.OKGREEN} Valid | {bcolors.OKCYAN + code} - {bcolors.OKBLUE + str(r.status_code) + bcolors.ENDC}")
            print(" ")
            
            f = open("nitrolinks.txt", "a")
            f.write("\n" + url)
            f.close()
            
            time.sleep(10)
            
        elif r.status_code == 429:
            print(f"{bcolors.FAIL} Error | Too many attempts - {bcolors.WARNING + str(r.status_code) + bcolors.ENDC}")
            time.sleep(1)
            
        else:
            print(f"{bcolors.FAIL} Invalid | {bcolors.OKCYAN + code} - {bcolors.WARNING + str(r.status_code) + bcolors.ENDC}")
            time.sleep(1)


def reallystart():
    
    os.system('color')
    
    with open('proxies.txt') as d:
        proxys = d.readlines()
    
    driver = uc.Chrome()
    
    while True:
    
        code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        
        url = "https://discord.com/gifts/" + code
        
        
        driver.get(url)
        
        try:
            #Anfang
            
            time.sleep(2)
            
            driver.find_element(By.XPATH, ("//div[text()='Login']/..")).click()
            
            #Ende
            
            
            print(" ")
            print(f"{bcolors.OKGREEN} Valid | {bcolors.OKCYAN + code + bcolors.ENDC}")
            print(" ")
            
            f = open("nitrolinks.txt", "a")
            f.write("\n" + url)
            f.close()
            
            time.sleep(10)
            
            
        except:
            print(f"{bcolors.FAIL} Invalid | {bcolors.OKCYAN + code}{bcolors.ENDC}")
            time.sleep(1)
    

reallystart()