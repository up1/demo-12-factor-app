from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import os

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

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000)