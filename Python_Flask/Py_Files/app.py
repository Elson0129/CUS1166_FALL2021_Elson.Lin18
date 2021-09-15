from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:course>")
def welcome(course):
    course = course.upper()
    return f"Welcome to {course}"

@app.route("/<string:course>/<int:size>/<int:color>")
def welcome_h(course,size, color):
    colors = ['red', 'green', 'blue','yellow','cyan', 'lime']
    return (f"<h{size} style='color:{colors[color]}'> Welcome to {course} <h{size}>")

if __name__ == '__main__':
    app.run()
