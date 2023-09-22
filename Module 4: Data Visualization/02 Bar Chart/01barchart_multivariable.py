# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Main program
if __name__ == "__main__":
    # Load the dataset into a DataFrame
    # Encoding is set to 'latin-1' to handle special characters
    df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/Summer-Olympic-medals-1976-to-2008.csv",
                     encoding='latin-1')

    # Find the top 10 countries with the most medals
    top_countries = df.Country.value_counts().iloc[:10].index

    # Create a Seaborn catplot to visualize the gender distribution of medals for top 10 countries
    # X-axis: Country
    # Y-axis: Year
    # Hue: Gender
    sns.catplot(x="Country",
                y="Year",
                hue="Gender",
                kind="box",
                data=df,
                order=top_countries)

    # Display the plot
    plt.show()
