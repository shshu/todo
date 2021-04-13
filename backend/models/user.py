from app import bcrypt, db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.email = email

    def __repr__(self):
        return f'username {username}>'

def get_user(username):
    user = User.query.filter_by(username=username).all()
    if user:
        return user[0]
    return []

def is_authenticate(username, password):
    """
    Authenticate a username/password - this sample routine simply checks
    the username/password against a hard-coded table, a real-world
    implementation would authenticate users against a database or external
    service.
    """
    user = User.query.filter_by(username=username).all()
    if not user:
        return False
    
    if user[0].password:
        return True

    return False

