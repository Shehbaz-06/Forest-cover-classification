#1. Always import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

#2. Load the dataset
forest_data = pd.read_csv("covertype.csv")

#3. Investigate the data
print(f"These are the stats of the data {forest_data.info()}")
print(f"This is the shape of the data {forest_data.describe()}")
print(f"These are the sum of all null{forest_data.isnull().sum()}")
# This drops rows with missing values
forest_data.dropna(inplace=True)
forest_data = forest_data.loc[:, ~forest_data.columns.str.contains('^Unnamed')]

print("This is the dataset after dropping the values:")

# For Encoding categorical columns
forest_data=pd.get_dummies(forest_data,drop_first=True)

#4. Split into features (X) and target (y)
X = forest_data.drop(columns=["Cover_Type"])
y = forest_data["Cover_Type"] # Target variable

#5. Split into features (X) and target (y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#6. Training the decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)

#7. Evaluating the model
y_pred= model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"Model accuracy: {accuracy*100:.2f}%")

#8. Visualizing confusion matrix and feature importance
# Confuison Matrix with Labels
forest_types = [
  'Spruce-Fir',
  'Lodgepole Pine',
  'Ponderosa Pine',
  'Cottonwood/Willow',
  'Aspen',
  'Douglas-fir',
  'Krumholz'
]
# For Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=forest_types)
disp.plot(cmap="Blues")
plt.title("Confusion Matrix Forest Cover Type Classification")
plt.tight_layout()
plt.show()

# Feature Importance (with names)
importances = model.feature_importances_
feature_importance = pd.Series(importances, index=X.columns).sort_values(ascending=False)[:10]
feature_importance.plot(kind='barh', color='teal')
plt.title("Top 10 Important Features")
plt.xlabel("Importance Score")
plt.ylabel("Feature Name")
plt.tight_layout()
plt.show()
