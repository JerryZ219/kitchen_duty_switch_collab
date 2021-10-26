from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "blah_blah_blah"


@app.route("/")
def index():
	return render_template("index.html")

# @app.route("/very_cool")
# def very_cool():


if __name__ == "__main__":
	app.run()