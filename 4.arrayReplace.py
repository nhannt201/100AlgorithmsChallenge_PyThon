#arrayReplace
import numpy as np

def rparray(arr, n):
    print(np.where(np.array(arr)==1, n, np.array(arr)) )

myarray = [1,2,1]
rparray(myarray, 3)
