"""
Author: Kanak Sachan
Date: 2024-05-18
Copyright (c) 2024 Kanak Sachan
Description: A basic Flask application with sample API endpoints.
"""

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
# the minimal Flask application

# Sample data to simulate a database
sample_data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
]

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route to get all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(sample_data)

# API route to get a single item by id
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in sample_data if item["id"] == item_id), None)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# API route to create a new item
@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item["id"] = len(sample_data) + 1
    sample_data.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
