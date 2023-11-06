from flask import Flask, jsonify
from database import DatabaseOperator

# info: database information.
data_operator = DatabaseOperator(database='q_mgmt', 
                user='postgres', 
                password='postgres', 
                host='localhost',
                port=5432)



app = Flask(__name__)

# do: provide get information.
@app.route('/data', methods=["GET"])
def hello_world():

    question = data_operator.extract_first_question()
    
    response = jsonify({"question":question})
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response