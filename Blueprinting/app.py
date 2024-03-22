from flask import Flask, render_template, request, url_for, session
from Milk import create_app

app = create_app()


if __name__ == '__main__':
    # app.run(host='localhost', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=False)