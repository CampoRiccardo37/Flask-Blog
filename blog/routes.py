from flask import render_template
from blog import app



@app.route("/")
def homepage():
    posts = [
        {"title":"primo POST", "body":"random"},
        {"title":"secondo POST", "body":"Some random"}
    ]
    some_bool = False
    return render_template( 
                            "homepage.html", 
                            posts=posts, 
                            boolean_flag=some_bool
                        )

@app.route("/about")
def about():
    return render_template( "about_page.html")