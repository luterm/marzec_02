import os
import time

print(os.getcwd())
os.mkdir("jeden")
time.sleep(3)
os.rename("jeden","mienso")
time.sleep(7)
os.rmdir("mienso")