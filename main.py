from flask import Flask, render_template, request
from src.elasticsearch_module import get_melodies, setup_database
import os


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    pattern = ""
    if request.method == "POST":
        pattern = request.form.get("pattern", "")
        if pattern:
            response = get_melodies(pattern)
            results = [
                {
                    "id": hit["_source"]["melody_id"],
                    "title": hit["_source"]["melody_title"],
                    "pattern": hit["_source"]["melody_pattern"],
                    "score": hit["_score"],
                }
                for hit in response["hits"]["hits"]
            ]
    return render_template("index.html", results=results, pattern=pattern)


@app.route("/setup_database", methods=["POST"])
def setup_database_route():
    setup_database()
    return ("", 204)


if __name__ == "__main__":
    app.run()
