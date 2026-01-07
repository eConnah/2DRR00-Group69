import numpy as np
from pprint import pprint

airports = ['Amsterdam', 'Barcelona', 'Berlin', 'Bratislava', 'Eindhoven', 'Frankfurt', 'London', 'Maastricht', 'Paris', 'Prague', 'Riga', 'Tallinn', 'Vilnius']

# from ⌜ to
connections = np.array([
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
])

def print_connections():
    for i in range(13):
        for j in range(13):
            if connections[i, j] == 1:
                print(f"{airports[i]} connects to {airports[j]}")

def print_matrix(m):
    for i in m:
        for j in i:
            print(f"{int(j):4}" if j == 0 else f"{j:4.2f}", end=" ")
        print()
                

connections_normalized = connections / np.abs(connections).sum(axis=0)  # normalize connections (G)


def compute_page_rank(p):
    n = len(connections)
    A = p * connections_normalized + (1 - p) * (1 / n) * np.ones((13,13))

    evalues, evectors = np.linalg.eig(A)  # compute eigenvalues and eigenvectors

    idx = np.where(np.isclose(evalues, 1.0, atol=1e-8))[0]  # filter to eigenvectors w/ ʎ = 1
    eigvec = evectors[:, idx]

    eigvec = eigvec.flatten()  # convert to vector

    eigvec_normal = np.abs(eigvec) / np.abs(eigvec).sum()  # normalize for ||x||1 = 1 and all x>=0

    eigvec_normal = np.round(eigvec_normal, 2)  # round to 2 decimal places

    for i in range(len(airports)):   # print
        print(f"{airports[i]} : {eigvec_normal[i]}")


compute_page_rank(0.85)
print("- "*10)
compute_page_rank(0.99)
print("- "*10)
compute_page_rank(0.50)