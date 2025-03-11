
import numpy as np

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

print(kvaternionsko_mnozenje([np.sqrt(3)/2, 0, 1/2, 0], [0, 1, 2, 0]))
'''


def func(a, b):
    return a + b

print(func([1, 2], [5, 7]))
'''