from data_splitter import split
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


def saveModel():
    clf, x_test, y_test = split()
    y_pred = clf.predict(x_test)
    # print(y_pred)
    # print(accuracy_score(y_pred, y_test))
    # print(confusion_matrix(y_pred, y_test))
    pickle.dump(clf, open('img_model.p', 'wb'))


def getModel():
    model = pickle.load(open('img_model.p', 'rb'))
    return model;


if __name__ == '__main__':
    saveModel()
