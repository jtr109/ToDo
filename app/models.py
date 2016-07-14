from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from datetime import datetime

from . import db
from . import login_manager


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    todo_lists = db.relationship('ToDoList', backref='master', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_password_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset_password': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset_password') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_changing_email_request(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ToDoList(db.Model):
    __tablename__ = 'todo-lists'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    master_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tasks = db.relationship('Task', backref='in_list', lazy='dynamic')
    events = db.relationship('ListEvent', backref='in_list', lazy='dynamic')

    @staticmethod
    def on_insert(mapper, connection, target):
        list_event = ListEvent(event='List "%s" was created.' % target.title,
                               list_id=target.id)
        db.session.add(list_event)

    @staticmethod
    def on_delete(mapper, connection, target):
        list_event = ListEvent(event='List "%s" was deleted.' % target.title,
                               list_id=target.id)
        db.session.add(list_event)

    def __repr__(self):
        return '<ToDoList %r>' % self.id

db.event.listen(ToDoList, 'after_insert', ToDoList.on_insert)
db.event.listen(ToDoList, 'before_delete', ToDoList.on_delete)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(64))  # todo: Is 'db.String' enough?
    state = db.Column(db.String(64), default='todo')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    list_id = db.Column(db.Integer, db.ForeignKey('todo-lists.id'))

    @staticmethod
    def on_changed_state(target, value, oldvalue, initiator):
        target.timestamp = datetime.utcnow()
        list_event = ListEvent(event='Task "%s" was changed from "%s" to "%s".' % (target.body, oldvalue, value),
                               list_id=target.list_id)
        db.session.add(list_event)

    @staticmethod
    def on_insert(mapper, connection, target):
        list_event = ListEvent(event='Task "%s" was created.' % target.body,
                               list_id=target.list_id)
        db.session.add(list_event)

    @staticmethod
    def on_delete(mapper, connection, target):
        list_event = ListEvent(event='Task "%s" was deleted.' % target.body,
                               list_id=target.list_id)
        db.session.add(list_event)

    def __repr__(self):
        return '<Task %r>' % self.id

db.event.listen(Task.state, 'set', Task.on_changed_state)
db.event.listen(Task, 'after_insert', Task.on_insert)
db.event.listen(Task, 'before_delete', Task.on_delete)


class ListEvent(db.Model):
    __tablename__ = 'list-events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    list_id = db.Column(db.Integer, db.ForeignKey('todo-lists.id'))

    def __repr__(self):
        return '<List Event %r>' % self.id
