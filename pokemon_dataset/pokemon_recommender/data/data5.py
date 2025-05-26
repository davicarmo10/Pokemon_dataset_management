import pandas as pd

# Load datasets
pokemon_df = pd.read_csv("train4.csv")
pokemon_df.info()

# Splitting the dataset into features and target variable
y = pokemon_df['Winner']            # Target: 1 if first Pokémon wins, 0 if second wins
X = pokemon_df.drop('Winner', axis=1)  # Features

# Splitting the dataset into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


#Train a Model (Random Forest Classifier)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

#Predict and Evaluate
from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model
import joblib
joblib.dump(model, 'pokemon_RandomForest_model.pkl')
print("Model saved as pokemon_RandomForest_model.pkl")

# Load the model
loaded_model = joblib.load('pokemon_RandomForest_model.pkl')
print("Model loaded from pokemon_RandomForest_model.pkl")

