# api/index.py
import json

# Load data once on cold start
with open("data.json", "r") as f:
    student_data = json.load(f)
    marks_map = {entry["name"]: entry["marks"] for entry in student_data}

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    if request.method == "OPTIONS":
        return response.status(200).send("")

    names = request.query.getlist("name")
    result = [marks_map.get(name, None) for name in names]

    return response.json({ "marks": result })
