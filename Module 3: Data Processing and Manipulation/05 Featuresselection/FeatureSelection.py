# Load libraries
from sklearn.preprocessing import LabelEncoder
import sklearn.feature_selection as fs
import pandas as pd

# Import data
PlayTennis = pd.read_csv('/Users/brocktbennett/GitHub/Project Data/PlayTennis.csv')

# Since the features are not numbers, we need to encode data
Le = LabelEncoder()

# Code columns
PlayTennis['outlook'] = Le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = Le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = Le.fit_transform(PlayTennis['humidity'])
PlayTennis['windy'] = Le.fit_transform(PlayTennis['windy'])
PlayTennis['play'] = Le.fit_transform(PlayTennis['play'])

# Define the target column y, and input columns (features) in X
y = PlayTennis['play']
X = PlayTennis.drop(['play'], axis=1)

# Apply feature selection
res = dict(zip(X.columns, fs.mutual_info_classif(X, y, discrete_features=True)))

# Show ranked features with if-else statements
print("Ranked Features by Mutual Information Score:")
for feature, mi_score in res.items():
    if mi_score >= 0.15:
        print(f"{feature}: {mi_score} - Strong relationship with 'play'.")
    elif mi_score >= 0.1:
        print(f"{feature}: {mi_score} - Moderate relationship with 'play'.")
    else:
        print(f"{feature}: {mi_score} - Weak relationship with 'play'.")
