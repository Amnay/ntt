
from nttUtils import *

def addPadding(n, vec):
    res = vec.copy()
    res.extend([0] * (n-len(vec)))
    return res

def delPadding(vec, *n):
    if len(n) > 2: raise Exception("There must be 1 or 2 length args")
    m = sum(n) + (-1 if len(n) == 2 else 0)
    return vec[:(len(vec)-(len(vec)-m))]
    
def preprocess(a, b):
    veclen = int(math.pow(2, math.ceil(math.log(len(a)+len(b)-1, 2))))
    x = addPadding(veclen, a)
    y = addPadding(veclen, b)
    
    return x, y

def params(*vectors):
    mod  = max([find_mod(v) for v in vectors])
    root = find_root(len(vectors[0]), mod)
    return root, mod
    
def run(a, b, transform, product, Itransform):
    x, y = preprocess(a, b)
    
    root, mod = params(x, y)
    
    c = transform(x, root, mod)
    d = transform(y, root, mod)
    e = product(c,d, mod)
    f = Itransform(e, root, mod)
    g = delPadding(f, len(a), len(b))
    return (g, root, mod)

def pointValue_product(C, D, mod):
    return [(c * d) % mod for c, d in zip(C, D)]

def straight_tf(vector, root, mod):
    y = []
    for i in range(len(vector)):
        y_n = 0
        for j, val in enumerate(vector):
            y_n += val * pow(root, i * j, mod)
            y_n %= mod
        y.append(y_n)
    return y

def straight_Itf(vector, root, mod):
    g       = reciprocal(root, mod)
    scaler  = reciprocal(len(vector), mod)
    y       = straight_tf(vector, g, mod)
    return [((y_n * scaler) % mod) for y_n in y]

def radix2_tf(vector, root, mod):
    b = bitRevCopy(vector)
    n = len(b)
    for s in range(1, int(math.log(n,2)) + 1):  # level from bottom to top
        m   = pow(2,s)                          # number of coeffs per node
        g_m = pow(root, int(n/m))               # root^[nodes on that level]
        for k in range(0, n, m):                # node index 0:m:n (skip m)
            g = 1
            for j in range(int(m/2)):           # each coeff within half-node
                left    = b[k + j]
                right   = (g * b[k + j + int(m/2)]) % mod
                b[k + j]            = (left + right) % mod  # first half
                b[k + j + int(m/2)] = (left - right) % mod  # second half
                g = (g * g_m) % mod
                
    return b

def radix2_Itf(vector, root, mod):
    g       = reciprocal(root, mod)
    scaler  = reciprocal(len(vector), mod)
    y       = radix2_tf(vector, g, mod)
    return [((y_n * scaler) % mod) for y_n in y]
    