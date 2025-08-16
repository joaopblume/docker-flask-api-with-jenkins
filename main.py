from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/names", methods=["GET", "POST"])
def names():
    """
    {
        "id": 1,
        "name": "John Doe"
    }
    """
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")
        if not name:
            return {"error": "Names is required"}, 400
        id = data.get("id")
        if not id:
            return {"error": "ID is required"}, 400
        with open("names.txt", "w") as f:
            f.write(f"{id} - {name}")
            return {"id": id, "name": name}
    else:
        with open("names.txt", "r") as f:
            lines = f.readlines()
            names = []
            for line in lines:
                id, name = line.strip().split(" - ")
                names.append({"id": id, "name": name})
            return {"names": names}, 200
        
@app.route('/name/<int:name_id>')
def name(name_id):
    with open("names.txt", "r") as f:
        lines = f.readlines()
        names = []
        for line in lines:
            id, name = line.strip().split(" - ")
            if int(id) == name_id:
                names.append({"id": id, "name": name})
                return {"names": names}, 200
        if not names:
            return {"error": "ID not found"}, 400