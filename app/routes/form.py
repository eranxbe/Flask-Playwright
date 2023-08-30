from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from ..forms.simple_form import NamerForm, UserForm, TraderFormAPI

form = Blueprint('form', __name__, url_prefix='/form')
    

@form.route('/')
def index():
    return render_template('home_page.html')

@form.route('/hello', methods=['GET', 'POST'])
def say_hello():
    name = None
    form = NamerForm()
    if request.method == 'POST':
        name = request.form['name']
        return render_template('get_name_form.html', form=form, name=name)
    else:
        return render_template('get_name_form.html', form=form)

@form.route('/fill-tha-form', methods=['GET', 'POST'])
def get_form():
    form = UserForm()
    if form.validate_on_submit():
        data = {
            'name' : request.form['name'],
            'email' : request.form['email'],
            'age' : request.form['age'],
            'gender' : request.form['gender'],
            'interests' : request.form['interests'],
            'country' : request.form['country'],
            'comment' : request.form['comment']
        }
        
        return redirect('form.after_submit', Response=['POST'], data=data)
    return render_template('form.html', form=form)

@form.route('/after-submit', methods=['GET', 'POST'])
def after_submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        print(f'User {data.get("name")} aged {data.get("age")}, {data.get("gender")} from {data.get("country")} was Submitted!')
    return render_template('after_submit.html')