from sklearn.model_selection import train_test_split
from preprocessing import cleanup
from sklearn.model_selection import GridSearchCV
from sklearn import svm



def split():
    flat_data, target = cleanup()
    x_train, x_test, y_train, y_test = train_test_split(flat_data, target, test_size=0.3, random_state=109)

    param_grid = [{'C': [1, 10, 100, 1000], 'kernel': ['linear']},
                  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']}, ]

    svc = svm.SVC(probability=True)
    clf = GridSearchCV(svc, param_grid)
    clf.fit(x_train, y_train)
    return clf, x_test, y_test
