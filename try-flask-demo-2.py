import os
import sys
from flask import Flask

app = Flask(__name__)

from app import views

#app.run()

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index(): 
        return render_template('index.html')

def hello():
    print(sys.version)
    print('this file is being read')
    return 'this file is being read now'
