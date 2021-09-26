# brute forcing weak md_5 hashes, to find colliding texts
import hashlib

def weak_md5(s):
    return hashlib.md5(s).digest()[:5]

def find_collisions():
    import string
    import itertools
    tab = list(string.ascii_lowercase)
    amt = list(itertools.product(tab,repeat=5))
    dic={}
    for j in  range(len(amt)):
        tex = ''.join(amt[j])
        md5 = weak_md5(tex.encode('utf-8'))
        if md5 in dic:
            return tex, dic[md5]
        dic[md5]  = tex

        
        
        
