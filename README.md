# Impact of Study Hours and Parental Support on Academic Performance

<p align = 'justify'>
  This project explores the relationship between study hours per week, levels of parental support, and student performance. By utilizing regression analysis,
the project aims to identify the strength of these relationships and provide actionable insights for educators. An interactive dashboard is included to visualize
the correlations and help educators make informed decisions to improve student outcomes.
</p>

## Project Overview
<p align = 'justify'>
The goal of this project is to analyze how study hours and parental support impact students' academic performance. We leverage machine learning techniques to perform
regression analysis, providing educators with insights on how these factors correlate with student success. The interactive dashboard allows users to explore these
relationships dynamically.
</p>

## Data Description

The dataset used in this project includes the following features:
- **Study Hours per Week:** The number of hours students spend studying each week.
- **Parental Support:** Levels of parental support categorized as low, medium, and high.
- **Previous Grade:** Measured through student grades or standardized test scores.
- **Extra Curricular Activities:** The number of ECA participated by the students.
- **Attendance:** The percentage of classes attended by the student.

The data is preprocessed and split into training and testing sets for regression analysis.

## Installation

Follow these steps to set up the project:

1. **Create Virtual Environment**
    ```bash
    python -m venv venv
    ```
2. **Activate Virtual Enviroment**
    - On windows
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run Application**
    ```bash
    python app.py
    ```


Readme info

Usage: 
  When the user submits the form, the form fields are sent as request text to the API. Then the API predicts the academic performance and returns the response/ prediction for the provided features.

  For running the frontend script, first open the main directory and then navigate to frontend folder then open the index.html file by double click on it.

  For running the backend, open the main directory in command line, then activate the virtual environment, then type uvicorn api:app --reload. If uvicorn is not installed install uvicorn by typing pip install uvicorn. For all of this to work the virtual environment should be properly setup.

    
