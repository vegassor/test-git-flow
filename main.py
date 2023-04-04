import json

data = {
    'sun': 1,
    'mon': 2,
    'tue': 3,
    'wed': 4,
    'thu': 5,
    'fri': 6,
}

print("JSON:")
print(json.dumps(data, indent=2))
