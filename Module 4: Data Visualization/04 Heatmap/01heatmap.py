# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Loading and displaying the built-in 'flights' dataset from seaborn library
flights = sns.load_dataset("flights")
print(flights.head())  # display only first few rows for clarity

# Pivot the dataset to reformat for heatmap visualization:
# - Rows represent months
# - Columns represent years
# - Values represent passengers count
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# Visualize the pivoted dataset using a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(flights_pivot, annot=True, cmap='viridis')
plt.title("Heatmap of Flight Data")
plt.show()

# Loading custom sales data from a CSV file
sales = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/sales_data_with_stores.csv")

# Aggregate the sales data:
# - Group by 'store' and 'product_group'
# - Calculate average of 'last_week_sales' for each group
# - Sort by average sales in descending order
sales_aggregated = sales.groupby(["store", "product_group"], as_index=False).agg(
    avg_sales=("last_week_sales", "mean")
).sort_values(by="avg_sales", ascending=False)

# Pivot the aggregated sales data to reformat for heatmap visualization:
# - Rows represent stores
# - Columns represent product groups
# - Values represent average sales
sales_pivot = sales_aggregated.pivot(index="store", columns="product_group", values="avg_sales")

# Visualize the pivoted sales data using a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(sales_pivot, annot=True, cmap='RdYlGn', linewidths=0.30)
plt.title("Sales Heatmap")
plt.show()
