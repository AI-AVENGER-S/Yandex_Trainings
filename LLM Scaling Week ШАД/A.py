import pandas as pd
import numpy as np
import xgboost as xgb
import json
import warnings

warnings.filterwarnings('ignore')

train_df = pd.read_csv('train_weights.csv')
test_df = pd.read_csv('test_weights.csv')
features = [f'W{i}' for i in range(10)]

X_train = train_df[features]
y_train = train_df['MSE']

X_test = test_df[features]

y_train_log = np.log1p(y_train)

model = xgb.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=1500,
    learning_rate=0.03,
    max_depth=6,          
    subsample=0.8,            
    colsample_bytree=0.8,       
    random_state=42,
    n_jobs=-1           
)

model.fit(X_train, y_train_log)

y_pred_log = model.predict(X_test)

y_pred_mse = np.expm1(y_pred_log)

y_pred_mse = np.maximum(0, y_pred_mse)

results_df = X_test.copy()
results_df['MSE'] = y_pred_mse

answers_list = results_df.to_dict('records')

output_filename = 'answers'
with open(output_filename, 'w') as f:
    json.dump(answers_list, f, indent=4)

print(f"\n[ГОТОВО] Файл '{output_filename}' успешно создан!")