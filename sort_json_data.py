import json


def sort_json(data):
    output_data = []
    parent_ids = []
    for category in data:
        if not category["parent_id"]:
            parent_ids.insert(0, category["parent_id"])
        else:
            parent_ids.append(category["parent_id"])
    for parent_id in parent_ids:
        for category in data:
            if category["parent_id"] == parent_id:
                output_data.append(category)
    print(output_data)


"Data from class variable"
input_data='[{"name": "Accessories","id": 1,"parent_id": 20},{"name": "Watches","id": 57,"parent_id": 1},{"name": "Men","id": 20,"parent_id": null}]'
data = json.loads(input_data)  # Uncomment it if you want to take data from constant/class variable.

"Data from file"
f = open("input_data.json", )
data = json.load(f)
f.close()

sort_json(data)
