import numpy as np
from sklearn.linear_model import Ridge

class ExponentialLinearRegression(Ridge):
    
    def __init__(self, alpha=1.0, fit_intercept=True, copy_X=True,
                 max_iter=None, tol=1e-3, solver='auto', random_state=None):
        super().__init__(alpha=alpha, 
                        fit_intercept=fit_intercept,
                        copy_X=copy_X, 
                        max_iter=max_iter,
                        tol=tol, 
                        solver=solver,
                        random_state=random_state)


    def fit(self, X, y, sample_weight=None):
        if np.any(y <= 0):
            raise ValueError("All target values must be positive!")
        
        y_log = np.log(y)
        
        super().fit(X, y_log, sample_weight=sample_weight)

        return self
    
    
    def predict(self, X):
        y_log_pred = super().predict(X)
        
        y_exp = np.exp(y_log_pred)

        return y_exp