import process_data
import pickle
from sklearn import tree, svm
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import MultinomialNB

'''
    This file contains three models: Decision Tree, Support Vector Machines, and Multinomial Naive Bayes 
    Before fitting each model with the data, I conducted a Grid Search over certain parameters to find the best
    performing ones. 
'''


def nb_learner(train_x, test_x, train_y, test_y):

    params = {
        'alpha': [1.0, 2.0, 3.0]
    }

    nb_clf = MultinomialNB()

    gs = GridSearchCV(nb_clf, params)

    gs.fit(train_x, train_y)

    accuracy = gs.score(test_x, test_y)

    file_name = 'nb_model.pkl'
    with open(file_name, 'wb') as file:
        pickle.dump(gs, file)

    return accuracy


def svm_learner(train_x, test_x, train_y, test_y):

    params = {
        'degree': [1, 3, 5, 7]
    }

    svm_clf = svm.SVC()

    gs = GridSearchCV(svm_clf, params)

    gs.fit(train_x, train_y)

    accuracy = gs.score(test_x, test_y)

    file_name = 'svm_model.pkl'
    with open(file_name, 'wb') as file:
        pickle.dump(gs, file)

    return accuracy

    
def tree_learner(train_x, test_x, train_y, test_y):

    params = {
        'criterion': ['gini', 'entropy'],
        'max_depth': [10, 50, 100, 250]
    }

    tree_clf = tree.DecisionTreeClassifier()

    gs = GridSearchCV(tree_clf, params)

    gs.fit(train_x, train_y)

    accuracy = gs.score(test_x, test_y)

    file_name = 'tree_model.pkl'
    with open(file_name, 'wb') as file:
        pickle.dump(gs, file)

    return accuracy


def main():
    train_features, test_features, train_targets, test_targets = process_data.main()

    tree_acc = tree_learner(train_features, test_features, train_targets, test_targets)

    svm_acc = svm_learner(train_features, test_features, train_targets, test_targets)

    nb_acc = nb_learner(train_features, test_features, train_targets, test_targets)

    print(tree_acc) # 0.9809
    print(svm_acc) # 0.9826
    print(nb_acc) # 0.9287


if __name__ == '__main__':
    main()
