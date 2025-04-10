from flask import render_template, request, redirect, url_for
from my_application import app

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        a = float(request.form.get('a', 0))
        b = float(request.form.get('b', 0))
        operation = request.form.get('operation')

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b != 0:
                result = a / b
            else:
                result = "Cannot divide by zero."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
