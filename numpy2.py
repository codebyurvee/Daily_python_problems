import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
a2 = a[ : , np.newaxis]
print(a2.shape)
print(a2)
col = a[np.newaxis, :]
print(col)
print(col.shape)
