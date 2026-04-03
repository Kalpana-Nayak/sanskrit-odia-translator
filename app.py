from flask import Flask, request, render_template
import json

app = Flask(__name__)

with open("dictionary.json", "r", encoding="utf-8") as f:
    dictionary = json.load(f)

def translate(text):
    words = text.split()
    result = []
    for word in words:
        word = word.replace("ः", "")
        result.append(dictionary.get(word, "[?]"))
    return " ".join(result)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        text = request.form["text"]
        output = translate(text)
    return render_template("index.html", output=output)

app.run(debug=True)