import numpy as np
import matplotlib.pyplot as plt
import math

f = open("kn57Nodes1to57_adj20.txt", 'r')
nodes_and_edges = f.readline()
nodes_and_edges = np.fromstring(nodes_and_edges, dtype=int, sep=' ')
print("number of nodes:", nodes_and_edges[0], "\nnumber of edges (m) : ", nodes_and_edges[1])
ADJ_MATRIX = np.zeros((57,))
m = nodes_and_edges[1]

for x in f:
  line = np.fromstring(x, dtype=int, sep = ' ' )
  #print(line)
  ADJ_MATRIX = np.vstack((ADJ_MATRIX,line))

#convert each line into a numpy array
#print(ADJ_MATRIX.shape)
ADJ_MATRIX = np.delete(ADJ_MATRIX,0,0)
#print(ADJ_MATRIX)

qtup = set([])
#f = open("tup5.txt","w")
def qcliques(mat,q):
  if q == 3:
    for i in range(mat.shape[0]):
      for j in range(i+1,mat.shape[0]):
          for k in range(j+1,mat.shape[0]):
            if mat[k][i] == 1 and mat[k][j]==1 and mat[j][i] == 1:
              qtup.add((i,j,k))
 #             f.write("(" + str(i) + "," + str(j) + "," + str(k) + ")\n")
  if q == 4:
    for i in range(mat.shape[0]):
      for j in range(i + 1, mat.shape[0]):
          for k in range(j + 1,mat.shape[0]):
            for l in range(k + 1,mat.shape[0]):
              if mat[i][j] == 1 and mat[i][k] == 1 and mat[i][l] == 1 and mat[j][k] == 1 and mat[j][l] == 1 and mat[k][l] == 1:
                qtup.add((i,j,k,l))
  #              f.write("(" + str(i) + "," + str(j) + "," + str(k) + "," + str(l) + ")\n")
  if q == 5:
    for i in range(mat.shape[0]):
      for j in range(i + 1, mat.shape[0]):
          for k in range(j + 1,mat.shape[0]):
            for l in range(k + 1,mat.shape[0]):
              for m in range(l + 1, mat.shape[0]):
                if mat[i][j] == 1 and mat [i][k] == 1 and mat[i][l] and mat[i][m] == 1 and mat[j][k] == 1 and mat[j][l] == 1 and mat[j][m] == 1 and mat[k][l] == 1 and mat[k][m] == 1 and mat[l] [m] == 1:
                  qtup.add((i,j,k,l,m))
   #               f.write("(" + str(i) + "," + str(j) + "," + str(k) + "," + str(l) + "," + str(m) +  ")\n")


  #print(mat.shape)

qtup.clear()
qcliques(ADJ_MATRIX,3)
print("number of 3-cliques (t) :",len(qtup))
t = len(qtup)
#NEW_MAT = np.array(([0,1,1,1],[1,0,1,1],[1,1,0,0],[1,1,0,0]))
#(qcliques(NEW_MAT,3))
qtup.clear()
qcliques(ADJ_MATRIX,4)
print("number of 4-cliques (f) :", len(qtup))
f = len(qtup)

ER_MLE = 2*nodes_and_edges[1]/(nodes_and_edges[0] * (nodes_and_edges[0]-1))
print("Erdos Renyi MLE (p):",ER_MLE)
#Erdos Renyi Class of prediciting the number of q cliques

# 3 cliques estimate
three_clique = math.comb(nodes_and_edges[0],3) * (ER_MLE ** 3)
print("Expected number of 3-cliques for ER:", three_clique)
# 4 clieques estimate
four_clique = math.comb(nodes_and_edges[0], 4) * (ER_MLE ** 6)
print("Expected number of 4-cliques for ER:", four_clique)

#SSBM Method of Moment Matching
n = nodes_and_edges[0]
m = nodes_and_edges[1]
qtup.clear()
qcliques(ADJ_MATRIX,3)
t = len(qtup)
c1 = 4*m/(n*(n-1))
c2 = 24*t/(n*(n-1)*(n-2))
a = 1/2*(c1 + math.pow((2*c2-math.pow(c1,3)),1/3))
b = 1/2*(c1 - math.pow((2*c2-math.pow(c1,3)),1/3))
print("Estimated value for a = " + str(a))
print("Estimated value for b = " + str(b))

n = nodes_and_edges[0]
En1 = n/2
En2 = (n**2 + n)/4
En3 = (n**2)*(n+3)/8
En4 = (n*(n+1)*(n**2 + 5*n -2))/16

part1 = (a**6/24)*(2*En4 - 4*n*En3 + En2*(6*(n**2) - 18 * n + 22) + En1*(-4*n**3 + 18*(n**2) - 22*n) + n**4 - 6*(n**3)+11*(n**2) - 6*n)
part2 = (a**3 * b **3)/6 * (-2*En4 + 4*n*En3 + En2*(-3*(n**2) + 3*n - 4) + En1*(n**3 - 3*(n**2)))
part3 = (a**2)*(b**4)/4 * (En4 - 2*n*En3 + (n**2+n-1)*En2 + (-1*(n**2)+n)*En1)

EX4 = part1 + part2 + part3
print("Expectation of # of 4-cliques: " + str(EX4))