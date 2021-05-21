# File: MTO.py
# Have to run this script from folder with the txt files!!!
# Abner De Jesus Martinez
# 5/20/2021

import os

path = os.getcwd()                       # file should be where all the text files are
os.chdir(path)

com = open('combined.txt', 'w+')         # create new text file and open as write

for file in os.listdir():                # read files one by one in a loop
    if file.find("th") != -1 :           # check if file has "th" in it
        fpath = f"{path}\{file}"         # puts file name in variable since it will be different every loop
        with open(fpath,'r') as f:       # with opens and then closes the file
            com.write(f.read())          # append entire text to new file
com.close()                              # close combined.txt
