from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/principal')
def principal():
    return render_template('principal.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run()


""" app.run(debug=True) """