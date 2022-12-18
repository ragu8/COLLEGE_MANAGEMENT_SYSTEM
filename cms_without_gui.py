#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Front_Login():
    print("Admin :")
    print("Teacher :")
    print("Student :")
    Front_Choose = input("Enter : Choose")
    if Front_Choose == "Admin":
        admin_check()
    elif Front_Choose == "Teacher":
        Teacher_check()
    elif Front_Choose == "Student":
        Student_check()
    else:
        return "try again"
    
def admin_check():
    user = input("enter the user_id")
    password = input("enter the password")
    if user == "Admin" and password =="Admin":
        admin_choose()
    else:
        Front_Login()
        
def admin_choose():
    print("Create")
    print("Delete")
    admin_choose = input("Enter : admin_choose")
    if admin_choose == "Create":
        print("Student_Create")
        print("Teacher_Create")
        admin_create_choose = input("Enter : admin_create_choose")
        if admin_create_choose == "Student_Create" :
            Student_Create()
        if admin_create_choose == "Teacher_Create":
            Teacher_Create()
    elif admin_choose == "Delete":
        print("Student_Delete")
        print("Teacher_Delete")
        admin_delete_choose = input("Enter : admin_delete_choose")
        if admin_delete_choose == "Student_delete" :
            Student_Delete()
        if admin_create_choose == "Teacher_delete":
            Teacher_Delete()
            
def Student_Create():
    Reg_NO = int(input("Reg_NO : "))
    Name = input("Name : ")
    Age = int(input("Age : ")) 
    Gender = input("Gender : ")
    Contact_No = int(input("Contact_No : " ))
    dict = {'Reg_NO':[Reg_NO] , 'Name': [Name], 'Age': [Age] , "Gender": [Gender],"Contact_No":[Contact_No]}
    df = pd.DataFrame(dict)
    df.to_csv('student_details.csv', mode='a', index=False, header=False)
    admin_choose()
    
def Teacher_Create():
    Emp_NO = int(input("emp_NO : "))
    Name = input("Name : ")
    Age = int(input("Age : ")) 
    Gender = input("Gender : ")
    Contact_No = int(input("Contact_No : " ))
    dict = {'emp_NO':[Reg_NO] , 'Name': [Name], 'Age': [Age] , "Gender": [Gender],"Contact_No":[Contact_No]}
    df = pd.DataFrame(dict)
    df.to_csv('teacher_details.csv', mode='a', index=False, header=False)
    admin_choose()
    
def Student_Delete():
    student_reg_number = int(input("Enter the student_reg_number : "))
    data = pd.read_csv('student_details.csv')
    data.set_index('Reg_NO', inplace=True)
    data = data.drop(student_reg_number)
    admin_choose()

def Teacher_Delete():
                             
    teacher_emp_number = int(input("Enter the teacher_emp_number : "))
    data = pd.read_csv('teacher_details.csv')
    data.set_index('Emp_NO', inplace=True)
    data = data.drop(teacher_emp_number)
    admin_choose()
    
def Teacher_check():
    data = pd.read_csv('teacher_details.csv')
    val = data["emp_NO"].values
    val = val.tolist()
    Emp_NO =  int(input("enter the Emp_NO"))
    password = int(input("enter the password"))
    if Emp_NO in val and  password in val:
        Teacher_Choice()
    else:
        Front_Login()
        
def Teacher_Choice():
    print("Create")
    print("Modify")
    Teacher_Choice = input("Teacher_Choice : ")
    if Teacher_Choice == "Create":
        Create_mark_list()
    elif Teacher_Choice == "Modify":
        Modify_mark_list()
    else:
        Teacher_Choice()
        
def Create_mark_list():
    Reg_NO = int(input("Reg_NO : "))
    Name = input("Name : ")
    Tamil = int(input("Tamil : ")) 
    English = int(input("English : "))
    Maths = int(input("Maths : " ))
    Physics = int(input("Physics : " ))
    Chemistry = int(input("Chemistry : " ))
    Computer = int(input("Computer : " ))
    Total = Tamil + English + Maths + Physics + Chemistry + Computer
    dict = {'Reg_NO':[Reg_NO] , 'Name': [Name], 'Tamil': [Tamil] , "English": [English],"Maths":[Maths], 'Physics': [Physics] , "Chemistry": [Chemistry],"Computer":[Computer],"Total":Total}
    df.to_csv('student_marks.csv', mode='a', index=False, header=False)
    Teacher_Choice()

def Modify_mark_list():
    data = pd.read_csv('student_marks.csv')
    Reg_NO = int(input("Reg_NO : "))
    subject = input("subject : ")
    marks = int(input("marks : "))
    data = data.loc[(data["Reg_NO"] == Reg_NO)] 
    data[subject] = data[subject].replace(marks)
    data.to_csv("student_marks.csv", index=False)
    Teacher_Choice()
    
def Student_check():
    data = pd.read_csv('student_details.csv')
    val = data["Reg_NO"].values
    val = val.tolist()
    Reg_NO =  int(input("enter the Reg_NO"))
    password = int(input("enter the password"))
    if Emp_NO in val and  password in val:
        Student_Choice()
    else:
        Front_Login()
    
def Student_Choice():
    print("View")
    print("Download")
    Teacher_Choice = input("Teacher_Choice : ")
    if Teacher_Choice == "View":
        View_mark_list()
    elif Teacher_Choice == "Download":
        Download_mark_list()
    else:
        Student_Choice()
        
def View_mark_list():
    data = pd.read_csv('student_marks.csv')
    Reg_NO = int(input("Reg_NO : "))
    data = data.loc[(data["Reg_NO"] == Reg_NO)] 
    print(data)
    
def Download_mark_list():
    data = pd.read_csv('student_marks.csv')
    Reg_NO = int(input("Reg_NO : "))
    data = data.loc[(data["Reg_NO"] == Reg_NO)]
    data.to_csv(f"{Reg_NO}.csv", index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




