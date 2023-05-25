from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.random.rand(100, 5)
y = np.random.randint(0, 5, (100,))
# print(y)

# Assuming you have your feature matrix X and target variable y

# Create a random forest classifier
rf_classifier = RandomForestClassifier()

# Train the random forest classifier
rf_classifier.fit(X, y)

# Get the feature importances
feature_importances = rf_classifier.feature_importances_
print(feature_importances)

# # Get the indices of features sorted by their importance score in descending order
sorted_indices = np.argsort(feature_importances)[::-1]
print(sorted_indices)

# Print the feature importance ranking
print("Feature Importance Ranking:")
for i, index in enumerate(sorted_indices):
    print(
        f"{i+1}. Feature {index}: Importance Score = {feature_importances[index]}")
