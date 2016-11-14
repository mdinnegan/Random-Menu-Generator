#defined lists
A = ['delicious','tasty','dangerous','glorious','illegal','klutzy','original','royal','thunderous','witty']
B = ['sugary','buttery','creamy','crispy','bitter','juicy','tart','tender','spicy','salty']
C = ['waffles','spaghetti','chicken','donuts','eggplants','cheese','hotdogs','apples','hamburgers','soup']

#choosing out of the lists
import random
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
print(A[a],B[b],C[c])
del(A[a],B[b],C[c])

d = random.randint(0,8)
e = random.randint(0,8)
f = random.randint(0,8)
print(A[d],B[e],C[f])
del(A[d],B[e],C[f])

g = random.randint(0,7)
h = random.randint(0,7)
i = random.randint(0,7)
print(A[g],B[h],C[i])
del(A[g],B[h],C[i])

j = random.randint(0,6)
k = random.randint(0,6)
l = random.randint(0,6)
print(A[j],B[k],C[l])
del(A[j],B[k],C[l])

m = random.randint(0,5)
n = random.randint(0,5)
o = random.randint(0,5)
print(A[m],B[n],C[o])
del(A[m],B[n],C[o])

p = random.randint(0,4)
q = random.randint(0,4)
r = random.randint(0,4)
print(A[p],B[q],C[r])
del(A[p],B[q],C[r])

s = random.randint(0,3)
t = random.randint(0,3)
u = random.randint(0,3)
print(A[s],B[t],C[u])
del(A[s],B[t],C[u])

v = random.randint(0,2)
w = random.randint(0,2)
x = random.randint(0,2)
print(A[v],B[w],C[x])
del(A[v],B[w],C[x])

y = random.randint(0,1)
z = random.randint(0,1)
D = random.randint(0,1)
print(A[y],B[z],C[D])
del(A[y],B[z],C[D])

E = random.randint(0,0)
F = random.randint(0,0)
G = random.randint(0,0)
print(A[E],B[F],C[G])