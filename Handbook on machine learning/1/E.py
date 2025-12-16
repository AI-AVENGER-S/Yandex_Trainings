from sklearn.base import RegressorMixin
from scipy.stats import mode


class MeanRegressor(RegressorMixin):
    def fit(self, X=None, y=None):
        '''
        Parameters
        ----------
        X : array like, shape = (n_samples, n_features)
        Training data features
        y : array like, shape = (_samples,)
        Training data targets
        '''
        self.mean_ = y.mean()
        return self

    def predict(self, X=None):
        '''
        Parameters
        ----------
        X : array like, shape = (n_samples, n_features)
        Data to predict
        '''
        return [self.mean_] * len(X) if X is not None else []