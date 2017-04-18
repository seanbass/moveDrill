import sys
import os
import inspect
import shutil


shutil.move("/Users/seanbass/Desktop/A/One.txt", "/Users/seanbass/Desktop/B/One.txt")
print (os.path.realpath(__file__)) 

shutil.move("/Users/seanbass/Desktop/A/Two.txt", "/Users/seanbass/Desktop/B/Two.txt")
print (os.path.realpath(__file__))  

shutil.move("/Users/seanbass/Desktop/A/Three.txt", "/Users/seanbass/Desktop/B/Three.txt")
print (os.path.realpath(__file__))  

shutil.move("/Users/seanbass/Desktop/A/Four.txt", "/Users/seanbass/Desktop/B/Four.txt")
print (os.path.realpath(__file__))  
