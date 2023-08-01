#importing necessary packages
from flask import Flask, request, jsonify
import mysql.connector
import config
import os

# Create MySQL connection
mydb = mysql.connector.connect(
  host=config.DATABASE_HOST,
  user=config.DATABASE_USER,
  password=config.DATABASE_PASSWORD,
  database=config.DATABASE_DB_NAME
)

# Create Flask app
app = Flask(__name__)

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return jsonify(users)

# Endpoint to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id =  data.get('id')
    name = data.get('name')
    age = data.get('age')
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO users (id, name, age) VALUES (%s, %s, %s)", (user_id, name, age))
    mydb.commit()
    cursor.close()
    return jsonify({"message": "User created successfully"}), 201

# Endpoint to update an existing user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        cursor.execute("UPDATE users SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
        mydb.commit()
        cursor.close()
        return jsonify({"message": "User updated successfully"}) 
    else:
        return jsonify({"message": "User doesn't exist"}), 404

# Endpoint to delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        mydb.commit()
        cursor.close()
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"message": "user doesn't exist"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

