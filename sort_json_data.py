import json


def sort_json(data):
    output_data = []
    category_ids = [category["id"] for category in data if not category["parent_id"]]
    output_data = [category for category in data if not category["parent_id"]]
    while len(category_ids) < len(data):
        for category in data:
            if category["parent_id"] in category_ids and category["id"] not in category_ids:
                category_ids.append(category["id"])
                output_data.append(category)
    return output_data


"Data from file"
f = open("input_data.json", )
data = json.load(f)
f.close()

result = sort_json(data)
