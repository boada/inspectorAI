from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps


# stuff for the models
from utils.strings import TARGET, FEATURES, CAT_FEATURES, DATE
from utils.utilities import select_by_date
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


app = Flask(__name__)
api = Api(app)

clf_path = 'models/logmodel.pkl'
with open(clf_path, 'rb') as f:
    model= pickle.load(f)

parser = reqparse.RequestParser()

def load_catalogs(start_date, end_date, FEATURES=FEATURES):
    inspecs = pd.read_csv('./data/inspecs_heat_scores.csv', parse_dates=[DATE])
    for feat in CAT_FEATURES:
        try:
            new_df = pd.concat([new_df, pd.get_dummies(inspecs[feat])], axis=1)
        except NameError:
            new_df = pd.DataFrame(index=inspecs.index)
            new_df = pd.concat([new_df, pd.get_dummies(inspecs[feat])], axis=1)
    FEATURES_big = FEATURES + new_df.columns.tolist()
    inspecs = pd.concat([inspecs, new_df], axis=1)

    test = select_by_date(inspecs, start_date, end_date)

    return test, FEATURES_big

class predict(Resource):
    def get(self):
        # use parser and find the user's query
        start_date = request.args['start_date']
        end_date = request.args['end_date']
        # args = parser.parse_args()
        # print('get', args)
        # start_date = args['start_date']
        # end_date = args['end_date']

        print(start_date, end_date)

        # load data
        df, FEATURES_big = load_catalogs(start_date, end_date)

        # make a prediction from model
        # prediction = model.predict(inputvector)
        pred = model.predict(df[FEATURES_big])

        print(pred[:10])
        # create JSON object
        output = {'predictions': [[int(c), int(p)] for c, p in zip(df.camis, pred)]}

        return jsonify(output)

    def post(self):
        # use parser and find the user's query
        args = parser.parse_args()
        start_date = args['start_date']
        end_date = args['end_date']

        print(start_date, end_date)

        # load data
        df, FEATURES = load_catalogs(start_date, end_date)

        # make a prediction from model
        # prediction = model.predict(inputvector)
        pred = model.predict(df[FEATURES])

        # create JSON object
        output = {'predictions': [[c, p] for c, p in zip(df.camis, pred)]}

        return jsonify(output)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(predict, '/predict') # Route_1
# api.add_resource(Employees, '/employees') # Route_1
# api.add_resource(Tracks, '/tracks') # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='8000', debug=True)
