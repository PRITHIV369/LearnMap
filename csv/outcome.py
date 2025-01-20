import pandas as pd

def determine_outcome(row):
    skill = row['skill']
    level = row['level']
    style = row['style']
    time = row['time']
    requirement = row['requirement']
    access = row['access']
    age = row['age']
    gender = row['gender']
    goal = row['goal']
    
    if 'survival' in goal.lower():
        if time == '3-5':
            possibility = 'low'
            approach = 'basic cooking classes'
        elif time == '5-8':
            possibility = 'medium'
            approach = 'online tutorials'
        else:
            possibility = 'high'
            approach = 'self-practice'
        motivation = 'self-sufficiency'
        challenges = 'limited ingredients, basic skills'
        necessary_things = 'Basic kitchen tools, Staple ingredients'
        
    elif 'gourmet' in goal.lower():
        if time == '3-5':
            possibility = 'low'
            approach = 'advanced cooking classes'
        elif time == '5-8' or time == '8-11':
            possibility = 'medium'
            approach = 'professional cooking courses'
        else:
            possibility = 'high'
            approach = 'self-practice with professional guidance'
        motivation = 'culinary excellence'
        challenges = 'complex techniques, high-quality ingredients'
        necessary_things = 'Advanced kitchen tools, Specialty ingredients, Recipe books'
        
    elif 'chef' in goal.lower():
        if time == '3-5':
            possibility = 'low'
            approach = 'culinary school'
        elif time == '5-8' or time == '8-11':
            possibility = 'medium'
            approach = 'culinary school, apprenticeships'
        else:
            possibility = 'high'
            approach = 'culinary school with extensive practice'
        motivation = 'professional career'
        challenges = 'high competition, rigorous training'
        necessary_things = 'Culinary school, Professional kitchen tools, Apprenticeships'
        
    else:
        possibility = 'low'
        approach = 'basic cooking classes, online tutorials, self-practice'
        motivation = 'personal'
        challenges = 'lack of clear goals'
        necessary_things = 'Basic kitchen tools, Ingredients'
    
    if age in ['13 below', '60 plus']:
        possibility = 'low'
        challenges = 'age-related limitations'
    
    if level == 3:
        necessary_things += ', advanced courses'
    
    if access == 0 or requirement == 0:
        possibility = 'low'
    
    return f"{possibility} / {approach} / {motivation} / {challenges} / {necessary_things}"

file_path = 'csv/merged_file9.csv'
df = pd.read_csv(file_path)
df['outcome'] = df.apply(determine_outcome, axis=1)
df.to_csv('merged_file_with_outcome4.csv', index=False)
print(df)
