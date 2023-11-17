# Importing the Libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Read the csv file into a dataframe
groceries_df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/Data Science Programming Data/GroceryStore.csv", header=None)

# Get the shape of the dataframe to understand the dataset's size
print("Size of table: ", groceries_df.shape)
print("No of Transactions: ", groceries_df.shape[0])
print("No of items: ", groceries_df.shape[1])

# Fill the missing value with 0 for uniformity
groceries_df.fillna(0, inplace=True)

# Initialize an empty set to get all unique products
all_products = set()

# Finding all the unique products across all transactions
for index, row in groceries_df.iterrows():
    # Update the set with unique items from each transaction
    all_products.update(row)

# Reference for the update method: https://www.w3schools.com/python/ref_set_update.asp
print("Count of products: ", len(all_products))
print("Products: ", all_products)

# Remove the placeholder '0' from the product list, as it's not a product
all_products.remove(0)
print("Count of products: ", len(all_products))
print("Products: ", all_products)

# One Hot Encoding to prepare the data for association rule mining
encoded_vals = []

# Iterate through each transaction to convert product presence into binary format
for index, row in groceries_df.iterrows():
    # Initialize all products as not present (0) for the current transaction
    rowset = {item: 0 for item in all_products}

    # Set the value to 1 for products present in the current transaction
    rowset.update({item: 1 for item in row if item != 0})

    # Add the encoded transaction to the list
    encoded_vals.append(rowset)

# Convert the list of encoded transactions into a dataframe
encoded_vals_df = pd.DataFrame(encoded_vals)
print(encoded_vals_df)

# Generate frequent itemsets with a minimum support threshold
freq_items = apriori(encoded_vals_df, min_support=0.3, use_colnames=True)

# Generate association rules from frequent itemsets with a minimum confidence threshold
rules = association_rules(freq_items, metric="confidence", min_threshold=0.9)

# Filter the resulting rules for easier analysis
rules = rules[['antecedents', 'consequents', 'support', 'confidence']]

# Sort and display the top 20 rules by confidence and support
pd.set_option('display.max_columns', None)
print(rules.sort_values(["confidence", "support"], ascending=[False, False]).reset_index(drop=True).head(20))
