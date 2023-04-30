from flask import Blueprint, request, render_template
# from .rest import people
import json

form = Blueprint('form', __name__)



@form.route('/form', methods=['GET', 'POST'])
def get_form():
    if request.method == 'GET':
        return render_template('form.html')
    
# I will work on this soon
# 
#     elif request.method == 'POST':
#         print(request.form)
#         name = request.form.get('name')
#         email = request.form.get('email')
#         age = request.form.get('age')
#         gender = request.form.get('gender')
#         interests = request.form.getlist('interests')
#         country = request.form.get('country')
#         comments = request.form.get('comments')
#         p_id = max([p['id'] for p in people]) + 1
#         new_person = {
#         'id': p_id,
#         'name': name,
#         'age': int(age),
#         'gender': gender
#         }
#     people.append(new_person)
#     with open("people.json", "w") as f:
#         json.dump({'people': people}, f)

#     return render_template('after-form.html')