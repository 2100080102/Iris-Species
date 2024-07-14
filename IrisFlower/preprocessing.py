from sklearn.preprocessing import LabelEncoder
from IrisFlower.dataloading import df
# Encode the target variable
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

# Display the first few rows of the modified dataset
print(df.head())
