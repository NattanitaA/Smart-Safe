from flask import Flask, redirect, url_for, request, render_template, jsonify, request
import ast, json, os, webbrowser, csv
from time import sleep
from enrollm1 import enroll
from checkm1 import check
#from Drawer_Data import *
#from Username_Data import *


data = '0'
withdrawdata = '0'
fingerAuth = 0
state = 0
app = Flask(__name__)

# @app.route('/', methods = ['GET'])
@app.route('/')
def home():
    return render_template('welcome_safebox.html')
    
@app.route('/check_finger')
def checkFinger():
    return render_template('fingerprint.html')

@app.route('/enroll_finger')
def enroll_finger_():
    return render_template('fingerprint_register.html')

@app.route('/no_finger_found')
def noFinger():
    return render_template('regis_adminpass.html')

@app.route('/name_deposit', methods = ['GET','POST'])
def nameDeposit():
        if request.method == 'POST':
            name = request.form['FirstName']       
            return render_template('WithdrawOrDeposit.html')

@app.route('/withdraw_or_deposit')
def WithdrawOrDeposit():
        return render_template('WithdrawOrDeposit.html')

@app.route('/check', methods = ['GET','POST'])
def check_():
    global check_tim
    global Username
    if request.method == 'POST':
        check_tim = check()
        if check_tim != (-1):
            #Username = findUsernameData(str(check_tim))
          #  print(Username)
            return render_template('WithdrawOrDeposit.html')
        else:
            return render_template('regis_adminpass.html')
    return ('error')

@app.route('/admin_password', methods = ['POST'])
def adminPassword():
    SetPassword = '12345'
    if request.method == 'POST':
        GetPassword = request.form['Password']
        print (GetPassword)
        if GetPassword == SetPassword:
            return render_template('register.html')
        else:
            return redirect(url_for('noFinger'))

@app.route('/register', methods = ['POST'])
def enroll_():
    global fingerData
    global register_name
    if request.method == 'POST':
        fingerData = enroll()
        if fingerData != (-1):
            print(fingerData)
#             writeUsernameData(register_name, fingerData)
            return redirect(url_for('home'))
        else:
                return render_template('regest_fail.html')
    return ('error')


@app.route('/register_name', methods = ['POST'])
def getRegisterName():
    global register_name
    if request.method == 'POST':
        register_name = request.form['FirstName']
        print (register_name)
        return render_template('fingerprint_register.html')

@app.route('/deposit')
def click_deposit():
    return render_template('open.html')
    
@app.route('/withdraw')
def click_withdraw():
    return render_template('open.html')

# @socketio.on('data')
# def camera():
#     
    

#     global state
#     if request.method == 'GET':
#         if state == 0:
#             if check_():
#                 state = 1
#                 print('open')
#                 state= 0
#                 return 'done'
#             else:
#                 state=1
#                 print('close')
#                 state=0
#                 return 'fail'
