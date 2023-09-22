import matplotlib.pyplot as plt
import pandas as pd

# Load the data with the specified encoding
data_path = "/Users/brocktbennett/GitHub/Project Data/Summer-Olympic-medals-1976-to-2008.csv"
df = pd.read_csv(data_path, encoding='latin-1')

# 1. Breakdown of medal types for the top countries
def medal_breakdown(df, top_n=10):
    print("\n=== Medal Breakdown for Top Countries ===")
    top_countries = df['Country'].value_counts().index[:top_n]
    medal_counts = df[df['Country'].isin(top_countries)].groupby(['Country', 'Medal']).size().unstack().fillna(0)
    medal_counts.plot(kind='bar', stacked=True)
    plt.title('Medal Breakdown for Top Countries')
    plt.ylabel('Number of Medals')
    plt.xlabel('Country')
    plt.xticks(rotation=45)
    plt.show()

medal_breakdown(df)

# 2. Medals progression for selected countries over the years
def medal_progression(df, countries):
    print("\n=== Medal Progression Over the Years ===")
    progression = df[df['Country'].isin(countries)].groupby(['Year', 'Country']).size().unstack().fillna(0)
    progression.plot()
    plt.title('Medal Progression Over the Years')
    plt.ylabel('Number of Medals')
    plt.xlabel('Year')
    plt.show()

countries = ['United States', 'Soviet Union', 'Australia']
medal_progression(df, countries)

# 3. Male vs. Female medal winners for top countries
def gender_comparison(df, top_n=10):
    print("\n=== Male vs Female Medal Winners for Top Countries ===")
    top_countries = df['Country'].value_counts().index[:top_n]
    gender_counts = df[df['Country'].isin(top_countries)].groupby(['Country', 'Gender']).size().unstack().fillna(0)
    gender_counts.plot(kind='bar', stacked=True)
    plt.title('Male vs Female Medal Winners for Top Countries')
    plt.ylabel('Number of Medals')
    plt.xlabel('Country')
    plt.xticks(rotation=45)
    plt.show()

gender_comparison(df)

# 4. Top sports for a selected country
def top_sports(df, country, top_n=5):
    print(f"\n=== Top {top_n} Sports for {country} ===")
    sports = df[df['Country'] == country]['Sport'].value_counts()[:top_n]
    sports.plot(kind='bar', color='green', edgecolor='black')
    plt.title(f'Top {top_n} Sports for {country}')
    plt.ylabel('Number of Medals')
    plt.xlabel('Sport')
    plt.xticks(rotation=45)
    plt.show()

top_sports(df, 'United States')
