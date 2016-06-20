import os
import sys

basedir = sys.path[0]

# command = 'chmod -Rv 777 ' + basedir
# print command
# os.system(command)
path = os.path.join(basedir, "service.py")
command1 = 'cd ' + basedir
print(command1)
command2 = 'python '+path + " 1111"
print(command2)
os.system(command1)
os.system(command2)