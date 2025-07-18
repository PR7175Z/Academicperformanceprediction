from faker import Faker
import pandas as pd
import numpy as np
import os

# creating dataGenerator as module

def dataGenerator(filename, count=1000, seed_num=42):
    fake = Faker()
    num_samples = count
    np.random.seed(seed_num)  # For reproducibility

    data = {
        'StudentID': [i for i in range(num_samples)],
        'Name': [fake.name() for _ in range(num_samples)],
        'Gender': [fake.random_element(elements=("Male", "Female"))
        for _ in range(num_samples)],
    }

    # Generate Parental Support (categorical)
    data['ParentalSupport'] = [
        fake.random_element(elements=("High", "Medium", "Low"))
        for _ in range(num_samples)
    ]

    # Generate Previous Grade (based on parental support and some randomness)
    data['PreviousGrade'] = [
        np.clip(np.random.normal(loc=85 if ps == 'High'
            else 75 if ps == 'Medium'  
            else 50, scale=5), 0, 99)
        for ps in data['ParentalSupport']
    ]

    # Generate Study Hours Per Week (dependent on parental support and previous grade)
    data['StudyHoursPerWeek'] = [
        np.clip(np.random.normal(loc=25 
            if ps == 'High' 
            else 18 if ps == 'Medium' 
            else 12, scale=5), 0, 36)
        for ps in data['ParentalSupport']
    ]

    # Generate Attendance Rate (influenced by parental support and extracurricular activities)
    data['ExtracurricularActivities'] = [fake.random_int(min=0, max=5) for _ in range(num_samples)]
    data['AttendanceRate'] = [
        np.clip(np.random.normal(loc=80 
            if ps == 'High' 
            else 70 if ps == 'Medium' 
            else 55, scale=10) - 2*act, 50, 100)
        for ps, act in zip(data['ParentalSupport'], data['ExtracurricularActivities'])
    ]

    # Generate Final Grade (based on all the above factors)
    final_grades = []
    for i in range(num_samples):
        # Base final grade influenced by previous grade
        base_grade = data['PreviousGrade'][i] * 0.4
        
        # Study hours influence
        study_hours_influence = data['StudyHoursPerWeek'][i] * 1.2
        
        # Attendance influence
        attendance_influence = data['AttendanceRate'][i] * 0.3
        
        # Extracurricular influence (small positive or negative effect depending on how it balances study)
        extracurricular_influence = -data['ExtracurricularActivities'][i] * 0.5 + 5
        
        # Parental support influence
        parental_support_influence = {
            'High': 10,
            'Medium': 5,
            'Low': 0
        }[data['ParentalSupport'][i]]
        
        # Random noise
        noise = np.random.normal(0, 5)
        
        # Final grade calculation
        final_grade = (base_grade + study_hours_influence + attendance_influence + 
                    extracurricular_influence + parental_support_influence + noise)
        
        # Clip final grade to realistic range [0, 100]
        final_grade = np.clip(final_grade, 0, 99)
        
        final_grades.append(final_grade)

    # Add Final Grades to the dataset
    data['FinalGrade'] = final_grades

    # Convert to DataFrame
    df = pd.DataFrame(data)
    print('Data Generated')

    

    # data_dir = '../data'
    # if not os.path.exists(data_dir):
    #     os.makedirs(data_dir)

    # print("Trying to save to:", os.path.abspath(data_dir))
    df.to_csv(f'data/{filename}.csv', index=False)