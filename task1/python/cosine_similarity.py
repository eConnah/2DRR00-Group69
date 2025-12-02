import json

# Opening and reading the JSON file
with open('../rankings/glorija.json', 'r') as f:
    # Parsing the JSON file into a Python dictionary
    ranking_Glorija = json.load(f)


glorija_magnitude = 0

for i in range (4):
    glorija_magnitude += (list(ranking_Glorija["ranking"].values())[i])**2

glorija_magnitude = (glorija_magnitude)**0.5


def compute_cosine_similarity(person):

    with open('../rankings/' + person + '.json', 'r') as f:
        ranking_person = json.load(f)

    inner_product = 0
    for i in range (4):
        inner_product += list(ranking_person["ranking"].values())[i] * list(ranking_Glorija["ranking"].values())[i]
    

    person_magnitude = 0
    for i in range (4):
        person_magnitude += (list(ranking_person["ranking"].values())[i])**2
    person_magnitude = person_magnitude**0.5

    return ((inner_product) / (glorija_magnitude * person_magnitude))



persons = ['connor', 'ivan', 'lukas', 'maria', 'viktors']

for name in persons:
    print( name +  str(compute_cosine_similarity(name)))