import pymysql
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = pymysql.connect(
            host='db',
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_ROOT_PASSWORD'),
            database='users'
        )
        conn.close()
        db_status = "Connected to the database successfully."
    except Exception as e:
        db_status = f"Error while connecting to the database: {e}"

    return render_template('index.html', db_status=db_status)

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5050, debug=debug_mode) # nosec B104