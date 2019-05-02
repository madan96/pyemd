import numpy as np
from pyemd import emd
from pyemd import emd_with_flow

s1 = 3
s2 = 5
np.random.seed(10)

a = np.random.rand(s1)
b = np.random.rand(s2)
d = np.random.rand(s1, s2)

result1 = emd(a, b, d)
result2 = emd_with_flow(a, b, d)

print (result1, result2)