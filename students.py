import pandas as pd

students = pd.DataFrame({'Name': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'],
                        'Genre': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'],
                         'Age': [15, 27, 56, 32, 42, 21, 19, 35],
                         'Grades': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6],
                         'Approved': [True, False, False, True, True, True, False, False]},
                        columns=['Name', 'Age', 'Genre', 'Grades', 'Approved'])
print(students.head(10))

selection = students['Approved'] == True
approved = students[selection]
print(approved.head(10))

selection2 = (students.Approved == True) & (students.Genre == 'F')
approvedF = students[selection2]
print(approvedF.head(10))

selection3 = ((students.Age > 10) & (students.Age < 20)) | (students.Age >= 40)
print(students[selection3])

selection4 = students['Approved'] == False
not_approved = students.loc[selection4, ['Name', 'Genre', 'Age']]
print(not_approved.head(10))

option2_selection4 = students['Approved'] == False
not_approved2 = students[['Name', 'Genre', 'Age']][option2_selection4]
print(not_approved2.head(10))
