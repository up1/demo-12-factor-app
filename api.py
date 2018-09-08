from flask import Flask
import pymysql.cursors
import json
import os

DATABASE_CONFIGURATION = {
   'host': os.environ['DATABASE_HOST'],
   'user': os.environ['DATABASE_USER'],
   'password': os.environ['DATABASE_PASSWORD'],
   'db': os.environ['DATABASE_NAME']
}

def execute_sql(query):
   connection = None
   try:
       connection = pymysql.connect(**DATABASE_CONFIGURATION)
       cursor = connection.cursor()
       cursor.execute(query)
       return cursor.fetchall()
   except pymysql.Error:
       print("Error %d: %s" % (e.args[0], e.args[1]))
       return None
   finally:
       if connection:
           connection.close()

def list_user():
   all_users = execute_sql("SELECT * FROM USER") or []
   return [{"id": user_id, "username": username} for (user_id, username) in all_users]


app = Flask(__name__)

@app.route("/user")
def list_all_user():
   return json.dumps(list_user())

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000)