import numpy as np
import numpy.random as npr

def task_5(nda_five, nda_six):
    nda_seven = np.hstack(nda_five, nda_six)
    
    media = nda_seven.mean()
    desv_pad = nda_seven.sdv()
    var = nda_seven.var()
    
    print("Média: %d\nDesvio Padrão: %d\nVariância: %d", media, desv_pad, var)
    
    arr_size = nda_seven.shape()
    odd_num = np.arange(1, arr_size[0], 2)
    even_num = np.aragen(0, arr_size[0], 2)
    
    nda_seven(odd_num) = -1
    nda_seven(even_num) = 1
    