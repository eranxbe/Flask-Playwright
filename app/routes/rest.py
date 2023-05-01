from flask import Blueprint, request, jsonify
from sqlalchemy import select
from ..extensions import db
from ..models.model_person import Person

 
rest = Blueprint('rest', __name__, url_prefix="/rest")


@rest.before_request
def parse_urlencoded_data():
    if request.content_type == 'application/x-www-form-urlencoded':
        data = request.form.to_dict()
        request.parsed_data = data

@rest.route('/hello')
def index():
    return {"message": "hello!"}, 200

@rest.route('/person/<name>', methods=['GET'])
def get_person_by_name(name: str):
    person = Person.query.filter_by(name=name).first()
    if not person:
        return jsonify({"message": "Person not found", "status": 404}), 404
    person_data =  {"id" : person._id,
        "name": person.name,
        "age": person.age,
        "gender": person.gender}
    return jsonify(person_data), 200

@rest.route('/get-all', methods=['GET'])
def get_all():
    found_persons_objects = Person.query.all()
    found_persons = []
    for person in found_persons_objects:
        person_data = {
            "id" : person._id,
            "name" : person.name,
            "age" : person.age,
            "gender" : person.gender
        }
        found_persons.append(person_data)
    return jsonify(found_persons), 200
        

# I will work on this soon
#
# @rest.route("/search", methods=["GET"])
# def search_person():
#     name = request.args.get('name')
#     age = request.args.get('age', type=int)

#     people_age = [p for p in people if p['age'] == age]

#     if name is None:
#         if age is None:
#             return jsonify(people)
#         else:
#             return jsonify(people_age)
#     else:
#         people_name = [p for p in people if name.lower() in p['name'].lower()]
#         if age is None:
#             return jsonify(people_name)
#         else:
#             combined = [p for p in people_age if p in people_name] 
#             return jsonify(combined)


@rest.route("/add-person", methods=["POST"])
def add_person():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    new_person = Person(name=name, age=age, gender=gender)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"message" : f"Person {name} was added!"}), 201



# I will work on this soon
#
# @rest.route("/change-person", methods=["PUT"])
# def change_person():
#     data = request.parsed_data
#     person = Person(**data)
#     new_person = {
#         'id': person.id,
#         'name': person.name,
#         'age': person.age,
#         'gender': person.gender
#     }
#     person_list = [p for p in people if p['id'] == person.id]
#     if len(person_list) > 0:
#         people.remove(person_list[0])
#         people.append(new_person)
#         with open("people.json", "w") as f:
#             json.dump({'people': people}, f)
#         return jsonify(new_person), 204
#     else:
#         return jsonify({'error': 'Person not found'}), 404

@rest.route("/delete-person", methods=["DELETE"])
def delete_person():
    data = request.json
    name = data.get('name')
    person = Person.query.filter_by(name=name).first()
    if not person:
        return jsonify({"message": "Person not found", "status": 404}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify(f"person {person.name} with id {person._id} deleted"), 202
