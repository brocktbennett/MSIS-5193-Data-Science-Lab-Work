import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing
# load data
loan = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/train_Loan.csv")
# fill missing values
loan[['ApplicantIncome']] = loan[['ApplicantIncome']].fillna(method='ffill')
loan[['LoanAmount']] = loan[['LoanAmount']].fillna(method='ffill')
# normalize data
scaler = preprocessing.MinMaxScaler()
loan[['LoanAmount']] = scaler.fit_transform(loan[['LoanAmount']])
loan[['ApplicantIncome']] = scaler.fit_transform(loan[['ApplicantIncome']])
# plot charts
plt.plot(loan['LoanAmount'])
plt.plot(loan['ApplicantIncome'])
# add title, legend and labels for x-axis, and y-axis
plt.legend(['LoanAmount','ApplicantIncome'])
plt.title('Loan Amount vs. Applicant Income')
plt.xlabel('')
plt.ylabel('$')
# show figure
plt.show()
