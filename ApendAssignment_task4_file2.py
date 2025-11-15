""" Append to file"""
from os import close

fh=open("myfile_1.txt","wt")
fh.write("Hello World")
#fh=open("myfile_1.txt","at")
try:
    fh=open("myfile_1.txt","at")
    fh.write("Good Afternon")
    fh.readline()
except IOError:
    print("File does not exist")
fh.close()