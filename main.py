import os
from flask import Flask, jsonify
import sqlalchemy
from google.cloud.sql.connector import IPTypes
from db import get_db_connection, connect_with_connector, get_IP_TYPE

app = Flask(__name__)

# Create the global connection pool when the application starts
pool = connect_with_connector()

@app.route("/")
def hello_world():
    """
    Simple health check route.
    
    Returns:
        str: Greeting message
    """
    return get_IP_TYPE()
    

@app.route("/get-time")
def get_time_controller():
    """
    Retrieves the current timestamp from the database.
    
    Returns:
        flask.Response: JSON response with current timestamp
    """
    try:
        with pool.connect() as db_conn:
            # Get current datetime from database
            result = db_conn.execute(sqlalchemy.text("SELECT NOW()")).fetchone()
            
            # Return the timestamp as JSON
            return jsonify({
                "current_time": str(result[0])
            })
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

@app.route("/users")
def get_users():
    """
    Retrieves all users from the database.
    
    Returns:
        flask.Response: JSON response with list of users
    """
    try:
        with pool.connect() as db_conn:
            # Fetch all users
            results = db_conn.execute(sqlalchemy.text("SELECT * FROM users"))
            print("Users : ", results)
            # Get column names
            column_names = results.keys()
            print("Column names:", column_names)
            
            # Convert results to list of dictionaries
            users = []
            for row in results:
                print("Raw row:", row)
                # Create a dictionary for each row using column names
                user_dict = {col: val for col, val in zip(column_names, row)}
                users.append(user_dict)
            
            return jsonify(users)
    except Exception as e:
        import traceback
        return jsonify({
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))