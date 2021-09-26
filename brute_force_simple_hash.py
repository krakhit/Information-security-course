#hash collisions: find and return y for h(input)=h(y)
def simple_hash(s):
    ln = len(s)
    r = 7
    ls = list(s)
    for i in  range(ln):
        r = (31*r + ord(ls[i])) % 2**(16)
    
    return r

def crack(s):
    if not s:
            return []
    
    import string
    import itertools
    hsh1 = simple_hash(s)
    tab = list(string.ascii_letters)+ list(string.digits)+list(string.punctuation) # + operator adds lists
    amt = list(itertools.product(tab,repeat=len(s))) # computes cartesian product of two lists upto a given length
    tmp=[]
    for i in range(len(amt)):
        tmp.append(''.join(amt[i]))

    tmp_n=list(dict.fromkeys(tmp)) #removes duplicate entries
    nhsh=[]
    for j in range(len(tmp_n)):
        nhsh.append(simple_hash(tmp_n[j]))

    for k in range(len(nhsh)):
        if(nhsh[k] == hsh1 and tmp_n[k] != s):
            return tmp_n[k]


    
    



