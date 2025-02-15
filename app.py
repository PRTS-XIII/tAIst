from flask import Flask, request, jsonify

app = Flask(__name__)

# A basic, curated dataset mapping ingredients to sensory characteristics.
ingredient_data = {
    "vanilla": {
        "taste": "sweet, creamy",
        "smell": "warm, comforting vanilla aroma",
        "sight": "rich, dark extracts",
        "touch": "smooth, slightly oily",
        "hearing": "none"
    },
    "lemon": {
        "taste": "sour, tangy",
        "smell": "bright citrus",
        "sight": "vivid yellow",
        "touch": "rough, textured peel",
        "hearing": "none"
    }
}

@app.route('/ingredient', methods=['GET'])
def get_ingredient_info():
    # Expecting a query parameter, e.g. /ingredient?name=vanilla
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide an ingredient name."}), 400
    
    # Retrieve data using a simple, case-insensitive lookup.
    data = ingredient_data.get(name.lower())
    if not data:
        return jsonify({"error": "Ingredient not found."}), 404

    return jsonify({"ingredient": name, "sensory_data": data})

if __name__ == '__main__':
    # Running the app in debug mode for development purposes.
    app.run(debug=True)
