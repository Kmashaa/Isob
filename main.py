import numpy as np

def gen_alphs():
    alph = 'abcdefghijklmnopqrstuvwxyz'
    ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alph, ALPH

def gen_v_squares():
    alph, ALPH = gen_alphs()
    v_square = np.empty((26, 26), dtype="str")
    V_SQUARE = np.empty((26, 26), dtype="str")

    for i in range(0, 26):
        for j in range(0, 26):
            v_square[i][j] = alph[np.mod((j + i), 26)]

    for i in range(0, 26):
        for j in range(0, 26):
            V_SQUARE[i][j] = ALPH[np.mod((j + i), 26)]

    return v_square, V_SQUARE

def encr_Caesar(key, message):
    alph,ALPH = gen_alphs()
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
    alph,ALPH = gen_alphs()
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
    alph,ALPH = gen_alphs()
    v_square, V_SQUARE=gen_v_squares()

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
        elif (ord(message[i]) < 65 or (ord(message[i])>90 and ord(message[i])<97) or ord(message[i])>122):
            res += message[i]
    return res

def decr_Vigenere(inp_key,encr_res):
    alph,ALPH = gen_alphs()
    v_square, V_SQUARE=gen_v_squares()

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
        elif (ord(encr_res[i]) < 65 or (ord(encr_res[i])>90 and ord(encr_res[i])<97) or ord(encr_res[i])>122):
            res += encr_res[i]
    return res
def read_data(file_name):
    f = open(file_name, 'r')
    i = 0
    key = ''
    message = ''
    for line in f:
        if i == 0:
            key = line
        elif i == 1:
            message = line
        i+=1
    return key, message


if __name__ == '__main__':

    c_key, c_message=read_data('caesar.txt')
    c_key=int(c_key)
    v_key, v_message=read_data('vigenere.txt')
    v_key=v_key[:len(v_key)-1]

    print("original text:",c_message)
    print("Caesar key:",c_key)
    encr_c=encr_Caesar(c_key, c_message)
    decr_c=decr_Caesar(c_key, encr_c)
    print("encrypted with Caesar cipher:",encr_c)
    print("decrypted with Caesar cipher:",decr_c,"\n")

    print("original text:",v_message)
    print("Vigenere key:",v_key)
    encr_v=encr_Vigenere(v_key,v_message)
    decr_v=decr_Vigenere(v_key,encr_v)
    print("encrypted with Vigenere cipher:",encr_v)
    print("decrypted with Vigenere cipher:",decr_v)
