import json

prediction = [0, 0, 0, 0]

persons = ["ivan", 'viktors' , 'maria', 'lukas', 'connor' ]

def compute_cosine_similarity():

    for name in persons: 
        with open('task1/rankings/' + name + '.json', 'r') as f:
            ranking_person = json.load(f)

        for i in range (4, 8):
            prediction[i - 4] += (list(ranking_person["ranking"].values())[i])

    for i in range (4, 8):
        prediction[i - 4] /= len(persons)

    return prediction
    

print("predicted score: " + str(compute_cosine_similarity()))