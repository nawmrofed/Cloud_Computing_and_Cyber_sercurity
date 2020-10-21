from flask import Flask
from flask import render_template
from flask import request
from math import sqrt
import requests


app = Flask(__name__)

# def isPrime(n):
#     if n > 1:
#         if n == 2:
#             return True
#         if n % 2 == 0:
#             return False
#         for x in range(3, int(sqrt(n) + 1), 2):
#             if n % x == 0:
#                 return False
#         return True
#     return False

@app.route('/calculate.html')
def post_html():
    return render_template('calculate.html')

@app.route('/deal_request', methods = ['GET', 'POST'])
def deal_request():
    if request.method == "POST":
        # post通过request.form["param_name"]形式获取参数值
        post_q = request.form["q"]
        if post_q.isnumeric():
            r = requests.get('https://2jxi3yokuh.execute-api.us-east-2.amazonaws.com/default/Helloworld?q=' + post_q)
            if r.status_code == requests.codes.ok:
                if r.text == 'true':
                    return render_template("./result.html", result=post_q + ' is prime.')
                else:
                    return render_template("./result.html", result=post_q + ' is not prime.')
            else:
                return render_template("./result.html", result='function is not working now')
        else:
            return render_template("./result.html", result=post_q + ' is not number!')
if __name__ == '__main__':
    # default：host=127.0.0.1, port=5000, debug=false
    app.run()