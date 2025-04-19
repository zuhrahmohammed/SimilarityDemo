import os
from flask import Flask, render_template, request
from similarity_model import SimilarityModel

app = Flask(__name__, template_folder='templates')
model: SimilarityModel = SimilarityModel("ontology_descriptions.json")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    message = request.form.get("message", "")
    score = model.compare_text(message)
    return render_template("index.html", score=round(score, 4), message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)  
