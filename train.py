# %% [code] {"jupyter":{"outputs_hidden":false}}

import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction import DictVectorizer

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score


#parameters

output_file = 'model.bin'
n_splits = 5


#data preparation

df = pd.read_csv('/kaggle/input/loan-approval-classification-data/loan_data.csv')

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.lower()

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

categorical = list(df.dtypes[df.dtypes == 'object'].index)
numerical = ['person_age', 'person_income', 'person_emp_exp',
             'loan_amnt', 'loan_int_rate', 'loan_percent_income', 
             'cb_person_cred_hist_length','credit_score']


#training

def train(df_train, y_train):
    dicts = df_train[categorical + numerical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model= RandomForestClassifier(
        n_estimators=22,
        max_depth=11,
        min_samples_split=8,
        min_samples_leaf=2,
        random_state=42)
    
    model.fit(X_train, y_train)
    
    return dv, model


def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X = dv.transform(dicts)
    y_prob = model.predict_proba(X)[:, 1]
    y_pred = model.predict(X)

    return y_prob, y_pred


# validation

print('Doing validation')

kfold = KFold(n_splits=n_splits, shuffle=True, random_state=42)

scores = []

fold = 0

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.loan_status.values
    y_val = df_val.loan_status.values

    dv, model = train(df_train, y_train, C=C)
    y_prob = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_prob)
    scores.append(auc)

    print(f'auc on fold {fold} is {auc}')
    fold = fold + 1

print('validation results:')
print('C=%s %.3f +- %.3f' % (C, np.mean(scores), np.std(scores)))


# training the final model

print('Training the final model')
dv, model = train(df_full_train, df_full_train.loan_status.values)
y_prob, y_pred = predict(df_test, dv, model)

y_test = df_test.loan_status.values
auc = roc_auc_score(y_test, y_prob)
accuracy = accuracy_score(y_test, y_pred)

print(f'AUC: {auc}, Accuracy: {accuracy}')


# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')