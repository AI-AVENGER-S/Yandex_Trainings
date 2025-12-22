import numpy as np

def root_mean_squared_logarithmic_error(y_true, y_pred, a_min=1.):
    if np.any(y_true < 0):
        raise ValueError("y_true содержит отрицательные значения!")
    
    y_pred_corrected = np.maximum(y_pred, a_min)
    

    rmsle = np.sqrt(
        np.mean(
            (np.log(y_true) - np.log(y_pred_corrected)) ** 2
        )
    )
    
    return rmsle
    