from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB connection
# Update these settings with your MongoDB credentials
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
DB_NAME = os.environ.get('MONGO_DB', 'search_db')
COLLECTION_NAME = os.environ.get('MONGO_COLLECTION', 'search_data')

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.json
        query = data.get('query', '')
        
        if not query:
            return jsonify({'results': [], 'message': 'Query is empty'}), 400
        
        # Create a text search query
        # You can customize this query based on your MongoDB schema
        results = list(collection.find(
            {'$text': {'$search': query}},
            {'score': {'$meta': 'textScore'}}
        ).sort([('score', {'$meta': 'textScore'})]).limit(20))
        
        # Convert ObjectId to string for JSON serialization
        for result in results:
            if '_id' in result:
                result['_id'] = str(result['_id'])
        
        return jsonify({'results': results})
    
    except Exception as e:
        print(f"Error during search: {e}")
        return jsonify({'error': str(e)}), 500

# For testing purposes - add sample data
@app.route('/add_sample_data', methods=['POST'])
def add_sample_data():
    try:
        sample_data = [
            {"title": "MongoDB Tutorial", "description": "Learn how to use MongoDB with Python"},
            {"title": "React Search Component", "description": "Building a search bar in React"},
            {"title": "Flask API Development", "description": "Creating REST APIs with Flask"},
            {"title": "Database Indexing", "description": "Optimize your MongoDB queries with proper indexing"},
            {"title": "Full-Stack Development", "description": "Connecting React frontend with Python backend"}
        ]
        
        # Create text index if it doesn't exist
        collection.create_index([("title", "text"), ("description", "text")])
        
        # Insert sample data
        result = collection.insert_many(sample_data)
        return jsonify({"message": f"Added {len(result.inserted_ids)} sample documents"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)