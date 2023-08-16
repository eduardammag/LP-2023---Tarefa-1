import numpy as np

def task_7():
    nda_8 = np.matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    nda_I3 = np.eye(3, dtype = int)
    
    determinante = np.linalg.det(nda_8)
    nda_inv = np.linalg.inv(nda_8)
