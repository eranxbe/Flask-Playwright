from flask import Blueprint, request, jsonify
from sqlalchemy import select
from ..extensions import db
from ..models.model_person import Person
from flask_restful import Resource, Api, abort, reqparse

 
rest = Blueprint('rest', __name__, url_prefix="/rest")
api = Api(rest)

## using flask_restful

class Hello(Resource):
    def get(self):
        return {'message' : 'Hello World!'}
    
api.add_resource(Hello, '/hello-restful')    

class People(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('_id', type=int)
        self.parser.add_argument('name')
        self.parser.add_argument('age', type=int)
        self.parser.add_argument('gender')

    def get(self, id_or_name=None):
        person = None
        if id_or_name.isdigit():
            person = Person.query.filter_by(_id=int(id_or_name)).first()
        else:
            person = Person.query.filter_by(name=id_or_name).first()

        if not person:
            return {'message': f'Person with id or name {id_or_name} not found',
                    'status': 404}
        
        person_data =  {"id" : person._id,
                        "name": person.name,
                        "age": person.age,
                        "gender": person.gender}

        return {"person": person_data,
                'status': 200}
    
    def post(self):
        args = self.parser.parse_args()
        new_person = Person(name=args['name'], age=args['age'], gender=args['gender'])
        db.session.add(new_person)
        db.session.commit()
        return {"message": f"Person {args['name']} was added successfully",
                'status': 201}
    
    def put(self, id_or_name=None):
        args = self.parser.parse_args()
        person = None
        if id_or_name.isdigit():
            person = Person.query.filter_by(_id=int(id_or_name)).first()
        else:
            person = Person.query.filter_by(name=id_or_name).first()

        if not person:
            return {'message': f'Person with id {id} not found', 'status': 404}

        if args['name'] is not None:
            person.name = args['name']
        if args['age'] is not None:
            person.age = args['age']
        if args['gender'] is not None:
            person.gender = args['gender']

        db.session.commit()

        return {'message': f'Person with id or name{id_or_name} was updated successfully', 'status': 200}

    def delete(self, id_or_name):
        person = None
        if id_or_name.isdigit():
            person = Person.query.filter_by(_id=int(id_or_name)).first()
        else:
            person = Person.query.filter_by(name=id_or_name).first()

        if not person:
            return {'message': f'Person with id or name {id_or_name} not found', 'status': 404}

        db.session.delete(person)
        db.session.commit()
        return {'message': f'Person with id or name {id_or_name} was deleted successfully',
                'status': 202}
    
api.add_resource(People, '/restful_person/<string:id_or_name>', 
                         '/restful_new_person')

'''
curl commands that work
curl -X GET "127.0.0.1:5000/rest/restful_person/<id_or_name>"
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"name\", \"age\": age, \"gender\": \"male\"}" "127.0.0.1:5000/rest/restful_new_person"
curl -X PUT -H "Content-Type: application/json" -d "{\"name\": \"newname\", \"age\": newage, \"gender\": \"newgender\"}" "127.0.0.1:5000/rest/restful_person/<id_or_name>"
curl -X DELETE "127.0.0.1:5000/rest/restful_person/<id_or_name>"
'''
