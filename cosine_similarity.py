import json

# Opening and reading the JSON file
with open('ranking_Glorija.json', 'r') as f:
    # Parsing the JSON file into a Python dictionary
    ranking_Glorija = json.load(f)

def compute_cosine_similarity(person):

    with open('ranking_' + person + '.json', 'r') as f:
        ranking_person = json.load(f)

    inner_product = 0

    for i in range (3):
        inner_product += ranking_Glorija["ranking"][i]
    
    for i in ranking_Glorija["ranking"]:
        