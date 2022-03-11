import pandas as pd

student = pd.DataFrame([['leela', 1], ['renu', 2], ['amu', 3]], columns=['Name', 'rollnumber'])

# convert items to csv file
student.to_csv("mystudent.csv")