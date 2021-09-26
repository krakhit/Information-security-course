#caesar
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    lbare = list(alphabet)
    enc = lbare[-int(k):] + lbare[:-int(k)]
    #caesar = join(enc)
    lenctext=[]
    ls = len(plaintext)
    ltext = list(plaintext)
    for i in range(ls):
        for j in range(26):
            if(ltext[i] == lbare[j]):
                lenctext.append(enc[j])


    enctext = ''.join(lenctext)            
    return enctext
    print(enctext)

    

