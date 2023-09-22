# Import required libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# Function to perform systematic sampling on a data frame
def systematic_sampling(df, step):
    """
    Performs systematic sampling on a data frame.

    Parameters:
        df (DataFrame): The input data frame to be sampled.
        step (int): The sampling interval.

    Returns:
        DataFrame: The sampled data frame.
    """
    # Get the indices of the sampling data
    indexes = np.arange(0, len(df), step=step)

    # Get the subset based on the indices
    systematic_sample = df.iloc[indexes]

    # Return the sampled data frame
    return systematic_sample


# Main program
if __name__ == "__main__":
    # Load data into DataFrame
    price = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/prod_prices.csv")

    # Perform data sampling
    pricenew = systematic_sampling(price, 5)

    # Impute missing data in the 'price' column
    pricenew.loc[:, 'price'] = pricenew['price'].fillna(method='ffill')

    # Plotting
    # Create a plot of 'price' against 'Date'
    plt.plot(pricenew['Date'], pricenew['price'])

    # Customize the plot
    plt.xticks(fontsize=10)

    # Display the plot
    plt.show()
