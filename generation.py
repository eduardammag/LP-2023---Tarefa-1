import numpy as np
import numpy.random as npr

#1

nda_int= np.arange(5,32,3)
print(nda_int)

nda_rand = npr.randint(3,77,9)
print(nda_rand)

nda_soma = nda_int + nda_rand
print(nda_soma)