# writing to a file
employee_file=open("employees.text","w")
# write the file
employee_file.write("toby - human resources\n")
employee_file.write("keven - customer service\n")
employee_file.write("abel - computer science\n")
employee_file.write("bati -software engineering\n")
employee_file.write("beti - electerical ebgineering\n")
employee_file.close()
# reading the employees file
employee_file=open("employees.text","r")
print(employee_file.readlines())
employee_file.close()
# using for loop
employee_file=open("employees.text","r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
# append to the file
employee_file=open("employees.text","a")
employee_file.write("benti -physics\n")
employee_file.close()
# how to creat a new file
html_file=open("index.html","w")
# writing to a file
html_file.write("<h1>WELCOME TO HTML SITE</h1> >") 
html_file.write("<h2> hello world; welcome to the html file</h2>")
html_file.write("<p> this is a paragraph HTML provides the basic framework</p>")

employee_file.close()
# how to create a new file of students with their id 
student_file=open("students.text","w")
student_file.write("bati - 1234\n")
student_file.write("bekele - 1235\n")
student_file.write("demo -12346\n")
student_file.write("deme - 12347\n")
student_file.write("demeke - 12348\n")
student_file.close()
# how to read the student file
student_file=open("students.text","r")
for student in student_file.readlines():
    print(student)
student_file.close()
# how to APPEND to the student file
student_file=open("students.text","a")
student_file.write("benti - 12349\n")
student_file.close()
print("you are done with the file reading , writing and appending!!!!\n"+"GOOD JOP!!!")












