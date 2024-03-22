from flask import Flask, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
import werkzeug


app = Flask(__name__)
# Configure the SQLAlchemy part
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site123.db' # Local SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            if werkzeug.security.check_password_hash(user.password, password):
                session['user_id'] = user.id
                return url_for('profile')
            else:
                return 'Invalid password!'
        else:
            return 'No account found!'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(username, email, password)
        hashed_password = werkzeug.security.generate_password_hash(password=password, method='scrypt', salt_length=16)
        print(hashed_password)
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return 'User created!'
    return render_template('register.html')

@app.route('/profile')
def profile():
    session.get('user_id', '')
    user = User.query.filter_by(id=session.get('user_id', '')).first()
    username = user.username
    email = user.email
    return render_template('profile.html', username=username, email=email)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False)
