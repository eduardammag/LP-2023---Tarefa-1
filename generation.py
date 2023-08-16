
import numpy as np
import numpy.random as npr

#1

a1D_1= np.arange(5,32,3)
print(a1D_1)

a1D_2 = npr.randint(3,77,9)
print(a1D_2)

a1D_soma = a1D_1 + a1D_2
print(a1D_soma)

#2
print(a1D_soma.shape)

