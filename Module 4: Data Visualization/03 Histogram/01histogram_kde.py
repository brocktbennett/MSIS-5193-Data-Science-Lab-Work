# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Setting the visual style for the plots
sns.set_style('darkgrid')

# Load loan data into a dataframe
loan = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/train_Loan.csv")
# Plotting a histogram with Kernel Density Estimation (KDE) for LoanAmount
sns.displot(loan['LoanAmount'], kde=True)
plt.show()

# Load stock data (for Apple) into a dataframe
stockapp = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/apple_stock_prices_2022.csv")
# Plotting a histogram using two variables: Open and Close price with KDE
sns.histplot(data=stockapp, x="Open", label="Open", kde=True)
sns.histplot(data=stockapp, x="Close", color="red", label="Close", kde=True)
# Adding a legend to differentiate between Open and Close prices
plt.legend()
plt.show()
