from flask import Flask

app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Hello Flask"

# POST /store     
app.run(port=5000)
