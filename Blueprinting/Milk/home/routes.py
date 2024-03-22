from flask import Flask, render_template, Blueprint
from . import home_bp

@home_bp.route('/')
def index():
    return render_template('home/index.html')
