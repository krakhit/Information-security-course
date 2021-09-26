#this is an example of a time attack Hackxercise part of information security course. 
#  Q1: The function check_password(password) is used by a safe with 4-digits passwords, and is susceptible to timing attacks.
#More specifically, it takes it around 0.1 seconds to check one digit – so brute-forcing all the possible combinations will take more than an hour.
#Can you implement a way to crack its password in less than a minute?
import time
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    pwd=[0,0,0,0]
    for i in range(4):
        for j in range(10):
            ptex=''.join(str(x) for x in pwd)
            t0 = time.time()
            check_password(ptex)
            t1 = time.time()
            if (i==3):
                if (check_password(ptex)):
                    pwd[i] = str(j)
                    break
            elif (t1-t0 == 0.2 + i/10):
                pwd[i] = str(j)
                break
        
        
    return ptex
