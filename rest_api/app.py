import mimetypes
from flask import Flask, request, jsonify ,render_template, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import secure_filename
import os
import base64

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Swagger
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(swaggerui_blueprint,url_prefix=SWAGGER_URL)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# User  class/model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    pword = db.Column(db.String(15))
    fullname = db.Column(db.String(30))
    photo = db.Column(db.Text)
    photo_name = db.Column(db.Text)
    photo_mimetype = db.Column(db.Text)

    def __init__(self, username, pword, fullname, photo, photo_name, photo_mimetype):
        self.username = username
        self.pword = pword.encode('utf-8')
        self.pword = base64.b64encode(self.pword)
        self.fullname = fullname
        self.photo = photo
        self.photo_name = photo_name
        self.photo_mimetype = photo_mimetype
# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','username','password','fullname','photo')
    
# Post class/model
class Post(db.Model): #title, description, priority, status, published_date ,user,created_at,updated_at
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(200))
    priority = db.Column(db.Integer)
    status = db.Column(db.String(15))
    published_date = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    
    def __init__(self, title, description, priority, status, user_id):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.user_id = user_id

# Post Schema
class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'priority', 'status', 'published_date', 'user', 'created_at', 'updated_at')

# Init Schema
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# redirect from index
@app.route('/')
def index():
    return redirect(url_for('signup'))

# signup page
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='POST':
        pic = request.files['photo']
        if not pic:
            return 'no pic uploaded', 400
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        new_user = User(request.form['username'],request.form['password'],request.form['fullname'],photo=pic.read(), photo_mimetype=mimetype,photo_name=filename)
        db.session.add(new_user)
        db.session.commit()
        return redirect('signin')
    else:
        return render_template('auth/signup.html')

# signin page
@app.route('/signin', methods=['GET','POST'])
def signin():
    if request.method=='POST':
        try:
            user = User.query.filter(User.username == request.form['username']).one()
            pword = request.form['password'].encode('utf-8')
            pword = base64.b64encode(pword)
            if user.pword == pword:
                return redirect(url_for('get_post',id=user.id))
            else:
                return redirect('signup')
        except:
            return 'User not found', 400
    else:
        return render_template('auth/signin.html')

# Create a Post
@app.route('/post', methods=['POST'])
def add_post():
    title = request.json['title']
    description = request.json['description']
    priority = request.json['priority']
    status = request.json['status']
    user = request.json['user']

    new_post = Post(title, description, priority, status, user)

    db.session.add(new_post)
    db.session.commit()

    return post_schema.jsonify(new_post)

# Get all Posts
@app.route('/post', methods=['GET'])
def get_posts():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)
    return jsonify(result)

# get user post
@app.route('/post/<id>', methods=['GET'])
def get_post(id):
    posts = Post.query.filter(Post.user_id == id).all()
    result = posts_schema.dump(posts)
    return jsonify(result)

# Update a Post 
@app.route('/posts/<id>', methods=['PUT'])
def update_Post(id):
    post = Post.query.get(id)

    title = request.json['title']
    description = request.json['description']
    priority = request.json['priority']
    status = request.json['status']
    user = request.json['user']
    post.title = title
    post.description = description
    post.priority = priority
    post.status = status
    post.user = user

    db.session.commit()

    return post_schema.jsonify(post)

# Delete Post
@app.route('/posts/<id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return post_schema.jsonify(post)

# Run server
if __name__ == '__main__':
    app.run(debug=True)