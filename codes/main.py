#main codes here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle



# with open('../models/model.pkl','rb') as f:
#         model = pickle.load(f)

# data = pd.read_csv('../student_performance.csv')

'''
    Impact of Study Hours and Parental Support on Academic Performance 
    Create an interactive dashboard that visualizes the correlation between
    study hours per week, levels of parental support, and student performance. 
    Use regression analysis to explore the strength of these relationships and
    provide actionable insights for educators.

'''

data = pd.read_csv('data/Student_performance_data.csv')
print(data.head())

features = [   
        'StudentID',
        'Age',
        'Gender',
        'Ethnicity',
        'ParentalEducation',
        'StudyTimeWeekly',
        'Absences',
        'Tutoring',
        'ParentalSupport',
        'Extracurricular',
        'Sports',
        'Music',
        'Volunteering',
        'GPA',
        'GradeClass'
    ]