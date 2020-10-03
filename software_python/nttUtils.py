import math
import random
import itertools

# Reverse binary number
def rev(num,n): 
    binary = bin(num)
    reverse = binary[-1:1:-1]
    reverse = reverse + ((n-1).bit_length() - len(reverse))*'0'
    return int(reverse, 2)

# List bit-reverse-copy
def bitRevCopy(x):
    x_len = len(x)
    return [x[rev(i, len(x))] for i in range(len(x))]

# Euclidean Greatest Common Divisor
def egcd(a, b):
    if a == 0: return (0, 1)
    else:
        y, x = egcd(b % a, a)
        return (x - (b // a) * y, y)

def reciprocal(a, mod):
    x, y = egcd(a, mod)
    return x % mod
    
def isPrime(n):
    if n < 2  or n%2 == 0 or n%3 == 0: return False
    if n == 2 or (n < 9 and n%2 != 0): return True
    
    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f     == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True

def unique_prime_factors(n):
    result = []
    i = 2
    end = math.floor(math.sqrt(n))
    while i <= end:
        if n % i == 0:
            n //= i
            result.append(i)
            while n % i == 0: n //= i
            end = math.floor(math.sqrt(n))
        i += 1
    if n > 1: result.append(n)
    return result
    
def is_generator(x, mod):
    pf = unique_prime_factors(mod-1)
    return pow(x, mod-1, mod) == 1 and all((pow(x, int((mod-1) / p), mod) != 1) for p in pf)

def find_mod(vector):
    n = len(vector)
    min_mod = max(n, max(vector)+1)
    k_1 = math.ceil((min_mod - 1) / n)
    for k in itertools.count(max(k_1, 1)):
        mod = k * n + 1
        if isPrime(mod):
            return mod

def find_root(veclen, mod):
    for i in range(1, mod):
        if is_generator(i, mod): gen = i

    root = pow(gen, int((mod-1) / veclen), mod)
    return root
    
# l = list(random.randrange(1,4) for i in range(10))
# print(l)
# m = find_mod(l)
# r = find_root(l,m)
# print("g^k % mod -- ", r, " % ", m)
# for i in range(0,len(l)+1):
    # print(pow(r,i,m))