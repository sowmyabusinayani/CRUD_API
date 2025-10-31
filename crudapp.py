from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for CRUD operations
Pandavas = [
    {"id": 1, "Name": "Yudistar", "Nickname": "Dharma Raju"},
    {"id": 2, "Name": "Bheema", "Nickname": "Vrikodara"},
    {"id": 3, "Name": "Arjuna", "Nickname": "Paartha"},
    {"id": 4, "Name": "Nakula", "Nickname": "Jayasena"},
    {"id": 5, "Name": "Sahadeva", "Nickname": "Asvineya"}
]


# Get all books
@app.route('/pandavas', methods=['GET'])
def get_Pandavas():
    return Pandavas


# Get a specific Pandav with Id
@app.route('/pandavas/<int:person_id>', methods=['GET'])
def get_pandav(person_id):
    for pandav in Pandavas:
        if (pandav['id'] == person_id):
            return pandav
    pandav_id = person_id
    return "Error:404 Pandava with Id ... is not found, try with another Id"


# Create a Pandav
@app.route('/pandavas/', methods=['POST'])
def create_pandav():
    new_Pandav = {"id": len(
        Pandavas)+1, 'Name': request.json['Name'], "Nickname": request.json["Nickname"]}
    Pandavas.append(new_Pandav)
    return new_Pandav


# Update a Pandav
@app.route('/pandavas/<int:person_id>', methods=['PUT'])
def update_pandav(person_id):
    for pandav in Pandavas:
        if (pandav['id'] == person_id):
            pandav['Name'] = request.json['Name']
            pandav['Nickname'] = request.json['Nickname']
            return pandav
    return "Error: Pandav with the specified id is not found"


# Delete a pandav
@app.route('/pandavas/<int:person_id>', methods=['DELETE'])
def delete_pandav(person_id):
    for pandav in Pandavas:
        if (pandav['id'] == person_id):
            Pandavas.remove(pandav)
            return "Pandav removed successfully"
    return "Error: Pandav with the specified id is not found"


# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
