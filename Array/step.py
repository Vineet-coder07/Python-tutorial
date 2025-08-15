import numpy as np
a=np.arange(10,1,-2)
print("\n a sequential array with negative step: \n",a)
newarr=a[np.array([3,1,2])]
print("\n elements at these indices are:\n",newarr)

b=np.arange(20)
print("\n array is :\n",b)
print("\n b[15]=",b[15])
#
print("\n b[-8:17:1]= ",b[-8:17:1])
print("\n b[10:] = ",b[10:])