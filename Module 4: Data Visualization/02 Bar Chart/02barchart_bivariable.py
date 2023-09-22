# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Main program entry point
if __name__ == "__main__":
    # Load the dataset into a DataFrame, encoding set to 'latin-1' to handle special characters
    df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/Summer-Olympic-medals-1976-to-2008.csv", encoding='latin-1')

    # Identify the top 10 countries with the most medals
    top_countries = df.Country.value_counts().iloc[:10].index

    # Create a countplot to show the gender distribution of medals for the top 10 countries
    sns.countplot(x="Country", hue="Gender", data=df, order=top_countries)

    # Display the countplot
    plt.show()

    # Create a Seaborn catplot to show the gender distribution of medals for the top 10 countries
    # Here, we use a vertical layout for a different view
    sns.catplot(kind="count", y="Country", hue="Gender", data=df, order=top_countries)

    # Display the catplot
    plt.show()
