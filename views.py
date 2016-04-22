from flask import jsonify
from module1 import app
from pymongo import MongoClient
from flask import render_template


dbclient= MongoClient()
db = dbclient.test

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def get_student_data():
    result = db.mcq.insert_one({
            "instruction": "do it",
            "text": "This is a question",
            "group_id": 1,
            "image": [],
            "options": {
                "a": {
                    "text": "Option A",
                    "image": []
                },
                "b": "Option B",
                "c": "Option C",
                "d": "Option D"
            },
            "answers": ["a", "b"],
            "explanation": {
                "text": "Option A",
                "image": []
            },
            "subject": "Maths",
            "topics": {
                "Geometry": "Triangles",
                "Probability": "Basic Probability"
            },
            "exams": {
                "exam": "UPSC",
                "scoring": {
                    "positive": "",
                    "negative": ""
                },
                "level": 1
            },
            "resources": {
                "notes": "",
                "formulae": "" ,
                "videos": ""
            }
        }

    )

    q = db.mcq.find()
    for ques in q:
        print(ques["options"])

    return jsonify(result)
