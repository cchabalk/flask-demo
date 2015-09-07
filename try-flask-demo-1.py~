import os
import sys
from flask import Flask

app = Flask(__name__)

from app import app
app.run()

@app.route('/')
def hello():
    print(sys.version)
    print('this file is being read')
    return 'this file is being read'
