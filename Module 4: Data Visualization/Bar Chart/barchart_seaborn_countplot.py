# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Main program entry point
if __name__ == "__main__":
    # Load the dataset into a DataFrame
    # Encoding is set to 'latin-1' to handle special characters
    df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/Summer-Olympic-medals-1976-to-2008.csv", encoding='latin-1')

    # Display the list of countries in the DataFrame
    print("List of countries in the dataset:")
    print(df.Country)

    # Identify the top 10 countries with the most medals
    top_countries = df.Country.value_counts().iloc[:10].index

    # Create a countplot to show the number of medals for the top 10 countries
    # Use 'order' parameter to sort the countries based on their medal counts
    sns.countplot(x="Country", data=df, order=top_countries)

    # Show the plot
    plt.show()
