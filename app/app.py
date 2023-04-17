from flask import Flask, render_template, request, jsonify
from pydantic import BaseModel
from typing import Optional
import json

app = Flask(__name__)

class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

with open("people.json", "r") as f:
    people = json.load(f)['people']

@app.before_request
def parse_urlencoded_data():
    if request.content_type == 'application/x-www-form-urlencoded':
        data = request.form.to_dict()
        request.parsed_data = data

@app.route("/person/<int:p_id>", methods=["GET"])
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    return jsonify(person[0]) if len(person) > 0 else {}

@app.route("/search", methods=["GET"])
def search_person():
    name = request.args.get('name')
    age = request.args.get('age', type=int)

    people_age = [p for p in people if p['age'] == age]

    if name is None:
        if age is None:
            return jsonify(people)
        else:
            return jsonify(people_age)
    else:
        people_name = [p for p in people if name.lower() in p['name'].lower()]
        if age is None:
            return jsonify(people_name)
        else:
            combined = [p for p in people_age if p in people_name] 
            return jsonify(combined)


@app.route("/add-person", methods=["POST"])
def add_person():
    data = request.args
    print(data)
    person = Person(**data)
    p_id = max([p['id'] for p in people]) + 1
    new_person = {
        'id': p_id,
        'name': person.name,
        'age': person.age,
        'gender': person.gender
    }
    people.append(new_person)
    with open("people.json", "w") as f:
        json.dump({'people': people}, f)

    return jsonify(new_person), 201

@app.route("/change-person", methods=["PUT"])
def change_person():
    data = request.parsed_data
    person = Person(**data)
    new_person = {
        'id': person.id,
        'name': person.name,
        'age': person.age,
        'gender': person.gender
    }
    person_list = [p for p in people if p['id'] == person.id]
    if len(person_list) > 0:
        people.remove(person_list[0])
        people.append(new_person)
        with open("people.json", "w") as f:
            json.dump({'people': people}, f)
        return jsonify(new_person), 204
    else:
        return jsonify({'error': 'Person not found'}), 404

@app.route("/delete-person/<int:p_id>", methods=["DELETE"])
def delete_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    if len(person) > 0:
        people.remove(person[0])
        with open("people.json", "w") as f:
            json.dump({'people': people}, f)
        return '', 204
    else:
        return jsonify({'error': 'Person not found'}), 404


@app.route('/form', methods=['GET', 'POST'])
def get_form():
    if request.method == 'GET':
        return render_template('form.html')
    
    elif request.method == 'POST':
        print(request.form)
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        gender = request.form.get('gender')
        interests = request.form.getlist('interests')
        country = request.form.get('country')
        comments = request.form.get('comments')
        p_id = max([p['id'] for p in people]) + 1
        new_person = {
        'id': p_id,
        'name': name,
        'age': int(age),
        'gender': gender
        }
    people.append(new_person)
    with open("people.json", "w") as f:
        json.dump({'people': people}, f)

    return render_template('after-form.html')


if __name__ == '__main__':
    app.run(debug=True)
