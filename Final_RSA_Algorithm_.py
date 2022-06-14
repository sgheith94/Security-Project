#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from math import sqrt
from random import randint


# # Functions

# # 1- Key Generation

# In[2]:


def KeyGenRSA():
    def IsPrime(Number):
        prime_flag = 0
        for i in range(2, int(sqrt(Number)) + 1):
            if (Number % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return 1
        else:
            return 0
        
    def GCD(a,h):   
        while True:
            temp = a%h
            if temp == 0:            
                return h
            a = h
            h = temp
    #################################################
    Var = []
    while True:
        P = randint(1, 100000)
        Q = randint(1, 100000)   

        if IsPrime(P) == 1 and IsPrime(Q) == 1 and P!=Q:
            break
        
    n = P*Q    
#     print("P-> " + str(P) + " , Q-> " + str(Q) + " , n-> " + str(n)) 
    Var.append(P)
    Var.append(Q)
    
    #################################################
    
    ET = (P-1) * (Q-1)
    while True:
        e = randint(1, ET)
        if GCD(e,ET) == 1:
            break
    
#     print("e-> " + str(e) , ", ø(n)-> " + str(ET))
    Var.append(ET)
    
    #################################################
    
    d = pow(e, -1, ET)
    print("d-> " + str(d))
    
    #################################################
    
    PR = (d,n)
    PU = (e,n)
#     print("Public Key-> " + str(PU))
#     print("Private Key-> " + str(PR))
    return PU , PR , Var


# # 2- Encryption

# In[3]:


def EncryptRSA(Msg , e , n):
    def Block(Text , n):
        NewAlpha = Text
        M = NewAlpha[0]
        ct = 1
        for i in range(1 ,len(NewAlpha)):
            M += NewAlpha[i]
            if len(M) > len(str(n)):
                return ct
            else:
                ct+=1
        return ct
    
    def Padding(Msg):
        NewAlpha=[]
        for i in range(len(Msg)):
            ASCII = str(ord(Msg[i]))
            if len(ASCII) == 2:
                    ASCII = '0' + ASCII 
            NewAlpha.append(ASCII)
        return NewAlpha
    
    #################################################
    
    Msg = Padding(Msg)
    
    #################################################
    
    CypherText = []
    Text=''
    BlockNum = Block(Msg,n)
    ct = 0
    flag = 1
    print("Number Of Blocks = " + str(BlockNum))
    for i in range(len(Msg)):
        ASCII = Msg[i]
        Text+= str(ASCII)
        if ct == (BlockNum - 1):
            CypherText.append(pow(int(Text) , e , n))
            Text=''
            ct=-1
        ct+=1
        
    if ct!=0:
        CypherText.append(pow(int(Text) , e , n))
        
#     print("The Encrypted Message is: " + str(CypherText))
    
    return CypherText , BlockNum


# # 3- Decryption

# In[4]:


def DecryptRSA(CypherText , d , n):
    DecryptedText=[]
    for i in CypherText:
        temp = pow(i , d , n)
        DecryptedText.append(temp)

#     print("The Decrypted Message is: " + str(DecryptedText))
    
    #################################################
    
    PlainText =''
    for i in range (len(DecryptedText)):
        if len(str(DecryptedText[i])) % 3 == 0:
            Number = str(DecryptedText[i])
            text=''
            for j in range(len(Number)):
                text+=Number[j]
                if (j+1) % 3 == 0:
                    if text[0] == '0':
                        PlainText += chr(int(text[1:]))
                    else:
                        PlainText += chr(int(text))
                    text=''
        else:
            t = str(DecryptedText[i])
            text = t[0] + t[1]
            PlainText += chr(int(text))
            text=''
            ct = 0
            for j in range(2 , len(t)):
                text+=t[j]
                if (ct+1) % 3 == 0:
                    if text[0] == '0':
                        PlainText += chr(int(text[1:]))
                    else:
                        PlainText += chr(int(text))
                    text=''
                    ct=-1
                ct+=1
#     print("\n")
#     print("--------------------------------------------")
#     print("\n")
#     print("The Original Message: " + str(PlainText))
    return PlainText


# # 4- Creating Log Files

# In[5]:


def RSALogFiles(PU , PR , CypherText , DecryptedText , BlockNum , Var):
    with open('Log.txt', 'w',encoding='utf8') as f:
        f.write('Random Variables: P -> ' + str(Var[0]) + ' , Q -> ' + str(Var[1]) + ' , ø(n) -> ' + str(Var[2]))
        f.write('\n')
        f.write('------------------------')
        f.write('\n')
        
        f.write('e -> ' + str(PU[0]) + ('\nn -> ' + str(PU[1])))
        f.write('\n')
        f.write('Public Key: ' + str(PU))
        
        f.write('\n')
        f.write('------------------------')
        f.write('\n')
        
        f.write('d -> ' + str(PR[0]) + ('\nn -> ' + str(PR[1])))
        
        f.write('\n')
        f.write('Private Key: ' + str(PR))
        
        f.write('\n')
        f.write('------------------------')
        f.write('\n')
        
        f.write('Number Of Blocks Needed = ' + str(BlockNum))
        
        f.write('\n')
        f.write('------------------------')
        f.write('\n')

        f.write('Encrypted Message: ') 
        for i in CypherText:
            f.write(str(i))
        f.write('\n')
        
        f.write('------------------------')
        f.write('\n')
        f.write('Original Message: ') 
        for i in DecryptedText:
            f.write(str(i))
        f.write('\n')
#     print("Done")


# # Main

# In[6]:


# PublicKey , PrivateKey , Var = KeyGenRSA()


# # In[7]:


# Msg = input("Enter Your Message: ")


# # In[8]:


# EncryptedText , BlockNum = EncryptRSA(Msg , PublicKey[0] , PublicKey[1])


# # In[9]:


# DecryptedText = DecryptRSA(EncryptedText , PrivateKey[0] , PrivateKey[1])


# # In[10]:


# RSALogFiles(PublicKey , PrivateKey , EncryptedText , DecryptedText , BlockNum , Var)


# In[ ]:




