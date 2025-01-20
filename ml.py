import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = pd.read_csv('csv/learnmap.csv')
X = data[['skill', 'level', 'style', 'time', 'requirement', 'access', 'age', 'gender', 'goal']]
y = data['outcome']

label_encoders = {}
for col in X.columns:
    if X[col].dtype == 'object':
        label_encoders[col] = LabelEncoder()
        X.loc[:, col] = label_encoders[col].fit_transform(X.loc[:, col])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

def process_input(skill, level, style, time, requirement, access, age, gender, goal):
    return pd.DataFrame([[skill, level, style, time, requirement, access, age, gender, goal]],
                         columns=['skill', 'level', 'style', 'time', 'requirement', 'access', 'age', 'gender', 'goal'])

skill = input("Enter skill: ")
level = input("Enter level: ")
if level == 'beginner':
    level = '1'
elif level == 'intermediate':
    level = '2'
elif level == 'advanced':
    level = '3'
style = input("Enter style: ")
time = input("Enter available time (hours/week): ")
requirement = input("Enter requirement (do you have requirements?): ")
requirement = 1 if requirement.lower() == 'yes' else 0
access = input("Enter access (do you have access to books, mentor ,internet and etc.?):")
access = 1 if access.lower() == 'yes' else 0
age = input("Enter age: ")
gender = input("Enter gender: ")
goal = input("Enter goal: ")

user_input = process_input(skill, level, style, time, requirement, access, age, gender, goal)

for col in user_input.columns:
    if user_input[col].dtype == 'object':
        if col not in label_encoders:
            continue
        user_input.loc[:, col] = label_encoders[col].transform(user_input.loc[:, col])
print("OUTCOME:\n")
prediction = model.predict(user_input)
n=['possibility','approach','motive','challenges','necessary_things']
output=prediction[0].split('/')
for i in range(1,5):
    print(n[i]+" = "+output[i])
thershold=100.0
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)*thershold
print("\n")
print(f"Accuracy: {accuracy}%")
