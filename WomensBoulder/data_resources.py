from flask_restful import Resource
from flask import jsonify

class DataListResource(Resource):
    def __init__(self, data):
        self.data = data

    def get(self):
        return jsonify(self.data)


class DataResource(Resource):
    def __init__(self, data):
        self.data = data

    def filter_results(self, key, value):
        filtered_results = []
        for item in self.data:
            for result in item.get("results", []):
                if str(result.get(key, "")).lower() == str(value).lower():
                    item_copy = item.copy()
                    item_copy["results"] = [result]
                    filtered_results.append(item_copy)
                    break
        return filtered_results

    def get(self, **kwargs):
        filters = {
            "id": lambda x: next((item for item in self.data if item["id"] == x), None),
            "competition": lambda x: [item for item in self.data if x.lower() in item["competition"].lower()],
            "city": lambda x: [item for item in self.data if x.lower() in item["city"].lower()],
            "year": lambda x: [item for item in self.data if item["year"] == x],
            "dates": lambda x: [item for item in self.data if x.lower() in item["dates"].lower()],
            "rank": lambda x: self.filter_results("Rank", str(x)),
            "name": lambda x: self.filter_results("Name", x),
            "surname": lambda x: self.filter_results("Surname", x),
            "country": lambda x: self.filter_results("Country", x),
        }

        for key, value in kwargs.items():
            if key in filters:
                result = filters[key](value)
                if result:
                    return jsonify(result)

        return {"message": "Data not found"}, 404
