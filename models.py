from app import db

class User(db.Model):
    __tablename__ == 'users'
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(20), unique = False, nullable = False)
    lastName = db.Column(db.String(20), unique = False, nullable = False)
    email = db.Column(db.String(25), unique = True, nullable = False)