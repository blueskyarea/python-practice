from sklearn import datasets
from sklearn import svm, metrics
import matplotlib.pyplot as plt

# load dataset of handwriting digits
digits = datasets.load_digits()
S = digits.data
T = digits.target
num_train = len(S)*2//3

# training data
S_train = S[:num_train]
# teachar data
T_train = T[:num_train]
# test data
S_test, T_test = S[num_train:], T[num_train:]

# classifier
# if specify large value to gamma, the boundary will be complexed.
clf = svm.SVC(gamma = 0.001)
# learn by training data & teachar data
clf.fit(S_train, T_train)

# evaluate the learned model by test data
accuracy = clf.score(S_test, T_test)
print(f" accuracy rate {accuracy}")

# count the classification failure
predicted = clf.predict(S_test)
num_error = (T_test != predicted).sum()
print(f" number of error {num_error}")

# more detail report
print("<<<<<< classification report")
print(metrics.classification_report(T_test, predicted))
print("<<<<<< confusion matrix")
print(metrics.confusion_matrix(T_test, predicted))

# result of classification with image
img_tt_pre = list(zip(digits.images[num_train:], T_test, predicted))
for index, (image, t_t, pred) in enumerate(img_tt_pre[404:416]):
    plt.subplot(3, 4, index + 1)
    plt.axis('off')
    plt.tight_layout()
    plt.imshow(image, cmap="Greys", interpolation="nearest")
    plt.title(f't:{t_t} pre:{pred}', fontsize=12)
plt.show()
