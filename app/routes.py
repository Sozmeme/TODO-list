from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    tasks = [
        {"task": "With Flask develop TODO-lsit", "deadline": "inf"},
        {"task": "Patch TODO-list when it's done", "deadline": "inf + inf"}
    ]
    return render_template('index.html', tasks=tasks)
    