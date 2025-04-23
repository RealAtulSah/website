from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class VLE(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    consumers = db.relationship('Consumer', backref='vle', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Consumer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    block = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(64), nullable=False)
    district = db.Column(db.String(64), nullable=False)
    pin_code = db.Column(db.String(6), nullable=False)
    ca_number = db.Column(db.String(64), nullable=False)
    vle_id = db.Column(db.Integer, db.ForeignKey('vle.id'), nullable=False)

@login_manager.user_loader
def load_user(id):
    return VLE.query.get(int(id))
