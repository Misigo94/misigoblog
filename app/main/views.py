from flask import abort, render_template,request,redirect,url_for
from flask_login import login_required,current_user
from datetime import datetime
from .. import db,photos
from . import main
from ..models import User,Comment,Post
import requests,json
from .forms import PostForm,CommentForm

@main.route('/',  methods=["GET","POST"])
# @login_required
def index():
    quotes=requests.get("http://quotes.stormconsultancy.co.uk/random.json")
    data=json.loads(quotes.content)
    message = '<h1> PLease enter</h1>'
    postes = Post.query.all()
    return render_template('index.html',data=data,message=message)

@main.route("/", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        # Get form filled details
        form = request.form
        title = form.get("title")
        category = form.get("radioselection")
        description = form.get("postdescription")
    return render_template('index.html')

@main.route("/home")
@login_required
def about():
    quotes=requests.get("http://quotes.stormconsultancy.co.uk/random.json")
    data=json.loads(quotes.content)
    # postes = Post.query.all()
    return render_template("index.html",data=data)

@main.route("/post", methods=["GET","POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():

        
        title = form.posttitle.data
        category = form.postcategory.data
        description = form.postdescription.data
        post = Post(title=title, category=category, description = description, author_id= current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new_posy.html',form=form)

@main.route('/post/details/<post_id>')
@login_required
def post_details(post_id):
    quotes=requests.get("http://quotes.stormconsultancy.co.uk/random.json")
    data=json.loads(quotes.content)
    post = Post.query.get(post_id)
    comments = Comment.query.filter_by(id = post_id).all()
    return render_template('details.html',post = post ,data=data,comments = comments)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

# ROute to page you want to display commments on
@main.route('/comment/save/<post_id>', methods=['POST','GET'])
@login_required
# Generate new fucntion for saving ccomment 
def save_comment(post_id):

    if request.method == 'POST': #Get comment from form
        content = request.form.get('content') 
        new_comment = Comment(content=content, author_id=current_user.id, post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.post_details',post_id = post_id))

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
