from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:0812@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title,body):
        self.title = title
        self.body = body
        
@app.route('/',methods = ['POST', 'GET'])
def blog():

    blogs = Blog.query.all()
    single= request.args.get('blog.id')
    

    if request.method == 'request.args':
        return render_template('single_blog.html',blog_id=blog_id)

    else:
        return render_template('blog.html', 
        title="Build a Blog!", blogs=blogs, single=single )

    
 


@app.route('/newpost',methods = ['POST', 'GET'])
def add_blog():

    if request.method == 'POST':

        title = request.form['title']
        body = request.form['body']
        new_blog = Blog(title,body)
        
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect('/')

    else:
        return render_template('newpost.html')


if __name__ == '__main__':
    app.run()