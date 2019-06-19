import math
import numpy as np

list = [226, 253,247,225,233,257,287,229,236,328,371,425,378,433,415,455,534,640,655,577,605,702, 736, 960
]

minx = 0.9231163463866358
maxx = 1.0832870676749586 

arr = np.array(list)
arr = arr.astype(np.float64)
lam = []
for i in range(0, 10000, 1):
    new_array = arr + i
    for j in range(2,24):
        lam.append(new_array[j-1]/new_array[j])
    if ((max(lam) < maxx) and (min(lam) > minx)):
        print(i)
    lam = []

