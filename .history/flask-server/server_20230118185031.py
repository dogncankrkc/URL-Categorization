
from flask import Flask, request
app = Flask(__name__)

import sys
sys.path.insert(0, 'C:/Users/PC/Desktop/URLCategorization')
from main import x

@app.route('/cat' ,methods=['POST','GET'])
def cat():
    global url
    if request.method == 'POST':
        request_data = request.get_json()
        url=request_data['input']
        return 'a'
    elif request.method == 'GET':
        sonuc=x(url)
        a=sonuc[0]
        b=sonuc[1]
        return [a,b]
       

if __name__ == '__main__':
    app.debug = True
    app.run()