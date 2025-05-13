students_marks={'Shashwat':'90', 'Shashank':'95', 'Shivam':'99',}
students_name= input("Enter student's name -")
if students_name in students_marks:
    print(students_name + "'s marks are ", students_marks[students_name])
else:
    print(students_name,"'s details not found")