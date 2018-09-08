from flask import Flask
import pymysql.cursors
import json

app = Flask(__name__)

def list_user():
   all_users = execute_sql("SELECT * FROM USER") or []
   return [{"id": user_id, "username": username} for (user_id, username) in all_users]


def execute_sql(query):
   connection = None
   try:
       connection = pymysql.connect(host='localhost', 
                               user='user', 
                               password='password', 
                               db='demo')
       cursor = connection.cursor()
       cursor.execute(query)
       return cursor.fetchall()
   except pymysql.Error:
       print("Error %d: %s" % (e.args[0], e.args[1]))
       return None
   finally:
       if connection:
           connection.close()

@app.route("/user")
def list_all_user():
   return json.dumps(list_user())

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000)