from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

import numpy as np

from evestop.generic import EVEEarlyStopping

batch_size = 16

# Let's test EVE early stopping rule on MNIST with a linear model trained with SGD
classifier = SGDClassifier()
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

# Setting the early stopping rule for maximization process
# Rule: stop when smoothed quality hasn't increased in 50 iterations
# The smoothing hypermarameter is left as default
early_stopping = EVEEarlyStopping(mode='max', patience=50)

while early_stopping.proceed:
    subset = np.random.choice(len(X_train), batch_size)
    classifier.partial_fit(X_train[subset], y_train[subset], classes=digits.target_names)

    score = classifier.score(X_test, y_test)
    early_stopping.register(measurement=score,
                            measuree=classifier.coef_.copy())

# Restoring best known parameters
classifier.coef_ = early_stopping.best_measuree
print(classifier.score(X_test, y_test))