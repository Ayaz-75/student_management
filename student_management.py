

school=["Ayaz"]
print("1- Add student")
print("2- Update student")
print("3- Delete student")
print("4- See final students in School")




def add_student():
    new_student_add=input("Enter student's name to be added in school: ")
    school.append(new_student_add)
    print("Students in School are: ",school)




def update_student():
    chech_student=input("Enter the name of student to check either he is in or not: ")
    if chech_student in school:
        new_student=input("Enter the new stusents name to replace previous with: ")
        previous_students_position=school.index(chech_student)
        school.insert(previous_students_position,new_student)
        
        school.remove(chech_student)
        print(chech_student," is replaced with: ",new_student)
        #print("Students in school are:",)


def delete_student():
    check_existing=input("Enter students name to check weather he is in school or not: ")
    if check_existing in school:
        print(check_existing," is present in school do you want to kick him out ? ")
        choose=input("choose y for yes nd n for no: ")
        if choose=="y":
            school.remove(check_existing)
            print(check_existing," is now kicked out from school")
        else:
            print("I don't want to kick out him")



condition=True
while condition:
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_student()
    elif choice==2:
        update_student()
    elif choice==3:
        delete_student()
    elif choice==4:
        print(school)
    else:
        print("invalid Selection")
