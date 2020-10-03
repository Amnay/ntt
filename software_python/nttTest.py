
import random
import numpy
import unittest
import nttUtils
import nttFuncs as ntt
import math

straightNTT = (ntt.straight_tf, ntt.pointValue_product, ntt.straight_Itf)
radix2NTT   = (ntt.radix2_tf,   ntt.pointValue_product, ntt.radix2_Itf)

def initVector():   
    veclen = random.randrange(100) + 1
    maxval = random.randrange(100) + 1
    return [random.randrange(maxval) for _ in range(veclen)]

class NumberTheoreticTransform(unittest.TestCase):

    TRIALS = 10
	
    # Check the different NTT transform implementations
    def test_transform(self):
        for _ in range(self.TRIALS):
            a = initVector()
            
            veclen = int(math.pow(2, math.ceil(math.log(len(a), 2))))
            x = ntt.addPadding(veclen, a)

            mod = nttUtils.find_mod(x)
            root = nttUtils.find_root(veclen, mod)
            c = straightNTT[0](x, root, mod)
            d = radix2NTT[0](x, root, mod)
            
            self.assertEqual(c, d)

    # Check the different NTT inverse transform implementations
    def test_inverse_transform(self):
        for _ in range(self.TRIALS):
            a = initVector()
            
            veclen = int(math.pow(2, math.ceil(math.log(len(a), 2))))
            x = ntt.addPadding(veclen, a)
            
            mod = nttUtils.find_mod(x)
            root = nttUtils.find_root(veclen, mod)
            
            c = straightNTT[2](x, root, mod)
            d = radix2NTT[2](x, root, mod)
            
            self.assertEqual(c, d)
            
    def test_NTTs(self):
        for _ in range(self.TRIALS):
            a, b = initVector(), initVector()
            
            c, root, mod = ntt.run(a, b, *straightNTT)
            d, root, mod = ntt.run(a, b, *radix2NTT)
            
            res = numpy.convolve(a, b).tolist()
            res = [v % mod for v in res]
            self.assertEqual(res, c)
            self.assertEqual(res, d)
    

    def test_roundtrip(self):
        for _ in range(self.TRIALS):
            a = initVector()
            
            veclen = int(math.pow(2, math.ceil(math.log(len(a), 2))))
            x = ntt.addPadding(veclen, a)
            
            mod = nttUtils.find_mod(x)
            root = nttUtils.find_root(veclen, mod)
            
            c = straightNTT[2](straightNTT[0](x, root, mod), root, mod)
            d = radix2NTT[2](radix2NTT[0](x, root, mod), root, mod)
			
            e = ntt.delPadding(c, len(a))
            f = ntt.delPadding(d, len(a))
            
            self.assertEqual(a, e)
            self.assertEqual(a, f)
    
    
    def test_linearity(self):
        for _ in range(self.TRIALS):
            a, b = initVector(), initVector()
            x, y = ntt.preprocess(a, b)
            root, mod = ntt.params(x, y)

            d = radix2NTT[0](x, root, mod)
            e = radix2NTT[0](y, root, mod)
            f = [(i + j) % mod for (i, j) in zip(d, e)]   

            z = [(i + j) % mod for (i, j) in zip(x, y)]   
            g = radix2NTT[0](z, root, mod)
            
            self.assertEqual(f, g)

if __name__ == "__main__":
    unittest.main()
