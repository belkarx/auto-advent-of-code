#!/usr/bin/env python3
from datetime import date
from selenium import webdriver
import time
import subprocess
from sys import argv

lang = "py"
try:
    day = abs(int(argv[1]))
except:
    today = date.today()
    day = int(today.strftime("%d"))

def authAndSave():
    driver = webdriver.Firefox()
    driver.get("https://adventofcode.com/2020/auth/github")

    uname = ""
    passwd = ""

    driver.find_element_by_xpath("//*[@id=\"login_field\"]").send_keys(uname)
    driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(passwd)
    driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[3]/input[12]").click() 
    time.sleep(2)

    input_url = "https://adventofcode.com/2020/day/" + str(day) + "/input"

    driver.get(input_url)
    inp = driver.find_element_by_css_selector("pre")
    inp = inp.get_attribute('innerHTML')
    driver.quit()

    with open(f"/home/uk000/Code/Python/Advent of Code/input{day}.txt", 'w+') as f:
        f.write(inp)

def openApps():
    p = subprocess.Popen(f"code /home/uk000/Code/Python/Advent\ of\ Code/Day{day}.{lang}", shell=True)
    time.sleep(1)
    p.terminate()
    p = subprocess.Popen(f"gedit /home/uk000/Code/Python/Advent\ of\ Code/input{day}.txt", shell=True)
    time.sleep(1)
    p.terminate()
    p = subprocess.Popen("firefox https://adventofcode.com/2020/auth/login", shell=True)
    time.sleep(1)
    p.terminate()

authAndSave()
openApps()
