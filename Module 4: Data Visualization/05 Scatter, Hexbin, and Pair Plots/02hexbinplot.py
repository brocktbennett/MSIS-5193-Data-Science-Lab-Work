import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/apple_stock_prices_2022.csv")

# Scatter plot
plt.scatter(df['Close'], df['Open'])
plt.title('Scatter plot')
plt.xlabel('Close')
plt.ylabel('Open')
plt.show()

# Hexbin plot
df.plot.hexbin(x='Close', y='Open', gridsize=20)
plt.title('Hexbin plot')
plt.xlabel('Close')
plt.ylabel('Open')
plt.show()
