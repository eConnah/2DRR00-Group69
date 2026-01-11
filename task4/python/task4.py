import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd

terms = ['Tree', 'Leaf', 'Branch', 'Root', 'Coral', 'Shark', 'Whale', 'Water', 'Habitat', 'Oxygen']
documents = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']

A = np.array([
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 1],  # Tree
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Leaf
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1],  # Branch
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],  # Root
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],  # Coral
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # Shark
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],  # Whale
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],  # Water
    [0, 1, 1, 0, 1, 1, 0, 0, 1, 0],  # Habitat
    [0, 1, 1, 0, 1, 1, 0, 0, 1, 0],  # Oxygen
], dtype=float)

print("Term-Document Matrix A:")
print(A)
print(f"\nMatrix shape: {A.shape}")
print(f"Sparsity: {np.count_nonzero(A)} non-zero elements out of {A.size} ({100*np.count_nonzero(A)/A.size:.1f}%)")

U, sigma, Vt = svd(A, full_matrices=False)

print("\n" + "="*50)
print("SVD Decomposition")
print("="*50)
print(f"\nSingular values (σ): {sigma}")
print(f"\nU shape: {U.shape}")
print(f"V^T shape: {Vt.shape}")

U_12 = U[:, :2]
V_12 = Vt[:2, :].T 

print(f"\nU_{1,2} shape: {U_12.shape}")
print(f"V_{1,2} shape: {V_12.shape}")


u1 = U_12[:, 0]
v1 = V_12[:, 0]

if (u1 < 0).sum() > (u1 >= 0).sum():
    U_12[:, 0] = -U_12[:, 0]
    v1 = -v1

if (v1 < 0).sum() > (v1 >= 0).sum():
    V_12[:, 0] = -V_12[:, 0]

print("\nAfter ensuring u1 and v1 are nonnegative:")
print(f"u1 (first column of U_12): {U_12[:, 0]}")
print(f"v1 (first column of V_12): {V_12[:, 0]}")

C = U_12.copy()
print(f"\nTerm projections (C): {C.shape}")
print("Term projections (c_j):")
for i, term in enumerate(terms):
    print(f"  {term}: ({C[i, 0]:.3f}, {C[i, 1]:.3f}), norm: {np.linalg.norm(C[i]):.3f}")

D = V_12.copy()
print(f"\nDocument projections (D): {D.shape}")
print("Document projections (d_j):")
for i, doc in enumerate(documents):
    print(f"  {doc}: ({D[i, 0]:.3f}, {D[i, 1]:.3f}), norm: {np.linalg.norm(D[i]):.3f}")

np.save('term_projections.npy', C)
np.save('doc_projections.npy', D)
print("\n✓ Projections saved to term_projections.npy and doc_projections.npy")
