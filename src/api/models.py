from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    identification_type = db.Column(db.Enum('DNI', 'NIE', 'Passport', name='identification_type'), nullable=True)
    identification_number = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean(), unique=False, nullable=False)
    # Relaciones
    # author_to = db.relationship('Authors')  # Se definio en le backref user_to

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        # Do not serialize the password, its a security breach
        return {'id': self.id,
                'email': self.email,
                'firstname': self.firstname,
                'lastname': self.lastname,
                'identification_type': self.identification_type,
                'identification_number': self.identification_number,
                'is_active': self.is_active,
                'is_admin': self.is_admin}


class Authors(db.Model):
    # __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    dob =  db.Column(db.Date, unique=False, nullable=False)
    country = db.Column(db.String, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to = db.relationship('Users', foreign_keys=[user_id], backref=db.backref('author_to', lazy='select'))

    def __repr__(self):
        return f'<Author: {self.id} - {self.name}>'

    def serialize(self):
        return {'id': self.id,
                'dob': self.dob,
                'country': self.country,
                'user_id': self.user_id,
                'books': [row.serialize() for row in self.book_to]}


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author_to = db.relationship('Authors', foreign_keys=[author_id], backref=db.backref('book_to', lazy='select'))

    def __repr__(self):
        return f'<Book: {self.id} - {self.title}>'

    def serialize(self):
        return {'id': self.id,
                'title': self.title,
                'author_id': self.author_id}
