from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username= db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
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
                'password': self.password,
                'is_active': self.is_active,
                'is_admin': self.is_admin}


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to = db.relationship('Users', foreign_keys=[user_id], backref=db.backref('post_to', lazy='select'))

    def __repr__(self):
        return f'<Posts {self.user_id}>' 
    
    def seralize(self):
        return{"user.id": self.user_id}


class Followers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_from_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_from_to = db.relationship('Users', foreign_keys=[user_from_id])
    user_to_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to_to = db.relationship('Users', foreign_keys=[user_to_id],)

    def __repr__(self):
        return f'<Followers {self.user_from_id} - {self.user_to_id}>' 
    
    def seralize(self):
        return{"user_from_id": self.user_from_id,
               "user_to_id": self.user_to_id} 


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(400), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author_to = db.relationship('Users', foreign_keys=[author_id])
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users', foreign_keys=[user_id], backref=db.backref('comment_to', lazy='select'))

    def __repr__(self):
        return f'<Comments {self.comment_text} >' 
    
    def seralize(self):
        return{"id" : self.id,
            "user_from_id": self.comment_text,
             "author_id" : self.author_id,
              "user_id" : self.user_id }
    

class Medias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media_type = db.Column(db.Enum('video', 'image', 'sounds', name='media_type'), unique=True, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    post_to = db.relationship('Posts', foreign_keys=[post_id], backref=db.backref('media_to', lazy='select'))

    def __repr__(self):
        return f'<Medias {self.medias_type} >'

    def serealize(self):
        return{"id" : self.id,
               "medias_type" : self.media_type,
               "url" : self.url,
               "post_id" : self.post_id }
    
