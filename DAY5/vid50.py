#print('Hello world')
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
student_scores.sort()
print('The highest score in the class is:' , student_scores[-1])