from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import ShuffleSplit

# load iris data
iris = datasets.load_iris()
M = iris.data
T = iris.target

# create index for split data
iris_ss = ShuffleSplit(train_size=0.6, test_size=0.4, random_state=0)
train_index, test_index = next(iris_ss.split(M))

# split data
M_train, T_train = M[train_index], T[train_index]
M_test, T_test = M[test_index], T[test_index]

# create model
clf = svm.SVC()
# train
clf.fit(M_train, T_train)
# evaluate
print(clf.score(M_test, T_test))
