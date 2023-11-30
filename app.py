from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"
# debug = DebugToolbarExtension(app)

@app.route('/')
def questions():
    prompt = story.prompts
    return render_template("form.html", prompts = prompt)

@app.route('/story')
def generate_story():
    content = story.generate(request.args)
    return render_template("story.html", text = content)