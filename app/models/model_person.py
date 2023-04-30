from ..extensions import db

class Person(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age =  db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(6))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender