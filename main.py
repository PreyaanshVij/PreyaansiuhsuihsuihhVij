from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template')

correct_username = "Preyaansh Vij"
correct_password = "BT23GCS168"

@app.route('/')
def login():
    return render_template('new_login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    password = request.form['password']

    if username == correct_username and password == correct_password:
        return redirect(url_for('dashboard_page'))
    else:
        return "Login failed. Please check your username and password."

@app.route('/dashboard_page')
def dashboard_page():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
