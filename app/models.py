
from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_bcrypt import Bcrypt
import bcrypt

from app import db, login_manager
from . import app


class Employee(UserMixin, db.Model):
    """ Create an Employee table
    """

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(256))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, password):
        # self.password_hash = generate_password_hash(password)
        # bcrypt = Bcrypt()
        if app.config.get('SECURITY_PASSWORD_SALT'):
            # self.password_hash = bcrypt.generate_password_hash(password, app.config['SECURITY_PASSWORD_SALT'])
            # self.password_hash = bcrypt.generate_password_hash(password)
            self.password_hash = bcrypt.hashpw(password.encode('utf-8'), app.config['SECURITY_PASSWORD_SALT'].encode('utf-8')).decode('utf-8')
        else:
            print("SECURITY_PASSWORD_SALT not defined.")
            self.password_hash = None

    def verify_password(self, password):
        # return check_password_hash(self.password_hash, password)
        # bcrypt = Bcrypt()
        # return bcrypt.check_password_hash(self.password_hash, password)
        print("self.password_hash =", self.password_hash)
        print("self.password_hash.encoded = ", self.password_hash.encode('utf-8'))
        print("password = ", password)
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """ Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """ Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
