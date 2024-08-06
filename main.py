from flask import Flask
from public import public
from admin import admin
from api import api

# from flask_cors import CORS

app=Flask(__name__)
# CORS(api)

app.register_blueprint(public)

app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(api,url_prefix='/api')


app.secret_key="abc"

app.run(debug=True,port=5035,host="0.0.0.0")