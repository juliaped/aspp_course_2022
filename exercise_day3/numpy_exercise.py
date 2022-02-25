#! /bin/bash/env python
import numpy as np

#day3_1a: Creating null vector of size 10 with 5th value = 1
np_v = np.zeros(10)
np_v[4] = 1
print('np_v: ', np_v)

#day3_1b: Creating vector ranging from 10-49
np_f = np.arange(10,50)
print('np_f: ', np_f)

#day3_1c: Reverse vector f
np_f_rev = np_f[::-1]
print('np_f_rev: ', np_f_rev)

#day3_1d: create 3x3 matrix with values 0-8
np_g = np.arange(0,9).reshape(3,3)
print('np_g: ', np_g)

#day3_1e: find indices of non-zero element from [1,2,0,0,4,0]
np_k = np.array([1,2,0,0,4,0])
nonzero_np_k = np.nonzero(np_k)
print('nonzero_np_k: ', nonzero_np_k)

#day3_1f: create random vector (size 30) and find mean value
np_l = np.random.random(30)
mean_np_l = np.mean(np_l)
print('mean_np_l: ', mean_np_l)

#day3_1g: create 2d array with 1 on the border and 0 inside
np_p = np.ones((6,6))
np_p[1:-1,1:-1] = 0
print('np_p: ', np_p)

#day3_1h: create 8x8 matrix and fill ir with a checkbord pattern
np_s = np.ones((8,8), dtype=int)
np_s[1::2,::2] = 0
np_s[::2,1::2] = 0
print('np_s: ', np_s)

#day3_1i: create a checkerboard 8x8 matrix using the tile function
np_t1 = np.array([0,1,1,0]).reshape(2,2)
np_t2 = np.tile(np_t1, (4,4))
print('np_t2: ', np_t2)

#day3_1j: given 1D array , negate all elements which are between 3 and 8, in place
Z = np.arange(11)
x = (Z > 2) & (Z < 9)
Z[x] *= -1
print('Z: ', Z)

#day3_1k: create a random vector of size 10 and sort it
np_m = np.random.random(10)
np_m_sorted = np.sort(np_m)
print('np_m_sorted: ', np_m_sorted)

#day3_1l: consider two random array A and B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
print(A == B)

#day3_1m: how to convert an integer (32 bits) array into a float (32 bits) in place
Y = np.arange(10, dtype=np.int32)
print(Y.dtype)
Y_conv = Y.astype('float32')
print(Y_conv.dtype)

#day3_1n: how to get the diagonal of a dot product
C = np.arange(9).reshape(3,3)
D = C + 1
E = np.dot(C,D)
F = np.diag(E)
print('E: ', E)
print('F: ', F)
