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
    res = ''
    for y in encr_res:
        if y in alph:
            x = np.mod((alph.find(y) - key + 26), 26)
            res += alph[x]
        elif y in ALPH:
            x = np.mod((ALPH.find(y) - key + 26), 26)
            res += ALPH[x]
        elif (ord(y) < 65 or (ord(y)>90 and ord(y)<97) or ord(y)>122):
            res += y
    return(res)

def encr_Vigenere(inp_key,message):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v_square = np.empty((26, 26), dtype="str")
    V_SQUARE = np.empty((26, 26), dtype="str")

    for i in range(0, 26):
        for j in range(0, 26):
            v_square[i][j] = alph[np.mod((j + i), 26)]

    for i in range(0, 26):
        for j in range(0, 26):
            V_SQUARE[i][j] = ALPH[np.mod((j + i), 26)]

    v_key = ''

    for i in range(0, len(message)):
        v_key += inp_key[np.mod(i, len(inp_key))]

    res = ''
    for i in range(0, len(v_key)):
        if message[i] in alph:
            if v_key[i] in alph:
                res += v_square[alph.find(v_key[i])][alph.find(message[i])]
            elif v_key[i] in ALPH:
                res += v_square[ALPH.find(v_key[i])][alph.find(message[i])]
        elif message[i] in ALPH:
            if v_key[i] in alph:
                res += V_SQUARE[alph.find(v_key[i])][ALPH.find(message[i])]
            elif v_key[i] in ALPH:
                res += V_SQUARE[ALPH.find(v_key[i])][ALPH.find(message[i])]
    return res

def decr_Vigenere(inp_key,encr_res):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v_square = np.empty((26, 26), dtype="str")
    V_SQUARE = np.empty((26, 26), dtype="str")

    for i in range(0, 26):
        for j in range(0, 26):
            v_square[i][j] = alph[np.mod((j + i), 26)]

    for i in range(0, 26):
        for j in range(0, 26):
            V_SQUARE[i][j] = ALPH[np.mod((j + i), 26)]

    v_key = ''

    for i in range(0, len(encr_res)):
        v_key += inp_key[np.mod(i, len(inp_key))]

    res=''
    for i in range(0,len(encr_res)):
        if encr_res[i] in alph:
            if v_key[i] in alph:
                num_str=alph.find(v_key[i])
            elif v_key[i] in ALPH:
                num_str = ALPH.find(v_key[i])
            k = np.where(v_square[num_str, :] == encr_res[i])[0][0]
            res += alph[k]
        elif encr_res[i] in ALPH:
            if v_key[i] in alph:
                num_str=alph.find(v_key[i])
            elif v_key[i] in ALPH:
                num_str = ALPH.find(v_key[i])
            k = np.where(V_SQUARE[num_str, :] == encr_res[i])[0][0]
            res += ALPH[k]

    return res


if __name__ == '__main__':
    key=int(input("shift:"))
    message=input("message:")
    encr_res=encr_Caesar(key, message)
    print(encr_res)
    decr_res=decr_Caesar(key, encr_res)
    print(decr_res)

    inp_key=input("vigenere key:")
    enc_v=encr_Vigenere("lemon",message)
    print(enc_v)
    dec_v=decr_Vigenere(inp_key,enc_v)
    print(dec_v)
