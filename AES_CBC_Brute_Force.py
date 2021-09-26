#Brute force a message encrypted with AES-CBC, given that it was encrypted with a key
#that represents a phone number of someone, padded with zeroes
#(in other words, 9 digits, beginning with 036, and with trailing '0' to a length of 16 bytes,
#like this: 036######0000000).
#You should test your brute-force cracker code using the outputs from your
#AES encrypt function.

from Crypto.Cipher import AES
from Crypto import Random
import itertools
from collections import Counter

#The function encrypts a given Plain text and Key using AES in CBC mode, returns iv and ciphertext)
def aes_encrypt(plaintext, k):
    iv = Random.get_random_bytes(16)
    cipher = AES.new(k.encode("utf8"),AES.MODE_CBC,iv)
    ciphtext = cipher.encrypt(plaintext.encode("utf8"))
    return iv + ciphtext

#The function decrypts a given Plain text and Key using AES in CBC mode, returns iv and ciphertext)
def aes_decrypt(ciphertext, k):
    iv = ciphertext[:16]
    ciphtext = ciphertext[16:]
    cipher = AES.new(k.encode("utf8"),AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphtext)
    latext = plaintext.decode()
    return latext
#checking if it is ascii
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
#check if it is english alphabet
def is_english(s):
    if (is_ascii(s)):
        text = ''.join(c for c in s if c.isalpha())
        if (text == ''):
            return False
        else:
            lext = text.lower()
            chk = 'etaoin' #frequency analysis commonly used letters
            cnt = Counter(lext).most_common(3)
            cntn = [cnt[0][0],cnt[1][0],cnt[2][0]]
            cntjn = ''.join(cntn)
          #  print(cnt)
            for x in cntjn:
                if x not in chk:
                    return False
                else:
                    return True

def brute_force_aes(ciphertext):
    for i in range(999999):
        key = '036'+str(i).zfill(6)+'0000000'
        try:
            trial = aes_decrypt(ciphertext,key)
            if (is_english(trial)):
                return(trial,key)

        except UnicodeDecodeError:
            continue



