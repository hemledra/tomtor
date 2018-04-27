from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('vyruby.html')

@app.route("/vyruby")
def vyruby():
    return render_template('vyruby.html')

@app.route("/stavby")
def stavby():
    return render_template('stavby.html')

@app.route("/projekt")
def index3():
    return render_template('projekt.html')

if __name__ == "__main__":
    app.run()
