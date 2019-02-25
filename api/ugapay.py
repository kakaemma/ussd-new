from flask import Flask, request, make_response, render_template
from utility.menu import *
from api import create_app


app = create_app('DevelopmentEnv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ussd', methods=['POST', 'GET'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    if text == '':
        menu = main_menu
    elif text == '1':
        menu = deposit_menu
    elif text == '2':
        menu = send_money_menu
    elif text == '1*1':
        menu = amount_prompt
    elif text == '1*2':
        menu = wallet_number_prompt
    else:
        menu = default_message
    return menu

