import os
import sys

# add this file to the auto start file list, so that you will use the below link to control nao
# http://nao.local:1111

basedir = sys.path[0]
# command = 'chmod -Rv 777 ' + basedir
# print command
# os.system(command)
path = os.path.join(basedir, "service.py")
command1 = 'cd ' + basedir
print(command1)
command2 = 'python ' + path + " 31415"
print(command2)
os.system(command1)
os.system(command2)
