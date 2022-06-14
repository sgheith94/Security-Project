#!/usr/bin/env python
# coding: utf-8

# # <center> El GAMAL

# In[27]:


import random
from math import pow
from math import sqrt


# # 1) Keys Generation

# In[23]:


def KeyGenGamal():
    def gcd(a, b):
            if a < b:
                return gcd(b, a)
            elif a % b == 0:
                return b;
            else:
                return gcd(b, a % b)

    def PrimesInRange(x, y):
        prime_list = []
        for n in range(x, y):
            isPrime = True
            for i in range(2, n):
                if n % i == 0:
                    isPrime = False

            if isPrime:
                prime_list.append(n)

        return prime_list

    def isPrime(n):
        # Corner cases
        if (n <= 1):
            return False
        if (n <= 3):
            return True

        # This is checked so that we can skip middle five numbers in below loop
        if (n % 2 == 0 or n % 3 == 0):
            return False
        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6

        return True

    # Square and Multiply
    def power(x, y, p):
        res = 1 # Initialize result
        x = x % p # Update x if it is morethan or equal to p
        while (y > 0):
            # If y is odd, multiply x with result
            if (y & 1):
                res = (res * x) % p

            # y must be even now
            y = y >> 1 # y = y/2
            x = (x * x) % p

        return res

    def findPrimefactors(s, n):
        # Print the number of 2s that divide n
        while (n % 2 == 0):
            s.add(2)
            n = n // 2

        # n must be odd at this point. So we can skip one element (Note i = i +2)
        for i in range(3, int(sqrt(n)), 2):
            # While i divides n, print i and divide n
            while (n % i == 0):
                s.add(i)
                n = n // i

        # This condition is to handle the case when n is a prime number greater than 2
        if (n > 2):
            s.add(n)

    def findPrimitive(n):
        s = set()
        if (isPrime(n) == False):
            return -1
        phi = n - 1

        findPrimefactors(s, phi)

        # Check for every number from 2 to phi
        for r in range(2, phi + 1):
            # Iterate through all prime factors of phi. and check if we found a power with value 1
            flag = False
            for it in s:
                # Check if r^((phi)/primefactors) mod n is 1 or not
                if (power(r, phi // it, n) == 1):
                    flag = True
                    break

            # If there was no power with value 1.
            if (flag == False):
                return r

        # If no primitive root found
        return -1

    #prime_list = PrimesInRange(1000,9999)
    #q = random.choice(prime_list)
    q = 1000000000000000000000000000000000000000000000
    #print("q:",q)

    a = findPrimitive(q)
    #print("a:",a)

    R_private_key = random.randint(1, q-1) # Private key for Reciever Xa
    R_public_key = power(a, R_private_key, q) # Public key for Reviever Ya

    #print("Reciever private key:", R_private_key)
    #print("Reciever public key:", R_public_key)

    k = random.randint(1, q) # Sender chooses randomly
    S_private_key = power(R_public_key, k, q) # K

    #print("k:", k)
    #print("Sender's K:", S_private_key)
        
    return S_private_key, R_private_key, k, a, q,R_public_key


# ### 2) Encryption

# In[24]:


def encrypt(plain_text, S_private_key, a, k, q):
    
    def power(x, y, p):
        res = 1 # Initialize result
        x = x % p # Update x if it is morethan or equal to p
        while (y > 0):
            # If y is odd, multiply x with result
            if (y & 1):
                res = (res * x) % p

            # y must be even now
            y = y >> 1 # y = y/2
            x = (x * x) % p

        return res
    
    KM = []
    C2 = []
    M = []
    
    C1 = power(a, k, q)
    
    for i in range(0, len(plain_text)):
        M.append(ord(plain_text[i]))
        
    #print("M:", M)
    
    for i in range(0, len(M)):
        KM.append(S_private_key * M[i])
        
    #print("KM:", KM)
    
    for n in range(len(KM)):
        C2.append(power(KM[n], 1, q))
    
    return C1, C2


# ### 3) Decryption

# In[25]:


def decrypt(C2, C1, R_private_key, q):
    
    def power(x, y, p):
        res = 1 # Initialize result
        x = x % p # Update x if it is morethan or equal to p
        while (y > 0):
            # If y is odd, multiply x with result
            if (y & 1):
                res = (res * x) % p

            # y must be even now
            y = y >> 1 # y = y/2
            x = (x * x) % p

        return res
    
    def eea(a,b):
        if(a%b==0):
            return(b,0,1)
        else:
            gcd,s,t = eea(b,a%b)
            s = s-((a//b) * t)
            #print("%d = %d(%d) + (%d)(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
    
    def multinv(e,r):
        gcd,s,_ = eea(e,r)
        if(gcd!=1):
            return None
        return s%r
    
    message = []
    text = []
    C2_times_Kinv = []
    
    K = power(C1, R_private_key, q)
    #print("Reciever's K:", K)
    
    K_inverse = multinv(K, q)
    #print("K Inverse:", K_inverse)
    
    for n in range(len(C2)):
        C2_times_Kinv.append(C2[n] * K_inverse)
        message.append(power(C2_times_Kinv[n], 1, q))
    
    for i in range(0, len(message)):
        text.append(chr(int(message[i])))
        
    return text, message


# ### Main

# In[26]:


# S_private_key, R_private_key, k, a, q = KeyGenGamal()
# print("Sender private_key", S_private_key)
# print("Receiver private key", R_private_key)
# print("k", k)

# plain_text = input("Ekteb Hena: ")
# C1, C2 = encrypt(plain_text, S_private_key, a, k, q)
# print("C1:", C1)
# print("C2:", C2)

# decrypted_message, K = decrypt(C2, C1, R_private_key, q)    
# dmsg = ''.join(decrypted_message)
# print("Message:", dmsg)


# # <center> Log Files

# ### Encryption Log File

# In[20]:


def EncryptLog(R_private_key,R_public_key,S_private_key,k,C1,C2):
    with open('EncryptionG.txt', 'w') as f:
        f.write('Keys Generated:')
        f.write('\n')
        f.write('Reciever private key Xa :' + str(R_private_key))
        f.write('\n')
        f.write('Reciever public key Ya:' +  str(R_public_key))
        f.write('\n')
        f.write('k:' + str(k))
        f.write('\n')
        f.write('K generated for encryption:' + str(S_private_key))
        f.write('\n')
        f.write('Encryption:')
        f.write('\n')
        f.write('C1:' + str(C1))
        f.write('\n')
        f.write('C2:' + str(C2))


# ### Decryption Log File

# In[22]:


def DecryptLog(K,dmsg):
    with open('DecryptionGamal.txt', 'w') as f:
        f.write('Reciever K:' + str(K))
        f.write('\n')
        f.write('Decrypted Message:' + str(dmsg))


# In[ ]:




