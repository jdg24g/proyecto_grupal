from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.secret_key = "projectzero"

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '8d126d6c2c79e1'
app.config['MAIL_PASSWORD'] = 'fd7d497ea508ae'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False