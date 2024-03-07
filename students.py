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
