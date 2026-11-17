
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    roll = request.form.get("roll")

    subjects = {
        "English": int(request.form.get("english")),
        "Mathematics": int(request.form.get("maths")),
        "Physics": int(request.form.get("physics")),
        "Chemistry": int(request.form.get("chemistry")),
        "Computer Science": int(request.form.get("computer"))
    }

    total = sum(subjects.values())
    percentage = total / 5

    student = {
        "name": name,
        "roll": roll,
        "subjects": subjects,
        "total": total,
        "percentage": percentage
    }

    students = load_students()
    students.append(student)
    save_students(students)

    marks_html = ""
    for subject, marks in subjects.items():
        marks_html += f"<p>{subject}: {marks}</p>"

    return f"""
    <h1>Student Marksheet</h1>
    <p>Student Name: {name}</p>
    <p>Roll Number: {roll}</p>
    {marks_html}
    <h3>Total Marks: {total}/500</h3>
    <h3>Percentage: {percentage}%</h3>
    <a href="/">Go Back</a>
    <br><br>
    <a href="/students">View All Records</a>
    """

@app.route("/students")
def students():
    records = load_students()

    result = "<h1>All Student Records</h1>"

    for s in records:
        result += f"""
        <hr>
        <h3>{s['name']} (Roll: {s['roll']})</h3>
        <p>Total: {s['total']}/500</p>
        <p>Percentage: {s['percentage']}%</p>
        """

    result += '<br><a href="/">Go Back</a>'
    return result

@app.route("/test")
def test():
    return "Flask is working!"

if __name__ == "__main__":
    app.run(debug=True)
