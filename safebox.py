from flask import Flask, redirect, url_for, request, render_template, jsonify, request
import ast, json, os, webbrowser, csv
# from time import sleep
import time
#from Drawer_Data import *
#from Username_Data import *

# data = '0'
# withdrawdata = '0'
# fingerAuth = 0
state = 0
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    global state
    if request.method == 'GET':
        if state == 0:
            state = 1
            print('Unlock')
            time.sleep(3)
            print('Lock')
            state=0
            return 'True'
@app.route('/controller_open', methods=["GET"])
def open():
    print('Unlock')
    return 'v'
           
@app.route('/controller_close', methods=["GET"])
def close():
    print('Lock')
    return 'b'


