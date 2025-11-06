from flask import Flask, request, jsonify

app = Flask(__name__)

# Example endpoint that receives and returns JSON
@app.route('/api/add', methods=['POST'])
def add_numbers():
    # Get JSON data from request body
    data = request.get_json()
    
    # Extract values
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    # Perform operation
    if num1 is None or num2 is None:
        return jsonify({"error": "num1 and num2 required"}), 400
    
    result = num1 + num2
    
    # Return JSON response
    return jsonify({
        "result": result
    }), 200


@app.route('/api/hello', methods=['GET'])
def helo():
    
    # Return JSON response
    return jsonify({
        "result": "Hello World"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
