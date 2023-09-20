# Import required libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Define function for systematic sampling
def systematic_sampling(df, step):
    """
    This function performs systematic sampling on a Pandas DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame to sample from.
        step (int): The step size for sampling.

    Returns:
        pd.DataFrame: A new DataFrame containing the sampled data.
    """
    # Calculate the indexes for sampling
    indexes = np.arange(0, len(df), step=step)

    # Use the indexes to get a systematic sample from the DataFrame
    systematic_sample = df.iloc[indexes]

    # Return the sampled DataFrame
    return systematic_sample


# Main execution block
if __name__ == "__main__":
    # Load the data into a Pandas DataFrame
    price = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/prod_prices.csv")

    # Perform systematic sampling on the loaded data
    pricenew = systematic_sampling(price, 5)

    # Impute missing values in the 'price' column using forward fill method
    pricenew.loc[:, 'price'] = pricenew['price'].fillna(method='ffill')

    # Plotting the sampled 'price' data against 'Date'
    plt.plot(pricenew['Date'], pricenew['price'])

    # Customize x-axis tick labels
    plt.xticks(fontsize=10)

    # Display the plot
    plt.show()
