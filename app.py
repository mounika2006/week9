from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1><center>Hello World!!</center></h1>
    <a href="/register"><center>Go to Register Page</center></a>
    """

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    year = request.form["year"]

    return render_template("success.html", name=name, year=year)

if __name__ == "__main__":
    app.run(debug=True)