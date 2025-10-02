import pickle
import json

data = {'name' : 'Arun', 'age' : 22}
with open("data.pkl", 'wb') as f:
    pickle.dump(data, f)
    
with open("data.json", 'w') as f:
    json.dump(data, f)

with open("data.pkl", 'rb') as f:
    loaded = pickle.load(f)
    print(loaded)
    
with open("data.json", 'r') as f:
    loaded = json.load(f)
    print(loaded)