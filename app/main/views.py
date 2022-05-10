from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import  User
from .forms import UpdateProfile
from .. import db,photos
from flask_login import login_required,current_user
from ..models import Pitch, User, Comment, Upvote, Downvote

from .forms import UpdateProfile,PitchForm,CommentForm,UpvoteForm
# from .forms import UpdateProfile,PitchForm,CommentForm

# @main.route('/')
# def index():
#     """
#     View root page function that returns the index page and its data

#     """

#     return render_template('index.html')

@main.route('/')
def index():
    pitches = Pitch.query.all()
    interview = Pitch.query.filter_by(category = 'Interview').all() 
    product = Pitch.query.filter_by(category = 'Product').all()
    promotion = Pitch.query.filter_by(category = 'promotion').all()

    return render_template('index.html', interview = interview,product = product, pitches = pitches,promotion= promotion)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('pitch.html', form = form)  

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)      

@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods=['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id=pitch_id)

    if Upvote.query.filter(Upvote.user_id == user.id, Upvote.pitch_id == pitch_id).first():
        return redirect(url_for('main.index'))

    new_upvote = Upvote(pitch_id=pitch_id, user=current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))


@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods=['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id=pitch_id)

    if Downvote.query.filter(Downvote.user_id == user.id, Downvote.pitch_id == pitch_id).first():
        return redirect(url_for('main.index'))

    new_downvote = Downvote(pitch_id=pitch_id,user=current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))
