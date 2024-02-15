from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dog')
def dog():
    return render_template('dog.html')

@app.route('/cat')
def cat():
    return render_template('cat.html')

@app.route('/calculator', methods=['POST', 'GET'])
def calculator():
    if request.method == 'POST':
        print("POST request received!")
        print(f"Form data: {request.form}")
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
        return render_template('calculator.html', result=result)
    
    elif request.method == 'GET':
        return render_template('calculator.html')


if __name__ == '__main__':
    app.run(debug=True)

