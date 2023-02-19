import numpy as np

def encr_Caesar(key, message):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    ALPH= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''

    for x in message:
        if x in alph:
            y = np.mod((alph.find(x) + key), 26)
            res += alph[y]
        elif x in ALPH:
            y = np.mod((ALPH.find(x) + key), 26)
            res += ALPH[y]
        elif (ord(x) < 65 or (ord(x)>90 and ord(x)<97) or ord(x)>122):
            res += x
    return(res)

def decr_Caesar(key, encr_res):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    ALPH= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dec_res = ''
    for y in encr_res:
        if y in alph:
            x = np.mod((alph.find(y) - key + 26), 26)
            dec_res += alph[x]
        elif y in ALPH:
            x = np.mod((ALPH.find(y) - key + 26), 26)
            dec_res += ALPH[x]
        elif (ord(y) < 65 or (ord(y)>90 and ord(y)<97) or ord(y)>122):
            dec_res += y
    return(dec_res)


if __name__ == '__main__':
    key=int(input("shift:"))
    message=input("message:")
    res=''
    print(message)
    encr_res=encr_Caesar(key, message)
    print(encr_res)
    decr_res=decr_Caesar(key, encr_res)
    print(decr_res)