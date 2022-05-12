from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
   
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)
            def verify_password(self,password):
                return check_password_hash(self.pass_secure,password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User {self.username}'
            
# from . import db
# from werkzeug.security import generate_password_hash,check_password_hash
# from . import login_manager
# from datetime import datetime
# from flask_login import UserMixin,current_user



# class User(UserMixin,db.Model):
#     __tablename__='users'

#     id= db.Column(db.Integer,primary_key=True)
#     username= db.Column(db.String(255))
#     email = db.Column(db.String(255),unique = True,index = True)
#     bio = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())
#     pass_secure = db.Column(db.String(255))
    # pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    # comment = db.relationship('Comment', backref='user', lazy='dynamic')
    # upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    # downvote = db.relationship('Downvote',backref='user',lazy='dynamic')
#     @property
#     def password(self):
#         raise AttributeError('You cannot read the password attribute')

#     @password.setter
#     def password(self, password):
#         self.pass_secure = generate_password_hash(password)


#     def verify_password(self,password):
#         return check_password_hash(self.pass_secure,password)
    
#     def save_u(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     def __repr__(self):
#         return f'User{self.username}'

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))



# class Pitch(db.Model):
#     __tablename__ = 'pitches'
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(255),nullable = False)
#     post = db.Column(db.Text(), nullable = False)
#     comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
#     upvote = db.relationship('Upvote',backref='pitch',lazy='dynamic')
#     downvote = db.relationship('Downvote',backref='pitch',lazy='dynamic')
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     time = db.Column(db.DateTime, default = datetime.utcnow)
#     category = db.Column(db.String(255), index = True,nullable = False)
    
#     def save_p(self):
#         db.session.add(self)
#         db.session.commit()

        
#     def __repr__(self):
#         return f'Pitch {self.post}'

# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     comment = db.Column(db.Text(),nullable = False)
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
#     pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

#     def save_c(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_comments(cls,pitch_id):
#         comments = Comment.query.filter_by(pitch_id=pitch_id).all()

#         return comments

    
#     def __repr__(self):
#         return f'comment:{self.comment}'        


# class Upvote(db.Model):
#     __tablename__ = 'upvotes'

#     id = db.Column(db.Integer, primary_key=True)
#     upvote = db.Column(db.Integer, default=1)
#     pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     def save_upvotes(self):
#         db.session.add(self)
#         db.session.commit()

#     def add_upvotes(cls, id):
#         upvote_pitch = Upvote(user=current_user, pitch_id=id)
#         upvote_pitch.save_upvotes()

#     @classmethod
#     def get_upvotes(cls, id):
#         upvote = Upvote.query.filter_by(pitch_id=id).all()
#         return upvote

#     @classmethod
#     def get_all_upvotes(cls, pitch_id):
#         upvotes = Upvote.query.order_by('id').all()
#         return upvotes

#     def __repr__(self):
#         return f'{self.user_id}:{self.pitch_id}'        

# class Downvote(db.Model):
#     __tablename__ = 'downvotes'

#     id = db.Column(db.Integer, primary_key=True)
#     downvote = db.Column(db.Integer, default=1)
#     pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     def save_downvotes(self):
#         db.session.add(self)
#         db.session.commit()

#     def add_downvotes(cls, id):
#         downvote_pitch = Downvote(user=current_user, pitch_id=id)
#         downvote_pitch.save_downvotes()

#     @classmethod
#     def get_downvotes(cls, id):
#         downvote = Downvote.query.filter_by(pitch_id=id).all()
#         return downvote

#     @classmethod
#     def get_all_downvotes(cls, pitch_id):
#         downvote = Downvote.query.order_by('id').all()
#         return downvote

#     def __repr__(self):
#         return f'{self.user_id}:{self.pitch_id}'