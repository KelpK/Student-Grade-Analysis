"""**Project Question: Sorting Algorithm for Student Grade Analysis**

**Description:**
You are tasked with developing a Python program to manage and analyze student grades. The program should allow users to input student names and their corresponding grades, sort the students based on their grades, and perform various analyses on the data.

**Requirements:**


1. Create a function to input student data. This function should prompt the user to enter the student's name and grade and store this information in a data structure (e.g., dictionary, list of tuples).

2. Implement a function to display the sorted list of students along with their grades. Ensure that the output is clear and organized.

3. Develop functions to perform basic analyses on the student data, such as:
   - Calculate the average grade of all students.
   - aIdentify the highest and lowest grades.
   - Determine the medin grade.
   - Count the number of students who passed (grade >= passing_grade) and failed (grade < passing_grade).
"""

student=[]

# # student2 = student[1]
# # name = student2[0]
# # print(name)

# print(student[1][0])

def infoEnter():
   name=input("Enter student name: ")
   grade=int(input("Enter student grade: "))
   studentInfo=(name,grade)
   student.append(studentInfo)
   print(student)

def sort():
   
   student.sort(key = lambda x : x[1])
   print(student)

def average_grade():
   
   grade=[x[1] for x in student]
   length=len(grade)
   average=sum(grade)/length
   print(f"The average is {average}")

def extreme():
   grade=[x[1] for x in student]
   maxi=max(grade)
   mini=min(grade)
   print(f"The maximum is {maxi} and the minimum is {mini}.")

def pass_grade():
   pass_mark=50
   student_pass=[x[0] for x in student if x[1]>pass_mark]
   student_fail=[x[0] for x in student if x[1]<pass_mark]
   print(f"The students who passed the grade: {student_pass}\nThe students who failed the grade: {student_fail}")

def median():
   grade=[x[1] for x in student]
   grade.sort()
   length=len(grade)
   if length%2==0:
      mi=length//2
      median = (grade[mi] +grade[mi-1])/2
   elif length%2!=0:
      mi = length//2
      median = grade[mi]
   print(f"The median is {median}.")


while True:
   choice = int(input("0 to stop the program\n1 for data entry\n2 for sorting\n3 for average\n4 for max and min marks\n5 for passing and failing students\n6 for median\n: "))
   if choice ==1:
      infoEnter()
   elif choice ==2:
      sort()
   elif choice ==3:
      average_grade()
   elif choice ==4:
      extreme()
   elif choice ==5:
      pass_grade()
   elif choice ==6:
      median()
   elif choice ==0:
      print("thank you for using our software: ")
      break