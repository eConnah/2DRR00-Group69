import json

def dotProduct(vectorA, vectorB):
    dotProd = 0
    for a,b in zip(vectorA, vectorB):
        dotProd += a * b
    return dotProd

def vectorMod(vector):
    vectorMod = 0
    for i in vector:
        vectorMod += i**2
    return vectorMod ** 0.5

def cosineSim(vectorA, vectorB):
    return (dotProduct(vectorA, vectorB)/(vectorMod(vectorA) * vectorMod(vectorB)))
    

with open(f"task1/predictions.json") as f:
    content = json.load(f)
    actual = content['actual']
    data = content['people']

correctness = {}

for i in range (5):
    correctness[i + 1] = cosineSim(actual.values(), data[i].values())

print('Predictions accuracy from most to least:')
for i in sorted(correctness.values(), reverse=True):
    print(f'{list(correctness.keys())[list(correctness.values()).index(i)]}: {i}')