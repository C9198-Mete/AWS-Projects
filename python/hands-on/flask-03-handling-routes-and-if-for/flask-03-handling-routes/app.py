from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "This is home page for no path, <h1> Welcome Home</h1>"

@app.route("/about")
def about():
    return "<h1>This is my about page</h1>"

@app.route("/error")
def error():
    return "<h1>This is ERROR page</h1>"

@app.route("/hello")
def hello():
    return "<h1>Hello, World!</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("error"))




if __name__== "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)
    