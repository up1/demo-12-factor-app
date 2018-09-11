from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import os
import signal
import sys



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
   __tablename__ = 'USER'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100))

@app.route("/user")
def list_all_user():
   to_json = lambda user: {"id": user.id, "username": user.name}
   return json.dumps([to_json(user) for user in User.query.all()])

from flask import request

def shutdown_server(signal, frame):
    print('Got request to shutdown')
    # Doing Processes .....
    sys.exit(0)
 
if __name__ == "__main__":
   signal.signal(signal.SIGINT, shutdown_server)
   signal.signal(signal.SIGTERM, shutdown_server)
   
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)