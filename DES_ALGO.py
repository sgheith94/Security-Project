#!/usr/bin/env python
# coding: utf-8

# # All materials are from wikipedia
# https://en.wikipedia.org/wiki/DES_supplementary_material

# # 1. Supplementry Material

# In[1]:


import random


# In[18]:


import string


# In[3]:


IP = [58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7]


# In[4]:


IP_Inverse = [40,8,48,16,56,24,64,32,
            39,7,47,15,55,23,63,31,
            38,6,46,14,54,22,62,30,
            37,5,45,13,53,21,61,29,
            36,4,44,12,52,20,60,28,
            35,3,43,11,51,19,59,27,
            34,2,42,10,50,18,58,26,
            33,1,41,9,49,17,57,25]


# In[5]:


Expansion = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1 ]


# In[6]:


Permutation = [16,7,20,21,29,12,28,17,
                1,15,23,26,5,18,31,10,
                2,8,24,14,32,27,3,9,
                19,13,30,6,22,11,4,25]


# In[7]:


S_box = [
    [                      #s-box1
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]
    ],                     #s-box2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]
    ],                     #s-box3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]
    ],                     #s-box4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],                      #s-box5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]
    ],                       #s-box6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] 
    ],                       #s-box7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],                       #s-box8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]


# In[8]:


Shift_table = [ 1, 1, 2, 2,
                2, 2, 2, 2,
                1, 2, 2, 2,
                2, 2, 2, 1 ] #BIT ROTATION


# In[9]:


Key_compression = [ 14,17,11,24,1,5,3,28,
                    15,6,21,10,23,19,12,4,
                    26,8,16,7,27,20,13,2,
                    41,52,31,37,47,55,30,40,
                    51,45,33,48,44,49,39,56,
                    34,53,46,42,50,36,29,32 ]


# In[10]:


Conversions = { '0' : "0000",
                '1' : "0001",
                '2' : "0010",
                '3' : "0011",
                '4' : "0100",
                '5' : "0101",
                '6' : "0110",
                '7' : "0111",
                '8' : "1000",
                '9' : "1001",
                'A' : "1010",
                'B' : "1011",
                'C' : "1100",
                'D' : "1101",
                'E' : "1110",
                'F' : "1111",
                'a' : "1010",
                'b' : "1011",
                'c' : "1100",
                'd' : "1101",
                'e' : "1110",
                'f' : "1111",
                "0000" : '0',
                "0001" : '1',
                "0010" : '2',
                "0011" : '3',
                "0100" : '4',
                "0101" : '5',
                "0110" : '6',
                "0111" : '7',
                "1000" : '8',
                "1001" : '9',
                "1010" : 'A',
                "1011" : 'B',
                "1100" : 'C',
                "1101" : 'D',
                "1110" : 'E',
                "1111" : 'F',
                "1010" : 'a',
                "1011" : 'b',
                "1100" : 'c',
                "1101" : 'd',
                "1110" : 'e',
                "1111" : 'f',
              }


# ### CONVERSIONS

# In[11]:


def ConversionBinToHex(value):
    res = ""
    ct=0
    temp = ""
#     print(value)
    for i in range(len(value)):
        if ct<3:
            temp = temp + value[i]
            ct+=1
        else:
            temp = temp + value[i]
#             print(temp)
            res = res + Conversions[temp]
            ct=0
            temp = ""
    return res


# In[12]:


def ConversionHexToBin(value):
    res = ""
    for i in range(len(value)):
        res = res + Conversions[value[i]]
    return res


# In[13]:


def ConversionDecToBin(num):
    res = bin(num).replace("0b", "")
    if(len(res)%4 != 0):
        div = len(res) / 4
        div = int(div)
        counter =(4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


# In[14]:


def ConversionBinToDec(val):
       
    binary1 = val
    decimal, i, n = 0, 0, 0
    while(val != 0):
        dec = val % 10
        decimal = decimal + dec * pow(2, i)
        val = val //10
        i += 1
    return decimal


# ## IMPORTANT FUNCC

# In[58]:


def XOR(A,B):
    res = ""
#     print(len(A))
#     print(A)
#     print(len(B))
#     print(B)
    for i in range(0,len(A)):
        
        if A[i] != B[i]:
            res += "1"
        else:
            res += "0"
    return res


# In[16]:


def KeyShifting(key, no_shifts):
    s = ""
#     print(no_shifts)
    for i in range(no_shifts):
#         print(len(key))
#         print(key)
        for j in range(1,len(key)):
            s = s + key[j]
        s = s + key[0]
        key = s
        s = ""
#         print(key)
    return key


# In[17]:


def Arrange(key, arr, n):
    arrange = ""
    for i in range(0, n):
#         print(key[arr[i] - 1])
        arrange = arrange + key[arr[i] - 1]
    return arrange


# ## 2. ECB FUNCTIONS

# In[19]:


def Padding(plaintext):
####### 64 BIT PER BLOCK --> 8 BYTES #######
    padding_len = 8 - (len(plaintext) % 8) 
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding


# In[20]:


def Unpadding(plaintext):
    last_char = plaintext[-1]
### ord: returns the number representing the unicode code of a specified character ##
    if ord(last_char) < 8: 
        return plaintext.rstrip(last_char)
    else:
        return plaintext


# In[21]:


def ECB(plaintext,block_size):
    block=[]
    for i in range(0,len(plaintext),block_size):        
        block.append(plaintext[i:i+block_size])
    return block


# ## 3. Sub-Key 

# In[22]:


def KeyGeneration(Key_Len):
    temp=''
    for i in range(0,Key_Len):
        k=random.randint(0,1)
        temp+=str(k)
    return temp


# In[23]:


def KeyGen(Key):
#     Key = KeyGeneration(56)
    Left_Key = Key[0:28] 
    Right_Key = Key[28:56] 
    RoundKey_Binary = []
    RoundKey_Hexa = []
    for i in range(0, 16):
        Left_Key = KeyShifting(Left_Key, Shift_table[i])
        Right_Key = KeyShifting(Right_Key, Shift_table[i])

        Res = Left_Key + Right_Key

        round_key = Arrange(Res, Key_compression, 48)
        RoundKey_Binary.append(round_key)
        round_key
        res2 = ConversionBinToHex(round_key)
        RoundKey_Hexa.append(res2)
    return RoundKey_Binary,RoundKey_Hexa,Key
    


# ## 3. DES MAIN FUNCTION

# In[63]:


def Encryption(Plain_text,RoundKey_Hexa,RoundKey_Binary):
    Final = ""
    NEW = []
    Plain_text = Arrange(Plain_text, IP, 64)
#     print("len el plain" + str(len(Plain_text)))
#####        SPLITTT           #####
    Left_PT = Plain_text[0:32]
    Right_PT = Plain_text[32:64]
#     print(len(Right_PT))
#     print(len(Left_PT))
#     print( ConversionBinToHex(Left_PT))
#     print( ConversionBinToHex(Right_PT))
    Res_Sbox = " "
#######     16 roundsssss     #######
    for i in range(0,16):
######     Expansion        ######
        RExpansion = Arrange(Right_PT, Expansion, 48)
#         print("len el expan" + str(len(RExpansion)))
# #         print(RoundKey_Binary[i])
#         print("len el bin" + str(len(RoundKey_Binary[i])))
######     XOR KEY OF THE ROUND        ######
        Res_XOR = XOR(RExpansion ,RoundKey_Binary[i])
        
######     S-BOX CALCC        ######
        Sbox_Res = ""
        for s in range(0,8):
        ## Row  Position 0 & 6
        ## Column Position 1 --> 5
            Row = int(Res_XOR[s * 6] + Res_XOR[s * 6 + 5],2)
            Col = int(Res_XOR[s * 6 + 1] + Res_XOR[s * 6 + 2] + Res_XOR[s * 6 + 3] + Res_XOR[s * 6 + 4],2)
            val = S_box[s][Row][Col]

            Sbox_Res = Sbox_Res + ConversionDecToBin(val)
        
        Sbox_Res = Arrange(Sbox_Res, Permutation, 32)

            # XOR left and sbox_str
        Result = XOR(Left_PT , Sbox_Res)
        Left_PT = Result

#######       Swappperrrrr   #########
        if(i != 15):
            temp=Right_PT
            Right_PT=Left_PT
            Left_PT = temp
        NEW.append("Round "+ str(i + 1)+ " "+str( ConversionBinToHex(Left_PT))+ " "+str( ConversionBinToHex(Right_PT))+ " "+str(RoundKey_Hexa[i]))

    # Combination
    Final = Left_PT + Right_PT 
    Cipher_Text = Arrange(Final, IP_Inverse, 64)    
    return Cipher_Text,NEW


# ### ENCRYPTION PHASE

# In[134]:


def Encrypt(message,RoundKey_Binary,RoundKey_Hexa,Key,Flag_File):
    cipher_text=[]
#     print(message)
#     print(type(message))

    if Flag_File == 1 or Flag_File == 0:
        string= message.encode('utf-8')
        hex_str = string.hex()
    if Flag_File == 2:
        string = message
#         string= message.encode('utf-8')
#     print(message)

    new=Padding(string)
    blocks_enc=ECB(new,8)
    print(len(blocks_enc))
    text=[]
    for i in range (0,len(blocks_enc)):
        hex_str = blocks_enc[i].hex()
        Hex_PT = ConversionHexToBin(hex_str)
        cipher,steps = Encryption(Hex_PT,RoundKey_Hexa,RoundKey_Binary)
        cipher_text.append(cipher)
    EncryptionLog(string,Key,blocks_enc,steps,cipher_text)
#     print(cipher_text)
    return cipher_text,blocks_enc


# ### DECRYPTION PHASE

# In[148]:


def Decrypt(cipher_text,Inverse_Rk_Bin,Inverse_Rk_Hexa,Key,Flag_File):
    text = []
    for i in range(0,len(cipher_text)):
#         print("decrypt hexa"+ str(len(Inverse_Rk_Hexa)))
#         print("decrypt inverse" + str(len(Inverse_Rk_Bin)))
        pt,dec_steps = Encryption(cipher_text[i],Inverse_Rk_Hexa,Inverse_Rk_Bin)
        plain = ConversionBinToHex(pt)
        if Flag_File == 2:
            text.append(bytes.fromhex(plain).decode())
        else :
            text.append(bytes.fromhex(plain).decode())
    new_text=''.join(text)
    new2=Unpadding(new_text)
    cipher_text_res=''.join(cipher_text)
    cipher_text_res=ConversionBinToHex(cipher_text_res)
    DecryptionLog(cipher_text_res, Key, dec_steps, new2)
    return new2


# ## Log files for encryption

# In[136]:


def EncryptionLog(string,Key,x,steps,cipher_text):
    with open('Encryption.txt', 'w') as f:
        f.write('Encoded Plain text: ' + str(string))
        f.write('\n')
        f.write('Key: ' + str(Key))
        f.write('\n')
        f.write('ECB result: ' + str(x))
        f.write('\n')
        f.write('\n')
        f.write('Encryption Steps: ')
        f.write('\n')
        f.write('                    Left    Right    Round Key ')
        f.write('\n')
        for i in range(0,len(steps)):
            f.write('STEP '+ str(i) + "--> " + str(steps[i]))
            f.write('\n')
        f.write('\n')
        f.write('Encryption for each block: ')
        f.write('\n')
#         print(len(x))
#         print(len(cipher_text))
        for i in range(0,len(x)):
            f.write('Block '+ str(i) + ": "+ str(x[i])+ " --> " + str(cipher_text[i]))
            f.write('\n')


# ## Log files for decryption

# In[137]:


def DecryptionLog(cipher_text_res,Key,dec_steps,new2):
    with open('Decryption.txt', 'w') as f:
        f.write('Cipher text: ' + str(cipher_text_res))
        f.write('\n')
        f.write('Key: ' + str(Key))
        f.write('\n')
        f.write('\n')
        f.write('Decryption Steps: ')
        f.write('\n')
        f.write('                    Left    Right    Round Key ')
        f.write('\n')
        for i in range(0,len(dec_steps)):
            f.write('STEP '+ str(i) + "--> " + str(dec_steps[i]))
            f.write('\n')
        f.write('\n')
        f.write('Decrypted message: ' + str(new2))

