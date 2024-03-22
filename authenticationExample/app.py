from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_session import Session

app = Flask(__name__)

# Configure the secret key and Flask-Session
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user store
users = {'mike': {'password': 'milk_123'}}

# User model
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# User Loader
@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('protected'))
        else:
            return 'Invalid username or password'
    return render_template('index.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out!'

# Protected route
@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + session.get('user_id', '')

# Home route
@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=False)