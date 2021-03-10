student_list = ["Eren Bağcı","Melih Sefir","Edvin Zalzonaldo","Tayfun Lüfer"]
courses = ["Math","Physics","Algorithm and Programming","General Chemistry","Expository reading and writing","Statistics"]

def letter_grade():
    
    courses_input = input("\nWhich lessons do you want to take in: ")
    course_list = list(courses_input.split(","))
    
    if len(course_list) >= 3 and len(course_list) <= 5:
        
        for i in course_list:
            if i not in courses:
                return print("There is no lesson like that")
        
        course = input("Please enter the lesson's name to see your grade: ")
        
        if course in course_list:
            
            grades = {"midterm":0,"final":0,"project":0}
            
            midterm = int(input("\nEnter your midterm grade: "))
            grades["midterm"] = midterm
            final = int(input("Enter your final grade: "))
            grades["final"] = final
            project = int(input("Enter your project grade: "))
            grades["project"] = project
            
            grade = (midterm*30 + final*50 + project*20)/100
            
            if grade >= 90:
                return print("\nYour grade is AA.","you passed the lesson")
            if grade >= 70 and grade < 90:
                return print("\nYour grade is BB.","you passed the lesson")
            if grade >= 50 and grade < 70:
                return print("\nYour grade is CC.","you passed the lesson")
            if grade >= 30 and grade < 50:
                return print("\nYour grade is DD.","you passed the lesson")
            else:
                return print("\nYour grade is FF.",'You have failed')
                ('You have failed')  
        
        if course not in course_list and course in courses:
            return print("\nYou can't take this course.")
        
        else:
            return print("\nThis course does not exist in your class.")
        
    else:
        return print("\nYou must take at least 3 and at most 5 courses.")


for i in range(4):
    
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    
    student_info = name + " " + surname
    
    if student_info in student_list:
        
        print("\n",student_info,",","Welcome to student management system")
        letter_grade()
        break
    
    if i <= 2:
        
        print("Login is failed\n")
    
    else:
        
        print("Please try again")