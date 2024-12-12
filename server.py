from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/posts", methods=["GET"])
def posts():
    return """<h1>This is supposed to have posts here.</h1>\
<p><a href="/">Home page</a></p>"""


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html", title="Contact")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
