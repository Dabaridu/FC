
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def kvaternionsko_mnozenje(p,q):
    p3 = p[1:]
    q3 = q[1:]
    #print(q3)
    pq1 = p[0] * q[0]
    pq2 = (np.dot(p3, q3))
    pq3 = [x * p[0] for x in q3]
    pq4 = [x * q[0] for x in p3]
    pq5 = np.cross(p3,q3)
    pq5 = pq5.tolist()
    pq12 = float(pq1 + pq2)
    #print(pq12)
    pq345 = [sum(x) for x in zip(pq3, pq4, pq5)]
    #print(pq345)
    pq345.insert(0,pq12)
    pq = pq345
    #print(pq)
    return pq

pvq = (kvaternionsko_mnozenje(kvaternionsko_mnozenje([np.sqrt(3)/2, 0, 1/2, 0], [0, 1, 2, 0]), [np.sqrt(3)/2, 0, -1/2, 0]))

#print(pvq)

v_nov = pvq[1:]

print(v_nov)

vector = [round(x,2) for x in v_nov]

print(vector)


#############################################


fig = plt.figure()
 

ax = plt.axes(projection="3d")


org = np.array([[1,0,0], [0,1,0], [0,0,1]])

vectors = np.array([vector, [1,2,0]])

colors = ['r', 'g', 'b', 'c', 'm']
label = ['x', 'y', 'z', "v'", 'v']

for i, v in enumerate(org):
    ax.quiver(0, 0, 0, *v, color=colors[i], label=f'Vector {label[i]}')
    ax.legend()

plt.pause(2)

for i, v in enumerate(vectors):
    a = ax.quiver(0, 0, 0, *v, color=colors[i+3], label=f'Vector {label[i+3]}')
    ax.legend()
    plt.pause(1)
    a.remove()


skp = np.concatenate((org, vectors))

ax.set_xlim([min(skp[:, 0].min(), 0), max(skp[:, 0].max(), 0)])
ax.set_ylim([min(skp[:, 1].min(), 0), max(skp[:, 1].max(), 0)])
ax.set_zlim([min(skp[:, 2].min(), 0), max(skp[:, 2].max(), 0)])
 
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')



plt.show()