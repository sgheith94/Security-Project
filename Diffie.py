#!/usr/bin/env python
# coding: utf-8

# # <center> Diffie-Helman

# In[1]:


import random
import sympy
from random import randint
from math import pow
from math import sqrt


# In[10]:


def Diffie():
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
    
    def ConversionDecToBin(num):
        res = bin(num).replace("0b", "")
        if(len(res)%4 != 0):
            div = len(res) / 4
            div = int(div)
            counter =(4 * (div + 1)) - len(res)
            for i in range(0, counter):
                res = '0' + res
        return res
    
    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)


    flag_prime = 0
    ct = 0
    while flag_prime == 0:
        ct += 1
        q = random_with_N_digits(17)
        f_isprime = sympy.isprime(q)
        if f_isprime == True:
            flag_prime = 1
            #print(q)
            break
            
    q1 = ConversionDecToBin(q)
    q1 = len(q1)
    #print("q1:",q1)

    a = findPrimitive(q)
    #print("a:",a)

    Xa = random.randint(1, q) # Private key for Reciever
    Ya = power(a, Xa, q) # Public key for Reviever

    #print("Reciever private key:", Xa)
    #print("Reciever public key:", Ya)

    Xb = random.randint(1, q) # Private key for Sender
    Yb = power(a, Xb, q) # Public key for Sender

    #print("Sender private key:", Xb)
    #print("Sender public key:", Yb)

    #p = Xa *Xb
    #Kab = power(a, p, q) #  Shared session key

    Ka = power(Yb, Xa, q) # Reciver computes this to get (Kab)
    
    x = ConversionDecToBin(Ka)
    len_x = len(x)
#     print("x",x)
#     print("len",len_x)

    Kb = power(Ya, Xb, q) 
    
    # Sender computes this to get (Kab)
    #print("Reciver secret key Ka:", Ka)
    #print("Sender secret key Kb:", Kb)

    return Ka, Kb, x


# In[11]:


# Ka, Kb, x = Diffie()
# print("Reciver shared secret key Ka:", Ka)
# print("Sender shared secret key Kb:", Kb)


# In[ ]:




