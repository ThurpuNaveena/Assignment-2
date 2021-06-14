# -*- coding: utf-8 -*-
"""Assignment-2.py(part-1)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O3jfoe4Vrxgunm5KVK4qDQgrZCqeHbcb
"""

import numpy as np
import matplotlib.pyplot as plt
 
 
def dir_vec(A,B):
  return B-A
 
def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))
 
#Generate line points
#def line_gen(A,B):
#  len =10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,1,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*(B-A)
#    x_AB[:,i]= temp1.T
#  return x_AB
 
#Generate line intercepts
def line_icepts(n,c):
  e1 = np.array([1,0]) 
  e2 = np.array([0,1]) 
  A = c*e1/(n@e1)
  B = c*e2/(n@e2)
  return A,B
 
 
 
def line_gen_varlen(A,m, k1, k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
 
#Generate line points
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
 
#Generate line point
#def line_dir_pt(m,A, dim):
#  len = 10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,10,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*n1
#    x_AB[:,i]= temp1.T
#  return x_AB
 
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
 
 
def line_gen_varlen(A,B, k1, k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
 
 
#def line_dir_pt(n1,A, dim):
#  len = 10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,10,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*n1
#    x_AB[:,i]= temp1.T
#  return x_AB
 
 
#Inputs
M = np.array([1,-2])
A = np.array([-3,0]) 
 
 
#Generating all lines
x_AM = line_gen(A,M)
 
#Plotting all lines
plt.plot(x_AM[0,:],x_AM[1,:],label='$AM$')
 
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 + 0.03) , 'A')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 - 0.2), M[1] * (1) , 'M')
 
 
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
 
plt.show()