# one of the first codes i wrote for xor encryption
def encrypt(plaintext, k):
    bintext =  list(' '.join(format(ord(str(x)),'08b') for x in plaintext))
    binkey =   list(' '.join(format(ord(str(x)),'08b') for x in k))
    xorciph= []
    ciph = []
    cipht=[]
    temp=[]
    for (item,obj) in zip(bintext,binkey):
        if(item == '1' and obj =='0'):
            xorciph.append('1')
        elif(item == '0' and obj == '1'):
            xorciph.append('1')
        elif(item == '0' and obj == '0'):
            xorciph.append('0')
        elif(item == '1' and obj == '1'):
            xorciph.append('0')
        else:
            xorciph.append(' ')
        

    xorciph.append(' ')
    for i in range(len(xorciph)):
        if(xorciph[i] == ' '):
            ciph.append(''.join(cipht))
            cipht=[]
        else:
            cipht.append(str(xorciph[i]))
        

    ciphbin=' '.join(ciph)
    for i in range(len(ciph)):
        temp.append(chr(int(ciph[i],2)))
    
    print(plaintext,''.join(bintext))
    print(k, ''.join(binkey))
    print(''.join(temp),ciphbin)

