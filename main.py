from flask import Flask
import json


app = Flask(__name__)


@app.route("/")
def index_page():
    return "Student API Test for Graduation Project 2022-2023"


@app.route("/students", methods=["GET"])
def get_all_student():
    with open(file="students_data.json", mode="r") as students_file:
        return json.load(students_file)


@app.route("/students/<student_number>", methods=["GET"])
def get_student(student_number):
    return get_all_student()[student_number]


if __name__ == "__main__":
    # If you want your web server to run locally on your computer, use this:
    app.run(host="192.168.1.9", port="7878", debug=True)
