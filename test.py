import requests

url = 'http://localhost:9696/predict'

applicant = {'person_gender': 'male',
     'person_education': 'master',
     'person_home_ownership': 'own',
     'loan_intent': 'personal',
     'previous_loan_defaults_on_file': 'yes',
     'person_age': 25.0,
     'person_income': 85320.0,
     'person_emp_exp': 2,
     'loan_amnt': 4000.0,
     'loan_int_rate': 7.42,
     'loan_percent_income': 0.05,
     'cb_person_cred_hist_length': 2.0,
     'credit_score': 709}

response = requests.post(url,json=applicant).json()

print(response)

if response['loan_status'] == 1:
    print('Applicant can be granted loan')

else:
    print('Loan Rejected')