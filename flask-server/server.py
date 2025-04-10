
from flask import Flask, request
app = Flask(__name__)

# Import the prediction function
import sys
sys.path.insert(0, 'C:/Users/user/OneDrive/Masaüstü/URL-Categorization')
from main import x

# POST: Accept URL from client
# GET: Return prediction result based on previously received URL
@app.route('/cat' ,methods=['POST','GET'])
def cat():
    global url
    if request.method == 'POST':
        request_data = request.get_json()
        url=request_data['input']
        return ''
    elif request.method == 'GET':
        result=x(url)
        if result == None:
            return ''   
        a=result[0]
        b=result[1]
        return [a,b]

if __name__ == '__main__':
    app.debug = True
    app.run()