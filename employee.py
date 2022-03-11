import pandas as pd
employee = pd.DataFrame(
    [[1,'leela','BE',30000,'ACE'],
    [2, 'renu', 'BE', 30000, 'ACE'],
    [3, 'amu', 'BE', 30000, 'ACE'],
    [4, 'grini', 'BE', 30000, 'ACE'],
    [5, 'jo', 'BE', 30000, 'ACE']]

    ,columns=['Employee_code','Employee_name','Designation','Salary','Company Name'])

employee.to_csv("myemployee.csv")