import os
import sys
from flask import Flask
from app import app

#app = Flask(__name__)

def hello():
    print(sys.version)
    print('this file is being read')
    return app
