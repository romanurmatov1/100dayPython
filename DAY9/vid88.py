#print('Hello world')
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
};

student_grades = {}

for score in student_scores:

  grade = score
  student_grades[grade] = student_scores[score]

  if student_grades[grade] > 90:
    student_grades[grade] = "Outstanding"
  elif student_grades[grade] > 80:
    student_grades[grade] = "Exceeds Expectations"
  elif student_grades[grade] > 70:
    student_grades[grade] = "Acceptable"
  elif student_grades[grade] <= 70 :
    student_grades[grade] = "Fail"


print(student_grades)