
# Flask API with MySQL Database

This is a simple Flask API that interacts with a MySQL database for managing users. It provides basic CRUD (Create, Read, Update, Delete) operations to perform operations on user data.

## Prerequisites

- Python 3.10.0+
- Flask library
- MySQL database

## Installation and setup

1. Clone the repository.
2. Change to the project directory.
3. Install the required dependencies.
4. create a database in MySQL with any name , create a table with name *"users"* with 3 columns *"id"* as primary key ,*"name"* and  *"age"*.
5. Update the MySQL database connection details in the `config.py` file or declare them by using `ENVIRONMENT VARIABLES`. 

## usage

1. Run the flask API server. with `APP_FLASK=app.py flask run` if you are running in your local machine.   
2. The Flask app will start running at `http://127.0.0.1:5000/` by default.
3. You can use an API client (such as curl or Postman) to send HTTP requests to the API endpoints for testing the CRUD operations on user data.

## API Endpoints

- `GET /users`: Get all users.
- `GET /users/<user_id>`: Get a specific user by ID.
- `POST /users`: Create a new user.
- `PUT /users/<user_id>`: Update an existing user by ID.
- `DELETE /users/<user_id>`: Delete a user by ID.

## Examples
 1. Create a new user:
 `POST http://127.0.0.1:5000/users`
 `Content-Type: application/json`

`{
  "id": 1,
  "name": "Deepak",
  "age": 22
}`


 2. Get all users:
 `GET http://127.0.0.1:5000/users`
 
 3. Get a specific user by ID:
 `GET http://127.0.0.1:5000/users/1`
 
 4. Update an existing user by ID:
`PUT http://127.0.0.1:5000/users/1`
`Content-Type: application/json`

`{
  "id": 1
  "name": "Deepak Puri",
  "age": 23
}`

 
 5. Delete a user by ID:
 `DELETE http://127.0.0.1:5000/users/1`







