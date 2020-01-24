from sklearn import svm
from sklearn import datasets
import pickle

clf = svm.SVC()
X, y= datasets.load_iris(return_X_y=True)
clf.fit(X, y)

with open('model.pkl', 'wb') as model:
    pickle.dump(clf, model)
