from flask import Flask, request, jsonify
from flask_restplus import Resource, Api, fields, reqparse

# stuff for the models
from utils.strings import TARGET, FEATURES, CAT_FEATURES, DATE
from utils.utilities import select_by_date
import pandas as pd
import pickle

flask_app = Flask(__name__)
app = Api(app = flask_app,
          version = "v1.0",
          title = "PizzaRat",
          description = "Get likelihood of a restaurant having a critical violation")

# name_space = app.namespace('names', description='Manage names')
name_space = app.namespace('apis', description='APIs assciated with restaurant predictions')

predict_parser = reqparse.RequestParser()
predict_parser.add_argument('start_date', type=str, required=False, default='2019-05-01')
predict_parser.add_argument('end_date', type=str, required=False, default='2019-05-31')
predict_parser.add_argument('model', type=str, required=False,
                                  choices=['log', 'ada', 'gbt', 'nn', 'rf', 'xgb'], default='rf')

truth_parser = reqparse.RequestParser()
truth_parser.add_argument('start_date', type=str, required=False, default='2019-05-01')
truth_parser.add_argument('end_date', type=str, required=False, default='2019-05-31')

@name_space.route("/predict")
class MainClass(Resource):
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' },
             params={ 'start_date': 'Starting date for the prediction window',
                        'end_date': 'Ending date for the prediction window'})
    @app.expect(predict_parser)
    def get(self):
        """Get critical violation predictions"""
        args = predict_parser.parse_args()
        self.start_date = args['start_date']
        self.end_date = args['end_date']
        self.model_name = args['model']
        self.model = self.load_model()

        # load data
        df, FEATURES_big = self.load_catalogs(self.start_date, self.end_date)

        # make a prediction from model
        preds = self.model.predict(df[FEATURES_big])
        pred_probs = self.model.predict_proba(df[FEATURES_big])

        output = {'camis': df.camis.values.tolist(),
                DATE: df[DATE].dt.strftime("%m-%d-%Y").values.tolist(),
                  'prediction': preds.tolist(),
                  'probability': pred_probs.tolist()}

        return jsonify(output)

    def load_model(self):
        models = {'log': 'logmodel.pkl',
                    'ada': 'AdaBmodel.pkl',
                    'gbt': 'GBTmodel.pkl',
                    'nn': 'NNmodel.pkl',
                    'rf': 'RFmodel.pkl',
                    'xgb': 'XGBmodel.pkl'}
        try:
            model = models[self.model_name]
            clf_path = f'./models/{model}'
            with open(clf_path, 'rb') as f:
                model = pickle.load(f)
            return model
        except KeyError as e:
            name_space.abort(500, e.__doc__, status = "Could not retrieve model information", statusCode = "500")
        except Exception as e:
            name_space.abort(400, e.__doc__, status = "Could not retrieve model information", statusCode = "400")

    def load_catalogs(self, start_date, end_date, FEATURES=FEATURES):
        inspecs = pd.read_csv('./data/inspec_scores.csv', parse_dates=[DATE])
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

@name_space.route("/truth")
class MainClass(Resource):
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' },
             params={ 'start_date': 'Starting date for the prediction window',
                        'end_date': 'Ending date for the prediction window'})
    @app.expect(truth_parser)
    def get(self):
        """Get critical violation truths"""
        args = truth_parser.parse_args()
        self.start_date = args['start_date']
        self.end_date = args['end_date']
        self.model_name = args['model']
        self.model = self.load_model()

        inspecs = pd.read_csv('./data/inspec_scores.csv', parse_dates=[DATE])
        df = select_by_date(inspecs, self.start_date, self.end_date)

        output = {'camis': df.camis.values.tolist(),
                DATE: df[DATE].strftime("%Y-%m-%d").values.tolist(),
                  'critical': df.critical.values.tolist()}

        return jsonify(output)

    def load_model(self):
        pass

if __name__ == '__main__':
     app.run(port='5000', debug=True)
