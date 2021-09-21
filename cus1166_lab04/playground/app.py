from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    roster = [
    ("Adam","B","Sophomore"), ("Angela", "B", "Junior"),
    ("Bobby", "C", "Freshman"), ("Brigette", "A", "Sophomore"),
    ("Dexter", "A", "Senior"), ("Irene", "B", "Sophomore"),
    ("Jesse", "D", "Senior"), ("Amari", "A", "Junior"),
    ("Emmet", "B", "Freshman"), ("Phillipe", "C", "Junior")]
    return render_template("roster.html", roster=roster, grade_view=grade_view)


if __name__ == '__main__':
    app.run()
