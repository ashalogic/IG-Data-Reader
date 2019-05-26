import os
import sys
import json

if(len(sys.argv) < 2):
    print("Please give file name as argv for ex : main datafolder")
    exit()

path = "./"+sys.argv[1]+"/"
print("Collect data from directory " + path)

print(os.listdir(path))
