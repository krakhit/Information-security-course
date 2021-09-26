#fake rc4, the first part is a PRG (Pseudo Random number Generator). the second part generates the ciphertext using the key stream
def get_prg(plaintext_size, k):
    k_chr = str(k)
    k_len = len(k_chr)
    kchr_lis = list(k_chr)
    k_stream= ''
    i = j = 0
    for x in range(plaintext_size):
        i = (i + 1) % 32
        j = (j + ord(kchr_lis[i])) % 32
        kchr_lis[j], kchr_lis[i] = kchr_lis[i],kchr_lis[j]
        ind = (ord(kchr_lis[i]) + ord(kchr_lis[j])) % 32
        k_stream += kchr_lis[ind]

    return k_stream
               
def fake_rc4(plaintext, keystream):
    ciphtext=''
    for y in range(len(plaintext)):
        ciphtext += chr(ord(plaintext[y]) ^ ord(keystream[y]))


    return ciphtext
