import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from config import Config
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route("/add_course",methods=["POST"])
def add_course():
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")

    course = Course(course_number=course_number, course_title=course_title)
    db.session.add(course)
    db.session.commit()

    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route("/register_student/<int:course_id>",methods=["GET", "POST"])
def register_student(course_id):
    course = Course.query.get(course_id)

    if request.method == 'POST':
        name = request.form.get("name")
        grade = request.form.get("grade")
        course.reg_student(name,grade)

    registered_students = course.registered_students
    return render_template("course_details.html", course=course, registered_students=registered_students)

def main():
    if(len(sys.argv)==2):
        print(sys.argv)
        if sys.argv[1] == 'createdb':
            db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'python app.py createdb'")

if __name__ == "__main__":
    with app.app_context():
        main()
