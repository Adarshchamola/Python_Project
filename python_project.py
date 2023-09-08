import pandas as pd

# Load the dataset
df = pd.read_excel('pythonproject.xlsx')

# Question 1: How many unique students are included in the dataset?
unique_students = df['Email ID'].nunique()
print(f"1. Number of unique students: {unique_students}")

# Question 2: What is the average GPA of the students?
average_gpa = df['CGPA'].mean()
print(f"2. Average GPA of students: {average_gpa:.2f}")

# Question 3: What is the distribution of students across different graduation years?
graduation_distribution = df['Year of Graduation'].value_counts()
print("3. Distribution of students across different graduation years:")
print(graduation_distribution)

# Question 4: What is the distribution of students' experience with Python programming?
python_experience_distribution = df['Experience with python (Months)'].value_counts()
print("4. Distribution of students' experience with Python programming:")
print(python_experience_distribution)

# Question 5: How does the GPA vary among different colleges? (Show top 5 results only)
gpa_by_college = df.groupby('College Name')['CGPA'].mean().nlargest(5)
print("5. GPA by college (Top 5):")
print(gpa_by_college)

# Question 6: Are there any outliers in the 'attending status' & 'quantity (number of courses completed)' attribute?
outliers_status_quantity = df[['Attendee Status', 'Quantity']].describe()
print("6. Outliers in 'Attendee Status' & 'Quantity' attribute:")
print(outliers_status_quantity)

# Question 7: What is the average GPA for students from each city?
average_gpa_by_city = df.groupby('City')['CGPA'].mean()
print("7. Average GPA for students from each city:")
print(average_gpa_by_city)

# Question 8: How does the expected salary vary based on factors like 'GPA', 'Family income', 'Experience with Python (Months)'?
salary_variation = df.groupby(['CGPA', 'Family Income', 'Experience with python (Months)'])['Expected salary (Lac)'].mean()
print("8. Expected salary variation based on GPA, Family Income, and Python Experience:")
print(salary_variation)
