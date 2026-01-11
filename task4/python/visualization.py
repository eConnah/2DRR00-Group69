import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd

# Load the projections
C = np.load('term_projections.npy')
D = np.load('doc_projections.npy')

# Compute SVD to get singular values for scaling
A = np.array([
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
], dtype=float)

U, sigma, Vt = svd(A, full_matrices=False)
sigma_12 = sigma[:2]

# Scale projections by singular values to show actual contribution
C_scaled = C * sigma_12
D_scaled = D * sigma_12

terms = ['Tree', 'Leaf', 'Branch', 'Root', 'Coral', 'Shark', 'Whale', 'Water', 'Habitat', 'Oxygen']
documents = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']

# Color-code terms by domain
colors_terms = {
    'Tree': 'green', 'Leaf': 'green', 'Branch': 'green', 'Root': 'green',  # Forest terms
    'Coral': 'blue', 'Shark': 'blue', 'Whale': 'blue', 'Water': 'blue',   # Ocean terms
    'Habitat': 'purple', 'Oxygen': 'purple'  # Overlapping terms
}

# Create Figure 1: Term projections (scaled by singular values)
fig, ax = plt.subplots(figsize=(10, 8))

for i, term in enumerate(terms):
    color = colors_terms[term]
    ax.scatter(C_scaled[i, 0], C_scaled[i, 1], s=200, color=color, alpha=0.7, edgecolors='black', linewidth=1.5)
    ax.annotate(term, (C_scaled[i, 0], C_scaled[i, 1]), fontsize=10, fontweight='bold',
                xytext=(5, 5), textcoords='offset points', ha='left')

ax.set_xlabel('First Singular Component (σ₁u₁)', fontsize=12, fontweight='bold')
ax.set_ylabel('Second Singular Component (σ₂u₂)', fontsize=12, fontweight='bold')
ax.set_title('Term Projections in 2D Space (Scaled by Singular Values)', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='green', alpha=0.7, edgecolor='black', label='Forest terms'),
    Patch(facecolor='blue', alpha=0.7, edgecolor='black', label='Ocean terms'),
    Patch(facecolor='purple', alpha=0.7, edgecolor='black', label='Overlapping terms')
]
ax.legend(handles=legend_elements, loc='best', fontsize=10)

plt.tight_layout()
plt.savefig('term_projections.png', dpi=300, bbox_inches='tight')
print("✓ Saved term_projections.png")
plt.show()

# Create Figure 2: Document projections (scaled by singular values)
fig, ax = plt.subplots(figsize=(10, 8))

# Color-code documents
doc_colors = []
for i in range(1, 11):
    if i <= 4:
        doc_colors.append('green')  # Forest documents (1-4)
    elif i <= 6:
        doc_colors.append('purple')  # Overlapping documents (5-6)
    else:
        doc_colors.append('blue')    # Ocean documents (7-10)

for i, doc in enumerate(documents):
    ax.scatter(D_scaled[i, 0], D_scaled[i, 1], s=200, color=doc_colors[i], alpha=0.7, edgecolors='black', linewidth=1.5)
    ax.annotate(doc, (D_scaled[i, 0], D_scaled[i, 1]), fontsize=10, fontweight='bold',
                xytext=(5, 5), textcoords='offset points', ha='left')

ax.set_xlabel('First Singular Component (σ₁v₁)', fontsize=12, fontweight='bold')
ax.set_ylabel('Second Singular Component (σ₂v₂)', fontsize=12, fontweight='bold')
ax.set_title('Document Projections in 2D Space (Scaled by Singular Values)', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

# Add legend
legend_elements = [
    Patch(facecolor='green', alpha=0.7, edgecolor='black', label='Forest documents (D1-D4)'),
    Patch(facecolor='purple', alpha=0.7, edgecolor='black', label='Overlapping documents (D5-D6)'),
    Patch(facecolor='blue', alpha=0.7, edgecolor='black', label='Ocean documents (D7-D10)')
]
ax.legend(handles=legend_elements, loc='best', fontsize=10)

plt.tight_layout()
plt.savefig('document_projections.png', dpi=300, bbox_inches='tight')
print("✓ Saved document_projections.png")
plt.show()

print("\nBoth plots have been generated and saved!")
