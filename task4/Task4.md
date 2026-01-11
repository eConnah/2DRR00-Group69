# Plan
I choose two topics that slightly overlap, forest and ocean.
The 10 terms I choose are: Tree, Coral, Leaf, Shark, Branch, Whale, Root, Water, Habitat, Oxygen.
Disclaimer AI was used to generate the 10 documents as I could not find a good source that wouldn't contain too much of the words:

## Documents
1. An ancient Tree stands tall with a lush green Leaf canopy, towering above the misty Water nearby.
2. A bird perches on a low Branch near the exposed Root of the tree, while Oxygen flows through the Habitat.
3. This healthy forest Habitat breathes and produces fresh Oxygen, creating a refuge for many species.
4. Fallen debris on the forest floor includes a Tree Branch and a withered Leaf along with Coral fragments washed ashore.
5. The vast open Water serves as a natural Habitat for the migrating Whale and has plenty of Oxygen.
6. Tiny bubbles show there is plenty of Oxygen dissolved in the Water, supporting both forest and ocean Habitats.
7. A vibrant Coral reef provides a hunting ground for a lone Shark in the deep Water.
8. We spotted a Whale diving deep into the cold Water near the Roots of submerged Tree stumps.
9. A tropical Coral reef is a busy Habitat for many species with fresh Oxygen and Water currents.
10. A large Shark glides silently through the clear blue Water near ancient Tree Roots and Branches.

$$
\begin{bmatrix}
\text{Terms} & \text{D1} & \text{D2} & \text{D3} & \text{D4} & \text{D5} & \text{D6} & \text{D7} & \text{D8} & \text{D9} & \text{D10}\\
\text{Tree} & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 1\\
\text{Leaf} & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
\text{Branch} & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 1\\
\text{Root} & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1\\
\text{Coral} & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 1 & 0\\
\text{Shark} & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1\\
\text{Whale} & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0\\
\text{Water} & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1\\
\text{Habitat} & 0 & 1 & 1 & 0 & 1 & 1 & 0 & 0 & 1 & 0\\
\text{Oxygen} & 0 & 1 & 1 & 0 & 1 & 1 & 0 & 0 & 1 & 0
\end{bmatrix}
$$

# Results
## Overall
When we ran SVD on our term-document matrix it naturally pulled apart forest-related words from ocean-related words, while also highlighting the words which bridge both together.

## What the Graph Tells Us
### Seperations
When we plot everything on the graph, you can see clear groups forming:
- All the forest words (Tree, Leaf, Branch, Root) hang out together around one area
- The ocean terms (Coral, Shark, Whale, Water) cluster in their own spot nearby
- And then Habitat and Oxygen? They're sitting right in the middle, like they're connecting both groups

This makes sense when you think about it so it seemed we did it correct.

### Relations
The forest terms are all bunched up tight because they keep showing up in the same documents (1-4). Same story with the ocean terms in documents 7-10. It's validating to see that words with similar meanings are grouped naturally.

### The bridge terms
Habitat and Oxygen sit in the middle because they belong to both worlds. They show up in those transition documents (5-6) that mix forest and ocean content. The SVD recognised that these are shared ecological concepts.

### The documents mirror the terms perfectly
When you look at where the documents land:
- Forest docs (1-4) cluster together on one side
- Ocean docs (7-10) group up on the other
- Mixed docs (5-6) sit in between

## Did it work?
Yes, the SVD projection shows us that we can:
- Automatically separate different topics without labeling them first
- Distinguish between domain-specific terms and truly shared concepts
- Compress 10 dimensions down to just 2 while keeping the important relationships intact

The clustering makes intuitive sense, related terms behave as expected, and we even found some nice bridges between domains we might not have explicitly thought about.