from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# ---------- MySQL Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # change if needed
        password="",       # your MySQL password
        database="press2debug"
    )

# ---------- ROUTES ----------

# 1️⃣ Create a new user
@app.route('/api/users/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                   (username, password))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User created successfully"}), 201


# 2️⃣ Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT user_id, username, email FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users), 200


# 3️⃣ Get a single user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT user_id, username, email, password FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# update user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    fields = []
    values = []

    # Only update what’s provided
    if "username" in data:
        fields.append("username = %s")
        values.append(data["username"])
    if "email" in data:
        fields.append("email = %s")
        values.append(data["email"])
    if "password" in data:
        fields.append("password = %s")
        values.append(data["password"])

    if not fields:
        return jsonify({"error": "No fields provided to update"}), 400

    query = f"UPDATE users SET {', '.join(fields)} WHERE user_id = %s"
    values.append(user_id)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, tuple(values))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User updated successfully"}), 200


# 5️⃣ Delete a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User deleted successfully"}), 200

@app.route('/api/users/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    # user
    # "user_id": "1"
    # "email": "therealhussainali@gmail.com"
    # "password:": "1234"


    if user and user['password'] == password:
        return jsonify({"message": "Login successful", "user_id": user["user_id"]}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/users/signup', methods=['POST'])
def signup_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Check if username or email already exists
    cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
    existing_user = cursor.fetchone()
    if existing_user:
        cursor.close()
        conn.close()
        return jsonify({"error": "Username or email already exists"}), 409

    # Insert new user
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
        (username, email, password)
    )
    conn.commit()
    user_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify({
        "message": "User registered successfully",
        "user_id": user_id
    }), 201


@app.route('/api/users/todo', methods=['POST'])
def add_todo():
    data = request.get_json()

    username = data.get('username')
    todo = data.get('todo')

    if not all([username, todo]):
        return jsonify({"error": "Missing required fields"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Find user_id first
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    cursor.execute(
        "INSERT INTO todolist (user_id, todo_text) VALUES (%s, %s)",
        (user["user_id"], todo)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Added todo successfully"}), 200

@app.route('/api/users/<username>/todos', methods=['GET'])
def get_todos_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Find user_id first
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return jsonify({"error": "User not found"}), 404

    # Get todos for that user_id
    cursor.execute("SELECT todo_text FROM todolist WHERE user_id = %s", (user["user_id"],))
    todos = [row["todo_text"] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return jsonify({"username": username, "todos": todos}), 200


if __name__ == '__main__':
    app.run(debug=True)



