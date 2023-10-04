import re
from flask import redirect,render_template,request,session,url_for

from app import app

regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def emailValid(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False

@app.route('/')
def index():
    return f"<h1>Hello World!</h1>"