#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


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


# In[4]:


def ConversionHexToBin(value):
    res = ""
    for i in range(len(value)):
        res = res + Conversions[value[i]]
    return res


# In[5]:


def ECB(plaintext,block_size):
    block=[]
    for i in range(0,len(plaintext),block_size):        
        block.append(plaintext[i:i+block_size])
    return block


# In[6]:


def Padding(plaintext):
####### 128 BIT PER BLOCK --> 16 BYTES #######
    padding_len = 16 - (len(plaintext) % 16) 
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding


# In[7]:


def Unpadding(plaintext):
    last_char = plaintext[-1]
### ord: returns the number representing the unicode code of a specified character ##
    if ord(last_char) < 16: 
        return plaintext.rstrip(last_char)
    else:
        return plaintext


# # Encrypt

# In[8]:


def EncryptAES(message):
    s_box = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16],]
    ###########################################
    RCON = [[0x01,0x00,0x00,0x00],
        [0x02,0x00,0x00,0x00],
        [0x04,0x00,0x00,0x00],
        [0x08,0x00,0x00,0x00],
        [0x10,0x00,0x00,0x00],
        [0x20,0x00,0x00,0x00],
        [0x40,0x00,0x00,0x00],
        [0x80,0x00,0x00,0x00],
        [0x1B,0x00,0x00,0x00],
        [0x36,0x00,0x00,0x00]
       ]
     ##########################################   
    def mixColumns(s):  
        # combine bytes of each col of state S [§5.1.3]
        for c in range(4):
            a = []  # 'a' is a copy of the current column from 's'
            b = []  # 'b' is a·{02} in GF(2^8)
            for i in range(4):
                a.append(int(s[i][c],0))
                if(int(s[i][c],0) & 0x80):
                    b.append(int(s[i][c],0) << 1 ^ 0x011b)
                else:
                    b.append(int(s[i][c],0) << 1)
            
            # a[n] ^ b[n] is a·{03} in GF(2^8)
            s[0][c] = hex(b[0] ^ a[1] ^ b[1] ^ a[2] ^ a[3]) # 2*a0 + 3*a1 + a2 + a3
            s[1][c] = hex(a[0] ^ b[1] ^ a[2] ^ b[2] ^ a[3]) # a0 * 2*a1 + 3*a2 + a3
            s[2][c] = hex(a[0] ^ a[1] ^ b[2] ^ a[3] ^ b[3]) # a0 + a1 + 2*a2 + 3*a3
            s[3][c] = hex(a[0] ^ b[0] ^ a[1] ^ a[2] ^ b[3]) # 3*a0 + a1 + a2 + 2*a3
        return s
    ##############################################
    import random
    def KeyGeneration(Key_Len):
        temp=''
        for i in range(0,Key_Len):
            k=random.randint(0,1)
            temp+=str(k)
        return temp
    ##################################################
    #OutPutCiphers=[]
    TotalOutputs=[]
    TotalofKeys=[]
    BlocksOfKeyRandom=[]
    for k in range(len(message)):
        
        plaintext= message[k].hex()
        n=2
        plain=[plaintext[i:i+n] for i in range(0, len(plaintext), n)]
        PlainText=[]
        for i in range(4):
            ct=i
            row=[]
            for j in range(4):
                row.append(plain[ct])
                ct+=4
            PlainText.append(row)
        keybin=KeyGeneration(128)
        key=ConversionBinToHex(keybin)
        BlocksOfKeyRandom.append(key)
        n=2
        key2=[key[i:i+n] for i in range(0, len(key), n)]
        keystate=[]
        for i in range(4):
            ct=i
            row=[]
            for j in range(4):
                row.append(key2[ct])
                ct+=4
            keystate.append(row)
        RotWord=[]
        RotWord.append(hex(int(keystate[1][3],16)))
        RotWord.append(hex(int(keystate[2][3],16)))
        RotWord.append(hex(int(keystate[3][3],16)))
        RotWord.append(hex(int(keystate[0][3],16)))

        Subbyte=[]
        Sub_Byte=[]
        for i in range (4):

            saving=str(RotWord[i]).split('0x')[1]
            if len(saving)==1:
                var=saving[0]
                saving=[]
                saving.append('0')
                saving.append(var)
            if saving[0] in ['1','2','3','4','5','6','7','8','9'] and saving[1] in ['1','2','3','4','5','6','7','8','9']:
                saveSbox=s_box[int(saving[0])][int(saving[1])]
                Sub_Byte.append(hex(saveSbox))
            if saving[0] in ['1','2','3','4','5','6','7','8','9'] and saving[1] not in ['1','2','3','4','5','6','7','8','9']:
                sav1=int(saving[1],16)
                saveSbox=s_box[int(saving[0])][sav1]
                Sub_Byte.append(hex(saveSbox))
            if saving[0] not in ['1','2','3','4','5','6','7','8','9'] and saving[1] in ['1','2','3','4','5','6','7','8','9']:
                sav=int(saving[0],16)
                saveSbox=s_box[int(sav)][int(saving[1])]
                Sub_Byte.append(hex(saveSbox))
            if saving[0] not in ['1','2','3','4','5','6','7','8','9'] and saving[1] not in ['1','2','3','4','5','6','7','8','9']:
                sav=int(saving[0],16)
                sav1=int(saving[1],16)
                saveSbox=s_box[int(sav)][int(sav1)]
                Sub_Byte.append(hex(saveSbox))

        keyss=[]
        for i in range(4):
            key=[]
            for j in range(4):
                if i==0:
                    key.append(hex(int(Sub_Byte[j],0)^int(keystate[j][0],16)^int (str(RCON[0][j]),0)))
                else:
                    key.append(hex(int(keystate[j][i],16)^int(keyss[i-1][j],16)))
            keyss.append(key)
        key1=[]
        for i in range(4):
            row=[]
            for j in range(4):
                row.append(str(keyss[j][i]).split('0x')[1])
            key1.append(row)
        TenKeys=[]
        TenKeys.append(keystate)
        TenKeys.append(key1)
        for k in range(1,10):
            RotWord=[]
            RotWord.append(hex(int(TenKeys[k][1][3],16)))
            RotWord.append(hex(int(TenKeys[k][2][3],16)))
            RotWord.append(hex(int(TenKeys[k][3][3],16)))
            RotWord.append(hex(int(TenKeys[k][0][3],16)))
            #print(RotWord,"ROTTTTT")
            Subbyte=[]
            Sub_Byte=[]
            for i in range (4):

                saving=str(RotWord[i]).split('0x')[1]
                if len(saving)==1:
                    var=saving[0]
                    saving=[]
                    saving.append('0')
                    saving.append(var)
                #print(saving)
                if saving[0] in ['1','2','3','4','5','6','7','8','9'] and saving[1] in ['1','2','3','4','5','6','7','8','9']:
                    saveSbox=s_box[int(saving[0])][int(saving[1])]
                    Sub_Byte.append(hex(saveSbox))
                if saving[0] in ['1','2','3','4','5','6','7','8','9'] and saving[1] not in ['1','2','3','4','5','6','7','8','9']:
                    sav1=int(saving[1],16)
                    saveSbox=s_box[int(saving[0])][sav1]
                    Sub_Byte.append(hex(saveSbox))
                if saving[0] not in ['1','2','3','4','5','6','7','8','9'] and saving[1] in ['1','2','3','4','5','6','7','8','9']:
                    sav=int(saving[0],16)
                    saveSbox=s_box[int(sav)][int(saving[1])]
                    Sub_Byte.append(hex(saveSbox))
                if saving[0] not in ['1','2','3','4','5','6','7','8','9'] and saving[1] not in ['1','2','3','4','5','6','7','8','9']:
                    #print(saving[0])
                    #print(type(saving[0]))
                    sav=int(saving[0],16)
                    sav1=int(saving[1],16)
                    saveSbox=s_box[int(sav)][int(sav1)]
                    Sub_Byte.append(hex(saveSbox))
            #print(Sub_Byte)
            keyss=[]
            for i in range(4):
                key=[]
                for j in range(4):
                    if i==0:
                        key.append(hex(int(Sub_Byte[j],0)^int(TenKeys[k][j][i],16)^int (str(RCON[k][j]),0)))
                    else:
                        key.append(hex(int(TenKeys[k][j][i],16)^int(keyss[i-1][j],16)))

                keyss.append(key)
            key1=[]
            for i in range(4):
                row=[]
                for j in range(4):
                    row.append(str(keyss[j][i]).split('0x')[1])
                key1.append(row)
            TenKeys.append(key1)
        rounddd=[]
        for f in range(11):

            if f==0:
                rounds=[]
                for i in range(4):
                    row=[]
                    for j in range(4):

                        row.append(hex(int(PlainText[i][j],16)^int(TenKeys[0][i][j],16)))
                    rounds.append(row)

            else:


                Subbyte=[]

                for i in range (4):
                    Sub_Byte=[]
                    for j in range(4):

                        saving=str(rounds[i][j]).split('0x')[1]
                        if len(saving)==1:
                            var=saving[0]
                            saving=[]
                            saving.append('0')
                            saving.append(var)
                        #print(saving)
                        if saving[0] in ['1','2','3','4','5','6','7','8','9'] and saving[1] in ['1','2','3','4','5','6','7','8','9']:
                            saveSbox=s_box[int(saving[0])][int(saving[1])]
                            Sub_Byte.append(hex(saveSbox))
                        if saving[0] in ['1','2','3','4','5','6','7','8','9'] and saving[1] not in ['1','2','3','4','5','6','7','8','9']:
                            sav1=int(saving[1],16)
                            saveSbox=s_box[int(saving[0])][sav1]
                            Sub_Byte.append(hex(saveSbox))
                        if saving[0] not in ['1','2','3','4','5','6','7','8','9'] and saving[1] in ['1','2','3','4','5','6','7','8','9']:
                            sav=int(saving[0],16)
                            saveSbox=s_box[int(sav)][int(saving[1])]
                            Sub_Byte.append(hex(saveSbox))
                        if saving[0] not in ['1','2','3','4','5','6','7','8','9'] and saving[1] not in ['1','2','3','4','5','6','7','8','9']:
                            #print(saving[0])
                            #print(type(saving[0]))
                            sav=int(saving[0],16)
                            sav1=int(saving[1],16)
                            saveSbox=s_box[int(sav)][int(sav1)]
                            Sub_Byte.append(hex(saveSbox))
                    Subbyte.append(Sub_Byte)
                for i in range (4):
                    if i==1:
                        for j in range(0,3):
                            var=Subbyte[i][j]
                            var2=Subbyte[i][j+1]
                            Subbyte[i][j+1]=var
                            Subbyte[i][j]=var2
                    if i==2:
                        var=Subbyte[i][0]
                        var2=Subbyte[i][2]
                        Subbyte[i][0]=var2
                        Subbyte[i][2]=var
                        var=var=Subbyte[i][1]
                        var2=Subbyte[i][3]
                        Subbyte[i][1]=var2
                        Subbyte[i][3]=var
                    if i==3:
                        var=Subbyte[i][0]
                        var2=Subbyte[i][1]
                        var3=Subbyte[i][2]
                        var4=Subbyte[i][3]
                        Subbyte[i][0]=var4
                        Subbyte[i][1]=var
                        Subbyte[i][2]=var2
                        Subbyte[i][3]=var3
                if f<10:        
                    ss=mixColumns(Subbyte)

                    rounddd.append(ss)
                    rounds=[]
                    for i in range(4):
                        row=[]
                        for j in range(4):
                            row.append(hex(int(ss[i][j],16)^int(TenKeys[f][i][j],16)))
                        rounds.append(row)
                    #print(rounds)
                else:
                    output=[]
                    rounddd.append(Subbyte)
                    for i in range(4):
                        row=[]
                        for j in range(4):
                            row.append(hex(int(Subbyte[i][j],16)^int(TenKeys[f][i][j],16)))
                        output.append(row)
        TotalOutputs.append(output)
        TotalofKeys.append(TenKeys)
    return TotalOutputs,TotalofKeys,BlocksOfKeyRandom


# # Decrypt

# In[9]:


def DecryptAES(output,TenKeys):
    
    def galoisMult(a, b):
        
        p = 0
        hiBitSet = 0
        for i in range(8):
            if b & 1 == 1:
                p ^= a
            hiBitSet = a & 0x80
            a <<= 1
            if hiBitSet == 0x80:
                a ^= 0x1b
            b >>= 1
        
        return p % 256
    ####################################################
    def mixColumnInv(column):
        temp = copy(column)
        column[0] = galoisMult(temp[0],14) ^ galoisMult(temp[3],9) ^                     galoisMult(temp[2],13) ^ galoisMult(temp[1],11)
        column[1] = galoisMult(temp[1],14) ^ galoisMult(temp[0],9) ^                     galoisMult(temp[3],13) ^ galoisMult(temp[2],11)
        column[2] = galoisMult(temp[2],14) ^ galoisMult(temp[1],9) ^                     galoisMult(temp[0],13) ^ galoisMult(temp[3],11)
        column[3] = galoisMult(temp[3],14) ^ galoisMult(temp[2],9) ^           galoisMult(temp[1],13) ^ galoisMult(temp[0],11)
        return column
######################################################################
    inv_s_box = [
    [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
    [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
    [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
    [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
    [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
    [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
    [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
    [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
    [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
    [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
    [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
    [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
    [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
    [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
    [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D],
    ]

######################################################################
    BlocksOfMessage=[]
    BlockofDecTenKeys=[]
    from copy import copy
    for k in range(len(output)):
        TenKeysofDecryp=[]
        for i in range(10,-1,-1):
            TenKeysofDecryp.append(TenKeys[k][i])
        BlockofDecTenKeys.append(TenKeysofDecryp)    
        saver=[]
        for f in range(11):

            if f==0:
                rounds=[]
                for i in range(4):

                    row=[]
                    for j in range(4):
                        
                        row.append(hex(int(output[k][i][j],0)^int(TenKeysofDecryp[0][i][j],16)))
                        
                    rounds.append(row)
                
            else:
                if f != 1:
                    aftermixcolumninv=[]
                    fixedInverseSub=[]
                    for i in range(4):
                        row=[]
                        for j in range(4):
                            
                            row.append(int(saver[i][j],16))
                        fixedInverseSub.append(row)
                    RotatedMixCol=[]
                    for i in range(4):
                        row=[]
                        for j in range(4):
                            row.append(fixedInverseSub[j][i])
                        RotatedMixCol.append(row)
                    for i in range(4):
                        aftermixcolumninv.append(mixColumnInv(RotatedMixCol[i]))
                    fixedaftermixcolumninv=[]
                    for i in range(4):
                        row=[]
                        for j in range(4):
                            row.append(aftermixcolumninv[j][i])
                        fixedaftermixcolumninv.append(row)
                    fixedInverseMixCol=[]
                    for i in range(4):
                        row=[]
                        for j in range(4):
                            row.append(hex(fixedaftermixcolumninv[i][j]))
                        rounds.append(row)
       
                for i in range (4):
                    if i==1:
                        for j in range(3,0,-1):
                            var=rounds[i][j]
                            var2=rounds[i][j-1]
                            rounds[i][j-1]=var
                            rounds[i][j]=var2
                    if i==2:
                        var=rounds[i][0]
                        var2=rounds[i][1]
                        var3=rounds[i][2]
                        var4=rounds[i][3]
                        rounds[i][0]=var3
                        rounds[i][1]=var4
                        rounds[i][2]=var
                        rounds[i][3]=var2
                    if i==3:
                        var=rounds[i][0]
                        var2=rounds[i][1]
                        var3=rounds[i][2]
                        var4=rounds[i][3]
                        rounds[i][0]=var2
                        rounds[i][1]=var3
                        rounds[i][2]=var4
                        rounds[i][3]=var
                InverseSub=[]
                for i in range (4):
                    INVSub_Byte=[]
                    for j in range(4):
                        saving=str(rounds[i][j]).split('0x')[1]
                        if len(saving)==1:
                            var=saving[0]
                            saving=[]
                            saving.append('0')
                            saving.append(var)
                        #print(saving)
                        if saving[0] in ['1','2','3','4','5','6','7','8','9'] and saving[1] in ['1','2','3','4','5','6','7','8','9']:
                            saveSbox=inv_s_box[int(saving[0])][int(saving[1])]
                            INVSub_Byte.append(hex(saveSbox))
                        if saving[0] in ['1','2','3','4','5','6','7','8','9'] and saving[1] not in ['1','2','3','4','5','6','7','8','9']:
                            sav1=int(saving[1],16)
                            saveSbox=inv_s_box[int(saving[0])][sav1]
                            INVSub_Byte.append(hex(saveSbox))
                        if saving[0] not in ['1','2','3','4','5','6','7','8','9'] and saving[1] in ['1','2','3','4','5','6','7','8','9']:
                            sav=int(saving[0],16)
                            saveSbox=inv_s_box[int(sav)][int(saving[1])]
                            INVSub_Byte.append(hex(saveSbox))
                        if saving[0] not in ['1','2','3','4','5','6','7','8','9'] and saving[1] not in ['1','2','3','4','5','6','7','8','9']:
                            #print(saving[0])
                            #print(type(saving[0]))
                            sav=int(saving[0],16)
                            sav1=int(saving[1],16)
                            saveSbox=inv_s_box[int(sav)][int(sav1)]
                            INVSub_Byte.append(hex(saveSbox))
                    InverseSub.append(INVSub_Byte)
                
                saver=[]
                rounds=[]
                for i in range(4):
                    row=[]
                    for j in range(4):
                        row.append(hex(int(InverseSub[i][j],0)^int(TenKeysofDecryp[f][i][j],16)))
                    saver.append(row)
                
        BlocksOfMessage.append(saver)
        
    return BlocksOfMessage,BlockofDecTenKeys              


# # EncryptionLog

# In[10]:


def EncryptionLog(string,Key,x,steps,cipher_text):
    with open('EncryptionAES.txt', 'w') as f:
        f.write('Encoded Plain text: ' + string)
        f.write('\n')
        f.write('Key: ' + str(Key))
        f.write('\n')
        f.write('ECB result: ' + str(x))
        f.write('\n')
        f.write('\n')
        f.write('Encryption Steps: Ten Keys of Each Block ')
        f.write('\n')
        f.write('\n')
        var=0
        var2=10
        #print(len(x))
        for i in range(int(len(x)/10)):
            f.write('10 Keys of Block'+str(x))
            f.write('\n')
            for j in range(var,var2):
                #print(j)
                f.write('Key '+ str(j) + "--> " + str(steps[j]))
                f.write('\n')
            var=var2
            var2=var+10
        f.write('\n')
        f.write('Encryption for each block: ')
        f.write('\n')

        for i in range(0,len(x)):
            f.write('Block '+ str(i) + ": "+ str(x[i])+ " --> " + str(cipher_text[i]))
            f.write('\n')


# # DecryptionLog

# In[11]:


def DecryptionLog(cipher_text_res,Key,x,dec_steps,new2):
    with open('DecryptionAES.txt', 'w') as f:
        f.write('Cipher text: ' + str(cipher_text_res))
        f.write('\n')
        f.write('Key: ' + str(Key))
        f.write('\n')
        f.write('\n')
        f.write('Decryption Steps: Ten Keys of Each Block ')
        f.write('\n')
        f.write('\n')
        var=0
        var2=10
        for i in range(int(len(x)/10)):
            f.write('10 Keys of Block'+str(x))
            f.write('\n')
            for j in range(var,var2):
                #print(j)
                f.write('Key '+ str(j) + "--> " + str(dec_steps[j]))
                f.write('\n')
            var=var2
            var2=var+10
        
        f.write('\n')
        f.write('\n')
        f.write('Decrypted message: ' + str(new2))


# # Main

# In[24]:


def FinalEncAES(message):
    string= message.encode('utf-8')
    print(string)
    plaintext = string.hex()

    new=Padding(string)
    blocks_enc=ECB(new,16)

    CipherEncy,Tenkeys,KeysRandomCreated=EncryptAES(blocks_enc)
    EncryptionLog(message,KeysRandomCreated,blocks_enc,Tenkeys,CipherEncy)
    return CipherEncy,Tenkeys,KeysRandomCreated


# In[31]:


def FinalDecAES( CipherEncy,Tenkeys,KeysRandomCreated):
    THE_PLAIN_TEXT,TenKeysofDec=DecryptAES(CipherEncy,Tenkeys)

    newnextplain=[]
    for k in range(len(THE_PLAIN_TEXT)):
        newplain=[]
        for i in range(4):
            row=[]
            for j in range(4):
                row.append(str(hex(int(THE_PLAIN_TEXT[k][i][j],0))).split('0x')[1])
            newplain.append(row)
        newnextplain.append(newplain)

    text=[]
    ct=0
    for k in range(len(THE_PLAIN_TEXT)):
        for i in range(4):
            for j in range(4):
                if len(newnextplain[k][j][i])==2:
                    text.append(bytes.fromhex(newnextplain[k][j][i]).decode('latin1'))



    new_text=''.join(text)
    new2=Unpadding(new_text)
    return new2
    DecryptionLog(THE_PLAIN_TEXT, KeysRandomCreated,CipherEncy, TenKeysofDec, new2)


# In[12]:


# message="ning the northeast corner of Africa and southwest corner of Asia via a land bridge formed by the Sinai Peninsula. It is bordered by the Mediterranean Sea to the north, the Gaza Strip (Palestine) and Israel to the northeast, the Red Sea to the east, Sudan to the south, and Libya to the west. The Gulf of Aqaba in the northeast separates Egypt from Jordan and Saudi Arabia. Cairo is the capital and largest city of Egypt, while Alexandria, the second-largest city, is an important industrial and tourist hub at the Mediterranean coast.[14] At approximately 100 million inhabitants, Egypt is the 14th-most populated country in the world."
# string= message.encode('utf-8')
# plaintext = string.hex()

# new=Padding(string)
# blocks_enc=ECB(new,16)

# CipherEncy,Tenkeys,KeysRandomCreated=EncryptAES(blocks_enc)


# THE_PLAIN_TEXT,TenKeysofDec=DecryptAES(CipherEncy,Tenkeys)

# newnextplain=[]
# for k in range(len(THE_PLAIN_TEXT)):
#     newplain=[]
#     for i in range(4):
#         row=[]
#         for j in range(4):
#             row.append(str(hex(int(THE_PLAIN_TEXT[k][i][j],0))).split('0x')[1])
#         newplain.append(row)
#     newnextplain.append(newplain)

# text=[]
# ct=0
# for k in range(len(THE_PLAIN_TEXT)):
#     for i in range(4):
#         for j in range(4):
#             if len(newnextplain[k][j][i])==2:
#                 text.append(bytes.fromhex(newnextplain[k][j][i]).decode('latin1'))
            
            

# new_text=''.join(text)
# new2=Unpadding(new_text)
# #print(new2)
# #print(len(blocks_enc))
# EncryptionLog(message,KeysRandomCreated,blocks_enc,Tenkeys,CipherEncy)

# #DecryptionLog(THE_PLAIN_TEXT, KeysRandomCreated, TenKeysofDec, new2)


# In[55]:


# DecryptionLog(THE_PLAIN_TEXT, KeysRandomCreated,blocks_enc, TenKeysofDec, new2)


# In[13]:


# newnextplain


# In[32]:


# message2="hi i am salma"
# print(message2)
# CipherEncy,Tenkeys,KeysRandomCreated=FinalEncAES(message2)
# FinalDecAES( CipherEncy,Tenkeys,KeysRandomCreated)


# In[ ]:




