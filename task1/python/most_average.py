import json
import math

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
    return abs(dotProduct(vectorA, vectorB)/(vectorMod(vectorA) * vectorMod(vectorB)))
    

averages = []

data = {}

names = ["connor", "glorija", "lukas", "ivan", "maria", "viktors" ]

averagessness = {}

for i in names:
    with open(f"task1/rankings/{i}.json") as f:
        data[i] = json.load(f)

for i in range(8):
    average = 0
    for j in names:
        average += list((data[j])["ranking"].values())[i]
    averages.append(average / 6)

for i in names:
    averagessness[i] = cosineSim(averages, list((data[i])["ranking"].values()))

print(averagessness)
