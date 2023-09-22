import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset 'tips'
tips = sns.load_dataset('tips')
print(tips.head())  # Print only the first few rows for a quick view

# Scatter plot: Day vs. Total Bill
plt.scatter(tips['day'], tips['total_bill'])
plt.title('Scatter plot: Day vs. Total Bill')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()
