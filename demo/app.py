from flask import Flask, render_template, request
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import requests

app = Flask(__name__, template_folder="templates")
api = Api(app)

clf_path = 'models/model.pkl'
with open(clf_path, 'rb') as f:
    model= pickle.load(f)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('1')
parser.add_argument('2')
parser.add_argument('3')
parser.add_argument('4')

@app.route('/')
def student():
   return render_template('form.html')

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        result = request.form

        one = float(result['one'])
        two = float(result['two'])
        three = float(result['three'])
        four = float(result['four'])

        #order matters! check original model for schema
        input_vector = np.array([one, two, three, four]).reshape(1,-1)

        # make a prediction from model
        pred = model.predict(input_vector)

        # create JSON object
        output = {'prob_next_organic': int(pred)}
        return render_template('form.html', result=int(pred))

    else:
        render_template('form.html')


# @app.route('/', methods=['GET','POST'])
# def home():
#     if request.method == 'POST':
#         # use parser and find the user's query
#         args = parser.parse_args()
#         one = float(args['1'])
#         two = float(args['2'])
#         three = float(args['3'])
#         four = float(args['4'])
#
#         #order matters! check original model for schema
#         input_vector = np.array([one, two, three, four]).reshape(1,-1)
#
#         # make a prediction from model
#         # prediction = model.predict(inputvector)
#         pred = model.predict(input_vector)
#
#         # create JSON object
#         output = {'prob_next_organic': int(pred)}
#         return render_template('index.html', sentiment=int(pred))
#
#
#
#     return render_template('index.html', sentiment='')


#
#
#
# class predict(Resource):
#     def get(self):
#         # use parser and find the user's query
#         args = parser.parse_args()
#         one = float(args['1'])
#         two = float(args['2'])
#         three = float(args['3'])
#         four = float(args['4'])
#
#         #order matters! check original model for schema
#         input_vector = np.array([one, two, three, four]).reshape(1,-1)
#
#         # make a prediction from model
#         # prediction = model.predict(inputvector)
#         pred = model.predict(input_vector)
#
#         # create JSON object
#         output = {'prob_next_organic': int(pred)}
#
#         return render_template('index.html', sentiment=int(pred))
#
#     def post(self):
#         # use parser and find the user's query
#         args = parser.parse_args()
#         one = float(args['1'])
#         two = float(args['2'])
#         three = float(args['3'])
#         four = float(args['4'])
#
#         #order matters! check original model for schema
#         input_vector = np.array([one, two, three, four]).reshape(1,-1)
#
#         # make a prediction from model
#         # prediction = model.predict(inputvector)
#         pred = model.predict(input_vector)
#
#         # create JSON object
#         output = {'prob_next_organic': int(pred)}
#
#         return render_template('index.html', sentiment=int(pred))
#
# # Setup the Api resource routing here
# # Route the URL to the resource
# api.add_resource(predict, '/')

if __name__ == "__main__":
    app.run(port=3000, debug=True)
