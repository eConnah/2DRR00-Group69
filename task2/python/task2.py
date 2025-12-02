import numpy as np

airports = ['Amsterdam', 'Barcelona', 'Berlin', 'Bratislava', 'Eindhoven', 'Frankfurt', 'London', 'Maastricht', 'Paris', 'Prague', 'Riga', 'Tallinn', 'Vilnius']


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


connections_normalized = connections / np.abs(connections).sum(axis=0)




print(connections_normalized)