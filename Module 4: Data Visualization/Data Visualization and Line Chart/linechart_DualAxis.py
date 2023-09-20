import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing
# load data
loan = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/train_Loan.csv")
# prepare subplots to enable the creation of dual axis
fig, ax = plt.subplots(figsize=(12,5))
# Create a new Axes with an invisible x-axis and an
# independent y-axis positioned opposite
# to the original one (i.e. at right).
ax2 = ax.twinx()
# add title to the figure, and set the label
# for x-axis as empty
ax.set_title('Applicant Income and Loan Amount')
ax.set_xlabel('')
# plot values, one on ax, the other on ax2
ax.plot(loan['Loan_ID'], loan['ApplicantIncome'], color='green', marker='x')
ax2.plot(loan['Loan_ID'], loan['LoanAmount'], color='red', marker='o')
# plot the labels for ax and ax2
ax.set_ylabel('Applicant Income')
ax2.set_ylabel('Loan Amount')
# add legend to figure
ax.legend(['Applicant Income'])
ax2.legend(['Loan Amount'], loc='upper center')
# remove the xticks to tidy the figure
ax.set_xticks([])
ax2.set_xticks([])
# add a grid to the figure
ax.yaxis.grid(color='lightgray', linestyle='dashed')
# show figure
plt.show()
