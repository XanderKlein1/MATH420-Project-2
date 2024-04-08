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
