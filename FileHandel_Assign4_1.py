"""Assignment 4 File Handle"""
fh=open("sample.txt","wt")
fh.write("This is a sample file.")
fh.write("Sabinay Swain")
try:
    fh=open("sample.txt","rt")
    print(fh.readline())
except IOError:
        print("File does not exist.")
fh.close()
