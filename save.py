import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
data = pd.read_csv('csv/learnmap.csv')
X = data[['skill', 'level', 'style', 'time', 'requirement', 'access', 'age', 'gender', 'goal']]
y = data['outcome']
label_encoders = {}
for col in X.columns:
    if X[col].dtype == 'object':
        label_encoders[col] = LabelEncoder()
        X[col] = label_encoders[col].fit_transform(X[col])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
joblib.dump(model, 'decision_tree_model.joblib')
for col, le in label_encoders.items():
    joblib.dump(le, f'label_encoder_{col}.joblib')
