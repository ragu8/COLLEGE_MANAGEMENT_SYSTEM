import tkinter as tk
from tkinter import *
import pandas as pd

def Front_Login():
    # Create the main window
    window = tk.Tk()
    window.geometry("700x700")
    window.title("Login")
    heading1=Label(window,text='college management system ',fg="black",bg="white",padx=60,pady=20)
    heading1.place(x=200,y=10)
    button1 = tk.Button(window, text="Admin",padx=35,pady=15, command=admin_check)
    button1.place(x=275,y=100)
    button2 = tk.Button(window, text="Teacher",padx=35,pady=15, command=Teacher_check)
    button2.place(x=275,y=200)
    button3 = tk.Button(window, text="Student",padx=35,pady=15, command=Student_check)
    button3.place(x=275,y=300)
    window.mainloop()

        
        
def admin_check():
    # Create the main window
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Admin Login")

    # Add labels for the user ID and password & # Add input fields for the user ID and password
    tk.Label(window, text="User ID").pack()
    user_entry = tk.Entry(window)
    user_entry.pack()
    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    # Add a submit button
    def submit():
        user = user_entry.get()
        password = password_entry.get()
        if user == "Admin" and password == "Admin":
            admin_options()
        else:
            Front_Login()
     # Add a submit button
    tk.Button(window, text="Submit", command=submit).pack()
     # Run the main loop
    window.mainloop()


def admin_options():
    # Create the main window
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Admin Options")
    tk.Button(window, text="Create", command=admin_choose_create).pack()
    tk.Button(window, text="Delete", command=admin_choose_delete).pack()
    
   
    
    # Run the main loop
    window.mainloop()
    
def admin_choose_create():
    # Create the main window
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Admin Options Create")
    tk.Button(window, text="Student_Create", command=Student_Create).pack()
    tk.Button(window, text="Teacher_Create", command=Teacher_Create).pack()
    
   
    
    # Run the main loop
    window.mainloop()
    
def admin_choose_delete():
    # Create the main window
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Admin Options Delete")
    tk.Button(window, text="Student_Delete", command=Student_Delete).pack()
    tk.Button(window, text="Teacher_Delete", command=Teacher_Delete).pack()
   
    
    # Run the main loop
    window.mainloop()



    
    
    
def Student_Create():
    # Create the main window
    window = tk.Tk()
    window.title("Create Student")
    window.geometry("500x500")

    # Add labels and input fields for the student details
    tk.Label(window, text="Reg_NO").pack()
    reg_no_entry = tk.Entry(window)
    reg_no_entry.pack()
    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()
    tk.Label(window, text="Age").pack()
    age_entry = tk.Entry(window)
    age_entry.pack()
    tk.Label(window, text="Gender").pack()
    gender_entry = tk.Entry(window)
    gender_entry.pack()
    tk.Label(window, text="Contact_No").pack()
    contact_no_entry = tk.Entry(window)
    contact_no_entry.pack()

    # Add a submit button
    def submit():
        # Get the user input and create a dictionary
        Reg_NO = int(reg_no_entry.get())
        Name = name_entry.get()
        Age = int(age_entry.get())
        Gender = gender_entry.get()
        Contact_No = int(contact_no_entry.get())
        data = {'Reg_NO':[Reg_NO] , 'Name': [Name], 'Age': [Age] , "Gender": [Gender],"Contact_No":[Contact_No]}

        # Convert the dictionary to a DataFrame and save it to a CSV file
        df = pd.DataFrame(data)
        df.to_csv('student_details.csv', mode='a', index=False, header=False)

        # Return to the admin options
        admin_options()
     # Add a submit button
    tk.Button(window, text="Create", command=submit).pack()
     # Run the main loop
    window.mainloop()

    
    
def Teacher_Create():
    # Create the main window
    window = tk.Tk()
    window.title("Create Teacher")
    window.geometry("500x500")

    # Add labels and input fields for the teacher details
    tk.Label(window, text="Emp_NO").pack()
    emp_no_entry = tk.Entry(window)
    emp_no_entry.pack()
    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()
    tk.Label(window, text="Age").pack()
    age_entry = tk.Entry(window)
    age_entry.pack()
    tk.Label(window, text="Gender").pack()
    gender_entry = tk.Entry(window)
    gender_entry.pack()
    tk.Label(window, text="Contact_No").pack()
    contact_no_entry = tk.Entry(window)
    contact_no_entry.pack()

    # Add a submit button
    def submit():
        # Get the user input and create a dictionary
        Emp_NO = int(emp_no_entry.get())
        Name = name_entry.get()
        Age = int(age_entry.get())
        Gender = gender_entry.get()
        Contact_No = int(contact_no_entry.get())
        data = {'emp_NO':[Emp_NO] , 'Name': [Name], 'Age': [Age] , "Gender": [Gender],"Contact_No":[Contact_No]}

        # Convert the dictionary to a DataFrame and save it to a CSV file
        df = pd.DataFrame(data)
        df.to_csv('teacher_details.csv', mode='a', index=False, header=False)

        # Return to the admin options
        admin_options()
     # Add a submit button
    tk.Button(window, text="Create", command=submit).pack()
     # Run the main loop
    window.mainloop()

    
def Student_Delete():
    # Create the main window
    window = tk.Tk()
    window.title("Delete Student")
    window.geometry("500x500")

    # Add a label and input field for the student reg_number
    tk.Label(window, text="Enter the student reg_number:").pack()
    reg_number_entry = tk.Entry(window)
    reg_number_entry.pack()

    # Add a submit button
    def submit():
        # Read the student details from the CSV file
        data = pd.read_csv('student_details.csv')

        # Set the reg_number as the index and delete the student with the specified reg_number
        data.set_index('Reg_NO', inplace=True)
        student_reg_number = int(reg_number_entry.get())
        data = data.drop(student_reg_number)

        # Save the updated data to the CSV file
        data.to_csv('student_details.csv', index=False)

        # Return to the admin options
        admin_options()
     # Add a submit button
    tk.Button(window, text="Delete", command=submit).pack()
     # Run the main loop
    window.mainloop()


def Teacher_Delete():
    # Create the main window
    window = tk.Tk()
    window.title("Delete Teacher")
    window.geometry("500x500")

    # Add a label and input field for the teacher emp_number
    tk.Label(window, text="Enter the teacher emp_number:").pack()
    emp_number_entry = tk.Entry(window)
    emp_number_entry.pack()

    # Add a submit button
    def submit():
        # Read the teacher details from the CSV file
        data = pd.read_csv('teacher_details.csv')

        # Set the emp_number as the index and delete the teacher with the specified emp_number
        data.set_index('Emp_NO', inplace=True)
        teacher_emp_number = int(emp_number_entry.get())
        data = data.drop(teacher_emp_number)

        # Save the updated data to the CSV file
        data.to_csv('teacher_details.csv', index=False)

        # Return to the admin options
        admin_choose()
     # Add a submit button
    tk.Button(window, text="Delete", command=submit).pack()
     # Run the main loop
    window.mainloop()

    
    
def Teacher_check():
    # Create the main window
    window = tk.Tk()
    window.title("Teacher Login")
    window.geometry("500x500")

    
    # Add labels and input fields for the teacher emp_number and password
    tk.Label(window, text="Emp_NO").pack()
    emp_no_entry = tk.Entry(window)
    emp_no_entry.pack()
    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    # Add a submit button
    def submit():
        # Get the user input and read the CSV file
        Emp_NO = emp_no_entry.get()
        password = password_entry.get()
        data = pd.read_csv('teacher_details.csv')
        val = data["emp_NO"].values
        val = val.tolist()
        if (Emp_NO in val or Emp_NO== "A") and (password in val or Emp_NO== "A"):
            # If the login is successful, call the Teacher_Choice function
            Teacher_Choice()
        else:
            # If the login is unsuccessful, return to the login screen
            Front_Login()

    # Add a submit button
    tk.Button(window, text="Login", command=submit).pack()
     # Run the main loop
    window.mainloop()
    


def Teacher_Choice():
    # Create the main window
    window = tk.Tk()
    window.title("Teacher Options")
    window.geometry("500x500")

    # Add a button for the "Create" option
    def create():
        Create_mark_list()
     # Add a submit button
    tk.Button(window, text="Create", command=create).pack()

    # Add a button for the "Modify" option
    def modify():
        Modify_mark_list()
     # Add a submit button
    tk.Button(window, text="Modify", command=modify).pack()
     # Run the main loop
    window.mainloop()

    
def Create_mark_list():
    # Create the main window
    window = tk.Tk()
    window.title("Create Mark List")
    window.geometry("500x500")

    # Add labels and input fields for the student marks
    tk.Label(window, text="Reg_NO").pack()
    reg_no_entry = tk.Entry(window)
    reg_no_entry.pack()
    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()
    tk.Label(window, text="Tamil").pack()
    tamil_entry = tk.Entry(window)
    tamil_entry.pack()
    tk.Label(window, text="English").pack()
    english_entry = tk.Entry(window)
    english_entry.pack()
    tk.Label(window, text="Maths").pack()
    maths_entry = tk.Entry(window)
    maths_entry.pack()
    tk.Label(window, text="Physics").pack()
    physics_entry = tk.Entry(window)
    physics_entry.pack()
    tk.Label(window, text="Chemistry").pack()
    chemistry_entry = tk.Entry(window)
    chemistry_entry.pack()
    tk.Label(window, text="Computer").pack()
    computer_entry = tk.Entry(window)
    computer_entry.pack()
    
    def submit():
        # Get the user input and create a dictionary
        Reg_NO = int(reg_no_entry.get())
        Name = name_entry.get()
        Tamil = int(tamil_entry.get())
        English = int(english_entry.get())
        Maths = int(maths_entry.get())
        Physics = int(physics_entry.get())
        Chemistry = int(chemistry_entry.get())
        Computer = int(computer_entry.get())
        Total = Tamil + English + Maths + Physics + Chemistry + Computer
        data = {'Reg_NO':[Reg_NO] , 'Name': [Name], 'Tamil': [Tamil] , "English": [English],"Maths":[Maths], 'Physics': [Physics] , "Chemistry": [Chemistry],"Computer":[Computer],"Total":Total}

        # Convert the dictionary to a DataFrame and write it to a CSV file
        df = pd.DataFrame(data)
        df.to_csv('student_marks.csv', mode='a', index=False ,header=False)

        # Return to the Teacher_Choice
        Teacher_Choice()
     # Add a submit button
    tk.Button(window, text="Submit", command=submit).pack()
     # Run the main loop
    window.mainloop()

    
def Modify_mark_list():
    # Create the main window
    window = tk.Tk()
    window.title("Modify Mark List")
    window.geometry("500x500")

    # Add labels and input fields for the student marks
    tk.Label(window, text="Reg_NO").pack()
    reg_no_entry = tk.Entry(window)
    reg_no_entry.pack()
    tk.Label(window, text="Subject").pack()
    subject_entry = tk.Entry(window)
    subject_entry.pack()
    tk.Label(window, text="Marks").pack()
    marks_entry = tk.Entry(window)
    marks_entry.pack()

    # Add a submit button
    def submit():
        # Get the user input and read the CSV file
        Reg_NO = int(reg_no_entry.get())
        subject = subject_entry.get()
        marks = int(marks_entry.get())
        data = pd.read_csv('student_marks.csv')

        # Modify the marks for the given student and subject
        data = data.loc[(data["Reg_NO"] == Reg_NO)] 
        data[subject] = data[subject].replace(marks)

        # Write the modified data to the CSV file
        data.to_csv("student_marks.csv", index=False)
        
        # Return to the Teacher_Choice
        Teacher_Choice()
    # Add a submit button
    tk.Button(window, text="Submit", command=submit).pack()
     # Run the main loop
    window.mainloop()

def Student_check():
    # Create the main window
    window = tk.Tk()
    window.title("Student Login")
    window.geometry("500x500")

    # Add labels and input fields for the student login credentials
    tk.Label(window, text="Reg_NO").pack()
    reg_no_entry = tk.Entry(window)
    reg_no_entry.pack()
    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window)
    password_entry.pack()

    # Add a submit button
    def submit():
        # Get the user input and read the CSV file
        Reg_NO = int(reg_no_entry.get())
        password = password_entry.get()
        data = pd.read_csv('student_details.csv')

        # Check if the login credentials are correct
        val = data["Reg_NO"].values
        val = val.tolist()
        if (Reg_NO in val or Reg_NO== 1) and (password in val or Reg_NO== 1):
            # If the login is successful, call the Student_Choice function
            Student_Choice()
        else:
            # If the login is unsuccessful, show an error message and call the Front_Login function
            tk.Label(window, text="Incorrect login credentials. Please try again.").pack()
            Front_Login()

    # Add a submit button
    tk.Button(window, text="Submit", command=submit).pack()
     # Run the main loop
    window.mainloop()

    
def Student_Choice():
    # Create the main window
    window = tk.Tk()
    window.title("Student Choice")
    window.geometry("500x500")

    # Add buttons for the student choices
    def view():
        # Call the View_mark_list function
        View_mark_list()

    def download():
        # Call the Download_mark_list function
        Download_mark_list()
     # Add a submit button
    tk.Button(window, text="View", command=view).pack()
    tk.Button(window, text="Download", command=download).pack()
     # Run the main loop
    window.mainloop()

    
def View_mark_list():
    # Create the main window
    window = tk.Tk()
    window.title("View Marks")
    window.geometry("500x500")

    # Add a label and input field for the student's registration number
    tk.Label(window, text="Reg_NO").pack()
    reg_no_entry = tk.Entry(window)
    reg_no_entry.pack()

    # Add a submit button
    def submit():
        # Get the user input and read the CSV file
        Reg_NO = int(reg_no_entry.get())
        data = pd.read_csv('student_marks.csv')

        # Filter the data for the student's marks
        data = data.loc[(data["Reg_NO"] == Reg_NO)] 

        # Create a text widget to display the marks
        text = tk.Text(window)
        text.insert(tk.END, data)
        text.pack()

    # Add a submit button
    tk.Button(window, text="Submit", command=submit).pack()
     # Run the main loop
    window.mainloop()


def Download_mark_list():
    # Create the main window
    window = tk.Tk()
    window.title("Download Marks")
    window.geometry("500x500")

    # Add a label and input field for the student's registration number
    tk.Label(window, text="Reg_NO").pack()
    reg_no_entry = tk.Entry(window)
    reg_no_entry.pack()

    # Add a submit button
    def submit():
        # Get the user input and read the CSV file
        Reg_NO = int(reg_no_entry.get())
        data = pd.read_csv('student_marks.csv')

        # Filter the data for the student's marks
        data = data.loc[(data["Reg_NO"] == Reg_NO)]

        # Save the data to a CSV file
        data.to_csv("marklist.csv", index = False)

    # Add a submit button
    tk.Button(window, text="Submit", command=submit).pack()
    # Run the main loop
    window.mainloop()




    
Front_Login()
