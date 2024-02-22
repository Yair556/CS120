from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return f'Hello, {name}!'
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)