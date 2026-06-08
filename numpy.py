import numpy as np


a = np.array([1, 2, 3, 4, 5, 6])
b=a[3:]
print(a)
print(a[2])
print(a[:3])
print(a[3:])
print(a[1:5])
print(a[2:4])
print(b[2])

c =  np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(c[2,1])

# array attributes
print(c.ndim)
print(c.shape)
print(b.size)
print(a.dtype)


#array creation functions
d= np.zeros(4)
print(d)
e = np.ones(4)
print(e)
f = np.empty(2)
print(f)
g = np.arange(6)
print(g)
h = np.linspace(0, 10, num=5)
print(h)
i = np.ones(2, dtype=np.int64)#specify data type
print(i)

# sorting
j = np.array([2,4,52,633,5,3,99,39])
print(np.sort(j))

 # concatenate
k =np.concatenate((d,a))
print(k)

#reshaping array
l = np.arange(6)
m= np.reshape(l, (3,2))
print(m)



