from flask import Flask, url_for, render_template, redirect
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired

from pprint import pprint
from json import load

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
prof = ['JavaScript developer <Junior>', 'Python developer <Middle>',
        "Data Science engineer", "Medical doctor"]
answers = {'title': 'Анкета',
           'surname': 'big',
           'name': 'bob',
           'education': 'highly school',
           'profession': 'QA engineer',
           'sex': 'male',
           'motivation': 'Always on top!',
           'ready': 'True'}
persons = ['Линус Торвальдс',
           'Сэр Тим Бернерс-Ли',
           'Джеймс Гослинг',
           'Андерс Хейлсберг',
           'Марк Цукерберг',
           'Брэм Коэн',
           'Брендан Айк',
           'Бьерн Страуструп',
           'Джон Кармак']


@app.route('/training/<prof>')
def proff(prof):
    return render_template('base.html', title=prof)


@app.route('/list_prof/<type>')
def list_prof(type):
    return render_template(f"{type}_prof_list.html", prof=prof)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('auto_answer.html', **answers)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', persons=persons)


@app.route('/member')
def member():
    with open('templates/members.json') as j:
        return render_template('member.html', members=load(j))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
