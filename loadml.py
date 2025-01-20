from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('decision_tree_model.joblib')

label_encoders = {}
for col in ['skill', 'level', 'style', 'time', 'requirement', 'access', 'age', 'gender', 'goal']:
    try:
        label_encoders[col] = joblib.load(f'label_encoder_{col}.joblib')
    except FileNotFoundError:
        pass

def process_input(skill, level, style, time, requirement, access, age, gender, goal):
    return pd.DataFrame([[skill, level, style, time, requirement, access, age, gender, goal]],
                        columns=['skill', 'level', 'style', 'time', 'requirement', 'access', 'age', 'gender', 'goal'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        skill = request.form['skill']
        level = request.form['level']
        style = request.form['style']
        time = request.form['time']
        requirement = request.form['requirement']
        requirement = 1 if requirement.lower() == 'yes' else 0
        access = request.form['access']
        access = 1 if access.lower() == 'yes' else 0
        age = request.form['age']
        gender = request.form['gender']
        goal = request.form['goal']

        user_input = process_input(skill, level, style, time, requirement, access, age, gender, goal)
        for col in user_input.columns:
            if user_input[col].dtype == 'object' and col in label_encoders:
                user_input[col] = label_encoders[col].transform(user_input[col])

        prediction = model.predict(user_input)
        n = ['possibility', 'approach', 'motive', 'challenges', 'necessary_things']
        output = prediction[0].split('/')
        result = {n[i]: output[i] for i in range(1,len(n))}

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
