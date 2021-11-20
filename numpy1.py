import numpy as np
print(np.__version__)

a = [[11,12,13],[21,22,23],[31,32,33]]
A=np.array(a)

print(A.ndim)
print(A.shape)
print(A.size)
X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]])
Z=np.dot(X,Y)
print(Z)


