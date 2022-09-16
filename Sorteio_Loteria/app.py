from flask import Flask
from controller import verify_mega

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

app.add_url_rule('/mega',methods=['POST'],view_func=verify_mega)

app.run(host='0.0.0.0',port=80)