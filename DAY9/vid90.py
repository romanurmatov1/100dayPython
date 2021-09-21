#print('Hello world')
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
};
student_grades = {}

for i in student_scores:
   Grade = i 
   student_grades[Grade] = student_scores[i]
   if 90 < student_scores[i] <= 100:
      student_grades[Grade] = 'Outstanding'
   elif  80 < student_scores[i] <= 90:
      student_grades[Grade] = 'Exceeds Expectations'
   elif 70 < student_scores[i] <= 80:
      student_grades[Grade] = 'Acceptable'
   elif student_scores[i]<=70:
      student_grades[Grade] = 'Fail'
print(student_grades)