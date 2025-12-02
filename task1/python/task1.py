import numpy as np
import math



v = np.array([
    1,
    2,
    3,
    4,
    5,
    6,
    7
])

w = np.array([
    2,
    4,
    7,
    9,
    4,
    5,
    9
])


print(v.shape)
print(w.shape)


norm_v = np
norm_w = np.norm(w)

dot = np.dot(v,w)

c = dot / (norm_v * norm_w)

print(c)

