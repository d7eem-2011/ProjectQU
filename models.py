from flask import SQLALchemy

db = SQLALchemy()

class User(db.Model):
    """User model"""


    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=Ture)
    username = db.Column(db.String(25), unique=True, unllable=False)
    password = db.Column(db.String(), unllable=False)

    db.create_all()