from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from IrisFlower.preprocessing import label_encoder
from IrisFlower.splittingdata import X_train, X_test, y_train, y_test, X
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Display classification report
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Display confusion matrix
print(confusion_matrix(y_test, y_pred))

# Get feature importances
importances = model.feature_importances_
features = X.columns

# Create a DataFrame for better visualization
feature_importances = pd.DataFrame({'Feature': features, 'Importance': importances})
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importances)
plt.title('Feature Importances')
plt.show()
