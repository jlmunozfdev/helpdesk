from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def index():
    return render_template('login.html')


@app.route("/principal")
def principal():
    return render_template('principal.html')

@app.route("/component")
def component():
    return render_template('component.html')



if __name__ == '__main__':
    app.run()


""" app.run(debug=True) """