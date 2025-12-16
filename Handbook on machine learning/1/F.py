from sklearn.base import ClassifierMixin
from scipy.stats import mode


class MostFrequentClassifier(ClassifierMixin):
    def fit(self, X=None, y=None):
        '''
        Parameters
        ----------
        X : array like, shape = (n_samples, n_features)
        Training data features
        y : array like, shape = (_samples,)
        Training data targets
        '''
        self.most_frequent_ = mode(y)[0][0]
        return self

    def predict(self, X=None):
        return [self.most_frequent_] * len(X) if X is not None else []