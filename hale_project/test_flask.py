from flask import Flask,escape,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/main')
def home():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)
