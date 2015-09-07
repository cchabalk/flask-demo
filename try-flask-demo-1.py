import os
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print(sys.version)
    print('this file is being read')
    return print('this file is being read')+sys.version
