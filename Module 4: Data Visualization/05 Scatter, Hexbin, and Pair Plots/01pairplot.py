# Importing necessary libraries
import seaborn as sns  # Renamed 'seaborn' to the more conventional 'sns'
import matplotlib.pyplot as plt
import pandas as pd

# Loading the built-in 'tips' dataset using seaborn
tips_df = sns.load_dataset('tips')

# Visualizing relationships between numerical columns using pairplots
# Basic pairplot
sns.pairplot(tips_df)
plt.suptitle('Pairplot of Tips Dataset', y=1.02)  # Adding a title
plt.show()

# Pairplot with color differentiation ('hue') based on 'sex'
sns.pairplot(tips_df, hue='sex')
plt.suptitle('Pairplot of Tips Dataset (Colored by Sex)', y=1.02)  # Adding a title
plt.show()

# Loading custom sales data from a CSV file
sales_df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/sales_data_with_stores.csv")

# Removing 'last_week_sales' and 'last_month_sales' columns
# Note: It's a good practice to preserve the original data, hence not overwriting 'sales_df'
sales_df_reduced = sales_df.drop(['last_week_sales', 'last_month_sales'], axis=1)

# Visualizing relationships between numerical columns using pairplots
# Pairplot with color differentiation ('hue') based on 'store'
sns.pairplot(sales_df_reduced, hue='store')
plt.suptitle('Pairplot of Sales Data (Colored by Store)', y=1.02)  # Adding a title
plt.show()
