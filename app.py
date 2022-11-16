"""
module api contains a flask app with a single endpoint.
"""
from flask import Flask, jsonify, request
import logging
  
logging.basicConfig(filename='record.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s') 
app = Flask(__name__)
  

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET' and request.headers['Accept'] == 'application/json'):
        app.logger.debug("GET with header Accept")
        return {'message': 'hello world'}
    elif (request.method == 'GET'):
        app.logger.debug("GET without header Accept")
        return "<p>Hello, World</p>"
    else:
        app.logger.debug("POST call")
        return "{'message': 'hello world'}"

  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)