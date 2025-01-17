from sklearn.model_selection import train_test_split
from IrisFlower.dataloading import df
# Define features and target variable
X = df.drop('species', axis=1)
y = df['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
