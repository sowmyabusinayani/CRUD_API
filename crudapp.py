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


@app.route('/Pandavas', methods=['GET'])
def get_Pandavas():
    return Pandavas


# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
