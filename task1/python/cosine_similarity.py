import json

def compute_cosine_similarity(person):
    with open('task1/rankings/' + person + '.json', 'r') as f:
        ranking_person = json.load(f)

    inner_product = 0
    for i in range (4):
        inner_product += list(ranking_person["ranking"].values())[i] * list(ranking_chosen["ranking"].values())[i]
    

    person_magnitude = 0
    for i in range (4):
        person_magnitude += (list(ranking_person["ranking"].values())[i])**2
    person_magnitude = person_magnitude**0.5

    return ((inner_product) / (chosen_magnitude * person_magnitude))


chosen_person = 'glorija'

# Opening and reading the JSON file
with open(f'task1/rankings/{chosen_person}.json', 'r') as f:
    # Parsing the JSON file into a Python dictionary
    ranking_chosen = json.load(f)

chosen_magnitude = 0

for i in range (4):
    chosen_magnitude += (list(ranking_chosen["ranking"].values())[i])**2

chosen_magnitude = (chosen_magnitude)**0.5

persons = ['connor', 'ivan', 'glorija', 'maria', 'viktors', 'lukas']
persons.remove(chosen_person)

similarities = {}

for name in persons:
    similarities[name] = compute_cosine_similarity(name)

print('Similarity from most to least:')
for i in sorted(similarities.values(), reverse=True):
    print(f'{list(similarities.keys())[list(similarities.values()).index(i)]}: {i}')