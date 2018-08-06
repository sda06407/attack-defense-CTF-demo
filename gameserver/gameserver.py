#import trololol_put
#import trololol_get
import hashlib
import random
import string
import time
import os
import binascii
##
# Get random string
##


os.system("mkdir flag")
fo = open("teams.list", "r")
teams=[]


for team in fo.readlines():
    teams.append(team[:-1])
    ff = open("./flag/"+team[:-1]+".flag", "w")
    ff.close()

for team in teams:
    print team
    #m = hashlib.md5()
    #m.update(randomString(100))

    for otherteam in teams:
        if otherteam != teams:
            flag = binascii.b2a_hex(os.urandom(16))
            ff = open("./flag/"+otherteam+".flag", "w")
            fg = open("./flag/"+otherteam+".sent", "w")
            ff.write(flag+"\n")
            fg.write(flag+"\n")
            ff.close()
            fg.close()
        
        else:
            flag = binascii.b2a_hex(os.urandom(16))
            ff = open("./flag/"+otherteam+".flag", "w")
            ff.write(flag+"\n")
            fg = open("./flag/"+otherteam+".sent", "w")
            fg.write(flag+"\n")
            ff.close()
            fg.close()
time.sleep(3)
print "done"
