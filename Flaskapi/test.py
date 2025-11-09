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
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                   (username, email, password))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User created successfully"}), 201


# 2️⃣ Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT idusers, username, email FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users), 200


# 3️⃣ Get a single user by ID
@app.route('/api/users/<int:idusers>', methods=['GET'])
def get_user(idusers):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT idusers, username, email, password FROM users WHERE idusers = %s", (idusers,))
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
@app.route('/api/users/<int:idusers>', methods=['DELETE'])
def delete_user(idusers):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE idusers = %s", (idusers,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
