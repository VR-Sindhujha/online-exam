
from flask import Flask, jsonify

app = Flask(__name__)

questions = [
    {
        "id": 1,
        "question": "Which language runs on the JVM?",
        "options": ["Python", "Java", "C", "JavaScript"],
        "answer": "Java"
    },
    {
        "id": 2,
        "question": "Which data structure uses FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },
    {
        "id": 3,
        "question": "Which SQL command retrieves data?",
        "options": ["INSERT", "DELETE", "SELECT", "UPDATE"],
        "answer": "SELECT"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Online Exam System",
        "version": "v1"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/quiz")
def quiz():
    # Do not reveal answers to students
    public_questions = [
        {
            "id": q["id"],
            "question": q["question"],
            "options": q["options"]
        }
        for q in questions
    ]

    return jsonify(public_questions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
