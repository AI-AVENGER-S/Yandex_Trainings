import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score

print("Скрипт запущен...")

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'
SUBMISSION_FILE = 'answers.csv'

train_df = pd.read_csv(TRAIN_FILE)
test_df = pd.read_csv(TEST_FILE)


TARGET = 'target'
FEATURES = [col for col in train_df.columns if col != TARGET]

for col in FEATURES:
    train_df[col] = pd.to_numeric(train_df[col], errors='coerce')
    test_df[col] = pd.to_numeric(test_df[col], errors='coerce')

X_train = train_df[FEATURES]
y_train = train_df[TARGET]
X_test = test_df[FEATURES] 


pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),  
    ('model', RandomForestClassifier(n_estimators=100,
                                      random_state=42, 
                                      n_jobs=-1)) 
])

pipeline.fit(X_train, y_train)


test_probabilities = pipeline.predict_proba(X_test)[:, 1]

submission_df = pd.DataFrame({
    TARGET: test_probabilities
})

submission_df.to_csv(SUBMISSION_FILE, index=False)