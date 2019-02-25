from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")
    response = ""

    if text == '':
        # response = '''CON UGAPAY QUICKTELLER \n
        # 1. Deposit to Wallet
        # 2. Send Money
        # 3. Withdraw Money
        # 4. Pay Merchant
        # 5. My Account
        # '''
        response = "CON UGAPAY QUICKTELLER \n"
        response += "1. Deposit to Wallet \n"
        response += "2. Send Money \n"
        response += "3. Withdraw Money \n"
        response += "4. Pay Merchant \n"
        response += "5. My Account \n"
    elif text == '1':
        response = "CON Choose account information you want to view \n"
        response += "1. My wallet \n"
        response += "2. Other Wallet"
    elif text == '2':
        response = "CON Your phone number is \n"
        response += "1. UGAPAY wallet \n"
        response += "2. Mobile Number"
    elif text == '1*1':
        response = "END Thank you for using UGAPAY Wallet "
    elif text == '1*2':
        response = "CON Enter mobile number"
    return  response

if __name__ == '__main__':
    app.run(debug=True)