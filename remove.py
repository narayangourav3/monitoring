import glob, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

InstalledBot = os.system("ls Support*.exe >url.txt")
f = open("url.txt", "r")
time.sleep(5)
g = f.read()
h = (g[0:47])
print(h)
os.system(h + ' /uninstall /quiet /passive')
time.sleep(11)
removeBotName=os.system('rm '+ h)
time.sleep(3)
ClearReport= os.system("rm Report/*")

