from flask import Blueprint, request, jsonify, render_template
from . import auth_bp

@auth_bp.route('/signup', methods=['POST, GET'])
def signup():
    # Get the signup data from the request
    data = request.get_json()

    # TODO: Implement the signup logic here

    # Return a success message
    return render_template('auth/signup.html')

@auth_bp.route('/login', methods=['POST, GET'])
def login():
    # Get the login data from the request
    data = request.get_json()

    # TODO: Implement the login logic here

    # Return a success message
    return  render_template('auth/login.html')